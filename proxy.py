#!/usr/bin/env python3
"""
Proxy local para contornar CORS entre localhost:8080 e o webhook N8N.
Usa curl para fazer a requisição HTTPS (mais confiável no macOS).
Porta: 3001
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json

N8N_URL = 'https://lucasamarale.app.n8n.cloud/webhook/nola-cs-chatbot-webhook/chat'

class ProxyHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass

    def _cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')

            result = subprocess.run(
                [
                    'curl', '-s',
                    '-X', 'POST',
                    '-H', 'Content-Type: application/json',
                    '-d', body,
                    '--max-time', '30',
                    N8N_URL
                ],
                capture_output=True,
                timeout=35
            )

            response_body = result.stdout if result.stdout else b'{}'

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._cors_headers()
            self.end_headers()
            self.wfile.write(response_body)

        except Exception as e:
            err = json.dumps({'output': f'Erro no proxy: {str(e)}'}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._cors_headers()
            self.end_headers()
            self.wfile.write(err)

if __name__ == '__main__':
    print(f'🔀  Proxy rodando em http://localhost:3001')
    server = HTTPServer(('localhost', 3001), ProxyHandler)
    server.serve_forever()
