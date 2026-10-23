import os
import json
import base64
import urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

DITTO_URL = "http://localhost:8080"
THING_ID = "org.openegiz.kachar:mine-01"


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] != "/api/ditto":
            return super().do_GET()

        password = os.environ.get("DITTO_PASSWORD")
        if not password:
            return self.send_json(503, {"connected": False, "error": "Password missing"})

        user = os.environ.get("DITTO_USER", "ditto")
        credentials = base64.b64encode(
            f"{user}:{password}".encode()
        ).decode()

        request = urllib.request.Request(
            f"{DITTO_URL}/api/2/things/{THING_ID}",
            headers={"Authorization": f"Basic {credentials}"}
        )

        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                thing = json.load(response)

            features = thing["features"]

            self.send_json(200, {
                "connected": True,
                "source": "Eclipse Ditto",
                "production": features["production"]["properties"]["value"],
                "scenario": features["scenario_production"]["properties"]["value"],
                "improvement": features["improvement"]["properties"]["value"]
            })
        except Exception:
            self.send_json(502, {
                "connected": False,
                "error": "Ditto request failed"
            })

    def send_json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("Kachar Mine API: http://localhost:8766")
    ThreadingHTTPServer(("127.0.0.1", 8766), Handler).serve_forever()
