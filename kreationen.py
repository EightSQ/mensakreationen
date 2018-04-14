#!/usr/bin/env python

import os
from sys import argv
import markovify
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("PORT", 8080))

speise_file = "speisen2.txt"
if len(argv) == 2:
    speise_file = argv[1]

""" build markov chain """
with open(speise_file) as f:
    text = f.read()
    f.close()

text_model = markovify.NewlineText(text, state_size=1)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytearray("<html><head><title>Mensakreationen</title></head><body><h2>"+text_model.make_sentence(tries=100)+"</h2></body></html>", 'iso-8859-1'))

def run(server_class=HTTPServer, handler_class=S, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
