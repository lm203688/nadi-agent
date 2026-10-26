"""HTTP server for the frontend. Streams the team trace as JSON lines."""
from __future__ import annotations
import argparse, json, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from nadi_agent.core import run, load_user, new_session  # noqa: E402


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, obj, status=200):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_text(self, text, status=200):
        data = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self._send_json({"ok": True, "version": "0.1.0-championship"})
            return
        if self.path == "/":
            self._send_text("Nadi Agent API · GET /v1/deliberate · GET /health")
            return
        self._send_json({"error": "not found"}, 404)

    def do_POST(self):
        if self.path != "/v1/deliberate":
            self._send_json({"error": "not found"}, 404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        try:
            payload = json.loads(body)
        except json.JSONDecodeError as e:
            self._send_json({"error": f"bad json: {e}"}, 400)
            return

        message = payload.get("message", "").strip()
        user_id = payload.get("user_id", "anonymous")
        if not message:
            self._send_json({"error": "message required"}, 400)
            return

        session = load_user(user_id) if (Path(__file__).parent.parent / "demo_users" / f"{user_id}.json").exists() else new_session(user_id)
        t0 = time.time()
        result = run(message, session)

        self._send_json({
            "message": message,
            "session_id": session["session_id"],
            "response": result.response,
            "confidence": result.confidence,
            "evidence_count": result.evidence_count,
            "red_flags": result.red_flags,
            "evidence_ids": result.evidence_ids,
            "sources": result.sources,
            "safety_note": result.safety_note,
            "trace": result.agent_trace,
            "server_elapsed_seconds": round(time.time() - t0, 3),
        })

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--host", default="127.0.0.1")
    args = p.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Nadi Agent API listening on http://{args.host}:{args.port}")
    print(f"  POST /v1/deliberate {{\"message\":\"...\",\"user_id\":\"fatima\"}}")
    print(f"  GET  /health")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
