"""
The serve template model.

@author: Tang142857
@project: live_serve
@file: tmp.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
from http import server
import sys

import file_types


class PageSwap(object):
    def __init__(self):
        self.welcome_page = "hello"


class MainResponse(server.BaseHTTPRequestHandler):
    def log_request(self, code):
        print(f"At port: {self.server.server_port} -> ", end='')
        server.BaseHTTPRequestHandler.log_request(self, code)

    def do_GET(self):
        # if customers use root directory
        # lead them to index.html
        if self.path == '/':
            self.send_response(301)
            self.send_header('location', '/index.html')
            self.end_headers()
            return

        response_manager(self)


def response_manager(res: MainResponse):
    """Deal with all the requests."""
    # print(res.path)
    resource_path = res.path[1:]  # it starts with / :(
    # print(resource_path)

    try:
        with open(resource_path, 'rb') as f:
            bit_data = f.read()

        res.send_response(200)
        res.send_header('content-type',
                        file_types.get_file_type(resource_path))
        res.send_header('content-length', str(len(bit_data)))
        res.end_headers()

        res.wfile.write(bit_data)

    except FileNotFoundError as ans:
        res.send_response(404)
        res.send_header('content-type', 'text/plain')
        res.send_header('content-length', str(len(str(ans))))
        res.end_headers()

        res.wfile.write(str(ans).encode('utf-8'))
