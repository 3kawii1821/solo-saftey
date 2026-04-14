# keysaf.py - Simple HTTP server on port 80
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class LicenseHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/verify-license':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            print(f"[PYTHON] Received: {post_data.decode()}")
            
            try:
                data = json.loads(post_data.decode())
                license_key = data.get('licenseKey', '')
                print(f"[PYTHON] License: {license_key}")
            except:
                pass
            
            response = {"status": "valid", "message": "License Verified Successfully"}
            response_body = json.dumps(response)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body.encode())
            print(f"[PYTHON] Returned: {response}")
    
    def log_message(self, format, *args):
        print(f"[PYTHON] {format % args}")

if __name__ == '__main__':
    port = 80
    server = HTTPServer(('0.0.0.0', port), LicenseHandler)
    print(f"[PYTHON] HTTP Server running on http://0.0.0.0:{port}")
    print(f"[PYTHON] Waiting for solo-safety.com requests...")
    server.serve_forever()