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


class MainResponse(server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        info_string = 'At %(serve_address)s -> %(visitor)s [%(time)s] - %(message)s\n'
        info_dict = {
            'serve_address': self.server.server_address,
            'time': self.log_date_time_string(),
            'visitor': str(self.client_address),
            'message': format % args
        }
        info_string %= info_dict
        sys.stderr.write(info_string)
        self.log_in_file(info_string)

    def log_in_file(self, info_str: str):
        """
        Called by log requests 
        write the log into file ,closed in --debug
        """
        if '--debug' in sys.argv:
            return
        else:
            default_log_path = '%s/.service/log/live_serve.log'
            default_log_path %= os.path.expanduser('~')
            try:
                with open(default_log_path, 'a') as f:
                    f.write(info_str + '\n')
            except Exception as ans:
                print(f'Failed to write log file {str(ans)}')

    def do_GET(self):
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
