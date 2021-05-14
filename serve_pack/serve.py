"""
The serve serve model.

@author: Tang142857
@project: live_serve
@file: serve.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
import sys
from http import server

import processor


class MainResponse(server.BaseHTTPRequestHandler):
    def log_in_file(self):
        """
        Called by log requests 
        write the log into file ,closed in --debug
        """
        if '--debug' in sys.argv:
            return
        else:
            # TODO log in file
            pass

    def do_GET(self):
        status = f'At port -> {self.server.server_port}'
        print(status, end='')
        requests_manager(self)


def requests_manager(res: MainResponse):
    """Deal with all the requests."""
    # some simple visitor guide write here
    if res.path == '/':  # root guider
        res.send_response(301)
        res.send_header('location', '/index.html')
        res.end_headers()
        return

    # tell if it use api or just a file
    if res.path.startswith('/api'):
        processor.api_manager(res)
    else:
        processor.file_manager(res)
