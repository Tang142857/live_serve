"""
API tool kit for ls
all function here except which starts with _ will be add to processor.API
function here should receive res as its first argument.

@author: Tang142857
@project: live_serve
@file: api.py
@date: 2021-05-16
Copyright(c): DFSA Software Develop Center
"""
from http import server


def test_api(res: server.BaseHTTPRequestHandler):
    res.send_response(200)
    res.send_header('data', 'hello world')
    res.send_header('content-type', 'text/html')
    res.end_headers()
    res.wfile.write(b'hello world<br>')