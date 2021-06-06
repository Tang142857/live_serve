"""
The serve serve model.

@author: Tang142857
@project: live_serve
@file: serve.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
import os
import sys
from http import server

import processor
import share_memory


def log_in_file(info_str: str):
    """
    Called by log requests
    write the log into file ,closed in --debug
    """
    share_memory.logger.log(info_str)


class MainResponse(server.BaseHTTPRequestHandler):
    def log_message(self, format_, *args):
        info_string = 'At %(serve_address)s -> %(visitor)s [%(time)s] - %(message)s\n'
        info_dict = {
            'serve_address': self.server.server_address,
            'time': self.log_date_time_string(),
            'visitor': str(self.client_address),
            'message': format_ % args
        }
        info_string %= info_dict
        sys.stderr.write(info_string)
        log_in_file(info_string)

    # all requests will send to manager
    def do_GET(self):
        requests_manager(self)

    def do_POST(self):
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
