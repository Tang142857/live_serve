"""
The main serve program for live serve.

@author: Tang142857
@project: live_serve
@file: main.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
from http import server

from serve_pack import template

if __name__ == '__main__':
    server_address = ('', 8080)
    SERVER = server.HTTPServer(server_address, template.MainResponse)
    SERVER.serve_forever()
