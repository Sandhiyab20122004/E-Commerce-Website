import http.server
import socketserver
import json

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/products":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            with open("products.json", "r") as file:
                products = json.load(file)

            self.wfile.write(json.dumps(products).encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
    