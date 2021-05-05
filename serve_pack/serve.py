"""
The serve serve model.

@author: Tang142857
@project: live_serve
@file: serve.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
import re
import sys
from http import server

import processor


class MainResponse(server.BaseHTTPRequestHandler):
    def log_request(self, code):
        print(f"At port: {self.server.server_port} -> ", end='')
        server.BaseHTTPRequestHandler.log_request(self, code)
        self.log_in_file()

    def log_in_file(self):
        """
        Called by log requests 
        write the log into file ,closed in --debug
        """
        if '--debug' in sys.argv:
            return
        else:
            pass

    def do_GET(self):
        # if customers use root directory
        # lead them to index.html

        requests_manager(self)


def requests_manager(res: MainResponse):
    """Deal with all the requests."""
    if res.path == '/':
        res.send_response(301)
        res.send_header('location', '/index.html')
        res.end_headers()
        return

    use_callback(res)


def use_callback(res: MainResponse):
    for exp in processor.URL_LIST.keys():
        print(f'{exp=}:{res.path=}-{re.match(exp,res.path)=}')
        if re.match(exp, res.path):
            processor_ = processor.URL_LIST[exp]
            break
    # don't forget ,anyway the super manager will be the processor
    return processor_(res)
