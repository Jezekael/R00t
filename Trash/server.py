from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class LeakHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        path = query.get("path", [""])[0]
        status = query.get("status", [""])[0]

        if status == "200":
            print(f"\033[92m[VALID] {path} → {status}\033[0m")  # vert
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        return  # désactive le log HTTP par défaut

if __name__ == "__main__":
    print("[*] Server listening on http://0.0.0.0:8000 — Only display 200")
    HTTPServer(("0.0.0.0", 8000), LeakHandler).serve_forever()
