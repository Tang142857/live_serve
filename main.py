"""
The main serve program for live serve.

@author: Tang142857
@project: live_serve
@file: main.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
from http import server
from threading import Thread

from serve_pack import serve, share_memory

if __name__ == '__main__':
    server_address = ('', 8080)
    server_address_2 = ('', 8082)

    SERVER_1 = server.HTTPServer(server_address, serve.MainResponse)
    SERVER_2 = server.HTTPServer(server_address_2, serve.MainResponse)
    SERVE_THREAD_1 = Thread(target=SERVER_1.serve_forever)
    SERVE_THREAD_2 = Thread(target=SERVER_2.serve_forever)
    SERVE_THREAD_1.start()
    SERVE_THREAD_2.start()
    SERVE_THREAD_2.join()
    SERVE_THREAD_1.join()
