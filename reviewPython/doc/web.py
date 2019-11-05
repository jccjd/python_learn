import sys
import os
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
from wsgiref.simple_server import make_server

def demo_app(environ, start_response):
    """
    示例的 app
    """
    stdout = "Hello world!\n"
    h = sorted(environ.items())
    for k, v in h:
        stdout += k + '=' + repr(v) + "\r\n"
    print(start_response)
    start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
    return [stdout.encode("utf-8")]


httpd = make_server('', 8000, demo_app)
print('Serving HTTP on port 8000...')
httpd.serve_forever()