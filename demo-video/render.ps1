# ---------------------------------------------------------------
# Nadi demo-video renderer
#
# Usage:
#   .\render.ps1 -Audio "narration.m4a"           -> produces final.mp4
#   .\render.ps1 -SlidesOnly                      -> produces final.mp4 (silent, subtitles only)
#
# Prerequisites:
#   ffmpeg in PATH (verify: ffmpeg -version)
#   This folder already contains subtitles_en.srt, storyboard.md, script.md
#
# Optional: put one PNG per storyboard scene in ./scenes/ (scene_01.png ...
#           scene_20.png) to build a slideshow track instead of black background.
# ---------------------------------------------------------------
param(
    [string]$Audio,
    [switch]$SlidesOnly
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: ffmpeg not found in PATH." -ForegroundColor Red
    Write-Host "Install ffmpeg (any one of these):" -ForegroundColor Yellow
    Write-Host "  1. winget install --id Gyan.FFmpeg"
    Write-Host "  2. scoop install ffmpeg"
    Write-Host "  3. choco install ffmpeg"
    Write-Host "  4. Download from https://www.gyan.dev/ffmpeg/builds/ and put ffmpeg.exe in PATH"
    exit 1
}

# Sanity check that ffmpeg is actually executable (avoids the WinGet alias trap)
try {
    $versionOut = & ffmpeg -version 2>&1
    if ($LASTEXITCODE -ne 0 -or -not $versionOut) {
        throw "ffmpeg not responding"
    }
} catch {
    Write-Host "ERROR: ffmpeg in PATH is not a real executable (Windows Store alias?). Install a real build and re-run." -ForegroundColor Red
    Write-Host "Try: winget install --id Gyan.FFmpeg  (real executable, works in scripts)" -ForegroundColor Yellow
    exit 1
}

$base = "base.mp4"
$video = $base
$audioFile = "audio_src.m4a"
$concatFile = "concat.txt"

# 1. Build the video track
Write-Host "[1/4] Building video track..."
if (Test-Path "scenes") {
    $pngs = Get-ChildItem "scenes\*.png" | Sort-Object Name
    if ($pngs.Count -gt 0) {
        Write-Host "     Found $($pngs.Count) scene images in ./scenes/"
        "file '" + ($pngs[0].FullName -replace '\\','/') + "'" | Out-Null
        (
            foreach ($p in $pngs) { "file '$((($p.FullName) -replace '\\','/'))'" }
        ) | Set-Content -Encoding UTF8 $concatFile
        ffmpeg -y -f concat -safe 0 -i $concatFile `
            -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p" `
            -r 30 -t 90 -c:v libx264 -preset veryfast -crf 28 slideshow.mp4 2>&1 | Out-Null
        $video = "slideshow.mp4"
        Remove-Item $concatFile -Force
    }
} else {
    Write-Host "     No scenes/ folder — using black background."
    ffmpeg -y -f lavfi -i "color=c=black:s=1920x1080:r=30" -t 90 -c:v libx264 -preset veryfast -crf 26 $base 2>&1 | Out-Null
}

# 2. Burn subtitles in
Write-Host "[2/4] Burning subtitles..."
$style = "FontName=Inter,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=1"
$srtEsc = (Resolve-Path "subtitles_en.srt").Path -replace '\\','/'
$srtParam = "subtitles=$srtEsc:force_style='$style'"
ffmpeg -y -i $video -vf "$srtParam" -c:v libx264 -preset veryfast -crf 26 subtitled.mp4 2>&1 | Out-Null
$video = "subtitled.mp4"

# 3. Audio track
Write-Host "[3/4] Audio track..."
if ($SlidesOnly) {
    ffmpeg -y -f lavfi -i "anullsrc=r=44100:cl=stereo" -t 90 -c:a aac -b:a 128k $audioFile 2>&1 | Out-Null
} elseif ($Audio -and (Test-Path $Audio)) {
    ffmpeg -y -i $Audio -c:a aac -b:a 128k $audioFile 2>&1 | Out-Null
} else {
    Write-Host "     No audio file — using silence."
    ffmpeg -y -f lavfi -i "anullsrc=r=44100:cl=stereo" -t 90 -c:a aac -b:a 128k $audioFile 2>&1 | Out-Null
}

# 4. Mux + fade out
Write-Host "[4/4] Mux + fade..."
ffmpeg -y -i $video -i $audioFile -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 -shortest final_tmp.mp4 2>&1 | Out-Null
ffmpeg -y -i final_tmp.mp4 `
    -filter_complex "[0:v]fade=t=out:st=88:d=2,format=yuv420p[v];[0:a]afade=t=out:st=88:d=2[a]" `
    -map "[v]" -map "[a]" -c:v libx264 -preset veryfast -crf 24 -c:a aac -b:a 128k final.mp4 2>&1 | Out-Null
Remove-Item final_tmp.mp4 -Force -ErrorAction SilentlyContinue

if (Test-Path final.mp4) {
    $size = (Get-Item final.mp4).Length / 1KB
    Write-Host ""
    Write-Host "Done. final.mp4  ($([int]$size) KB)" -ForegroundColor Green
    Write-Host "Upload final.mp4 to the competition submission portal."
} else {
    Write-Host "ERROR: final.mp4 was not produced. Check ffmpeg output above." -ForegroundColor Red
    exit 1
}
