import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Yuta serving at port", PORT)
    httpd.serve_forever()

#exec: curl localhost:8000
