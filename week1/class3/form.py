from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))

        # Extracting data from the form
        name = post_params.get('name', [''])[0]
        email = post_params.get('email', [''])[0]

        # Response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Sending a simple response
        response = f"Hello {name}, your email {email} was submitted successfully!"
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
# how to run the server 
# python form.py
# open the browser and go to http://localhost:8000 
if __name__ == '__main__':
    run()