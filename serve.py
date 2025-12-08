#!/usr/bin/env python3
"""Simple static file server for testing GrantPing frontend."""

import http.server
import socketserver

PORT = 3000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

Handler = MyHTTPRequestHandler

print(f"Starting GrantPing frontend server on http://localhost:{PORT}")
print("Open your browser to http://localhost:3000")
print("Press Ctrl+C to stop")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
