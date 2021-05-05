"""
The porcessor for the serve.

@author: Tang142857
@project: workspace
@file: processor.py
@date: 2021-05-05
Copyright(c): DFSA Software Develop Center
"""
from http import server

import file_types

# url list is used to match the url of requests
# write the re expreession as key and callback function as value


def diary(res: server.BaseHTTPRequestHandler):
    res.send_header('provider', 'diary_serve')


def video(res: server.BaseHTTPRequestHandler):
    res.send_header('provider', 'video_server')


def super_manager(res: server.BaseHTTPRequestHandler):
    # only send the file with 200
    resource_path = res.path[1:]

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
        res.send_header('content-type', 'text/html')
        res.send_header('content-length', str(len(str(ans))))
        res.end_headers()

        error_page = server.DEFAULT_ERROR_MESSAGE % {
            'code': 404,
            'explain': str(ans),
            'message': '404 ERROR'
        }

        res.wfile.write(error_page.encode('utf-8'))


################################### split here #######################################
# have not start the sub serve
URL_LIST = {
    # r'^/pages/diary.html': diary,
    # r'^/pages/videos.html': video,
    r'.*': super_manager
}
