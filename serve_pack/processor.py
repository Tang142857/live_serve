"""
The processor for the serve.

@author: Tang142857
@project: workspace
@file: processor.py
@date: 2021-05-05
Copyright(c): DFSA Software Develop Center
"""
from http import server

import api
import file_types
import share_memory


class API(object):
    """The api.py's public functions."""
    def __init__(self):
        attrs = dir(api)
        attrs.remove('server')
        # remove the server form the api list

        for attr in attrs:
            if not attr.startswith('_'):
                setattr(self, attr, getattr(api, attr))

    def __str__(self):
        result = f'{super().__str__()}:\n'
        for attribute_name in dir(self):
            if attribute_name.startswith('_'):
                continue
            else:
                result += attribute_name + ' -> ' + str(
                    getattr(self, attribute_name)) + '\n'
        return result

    def get_api(self, path: str):
        if path.startswith('/'):
            path = path[1:]  # cut the first /
        path_item = path.split('/')

        father_api = self
        try:
            for item in path_item:
                father_api = getattr(father_api, item)
        except AttributeError:
            return None
        return father_api


app_interface = API()
# print(app_interface)


def api_manager(res: server.BaseHTTPRequestHandler):
    """
    When the pages' javascript cell me for data ,
    use the api manager.
    All this requests starts with /api/...
    """
    api_path = res.path.replace('/api', '')
    # you will get a path like /test_api

    if (api_ := app_interface.get_api(api_path)) is None:
        # could not find the required api
        error_page = share_memory.PAGES.ERROR_PAGE % {
            'code':
            404,
            'explain':
            'Required API Not Be Found  :(',
            'message':
            'Required API Not Be Found ,please check your script or see development guide'
        }

        res.send_response(404)
        res.send_header('content-type', 'text/html')
        res.send_header('content-length', str(len(error_page.encode('utf-8'))))
        res.end_headers()

        res.wfile.write(error_page.encode('utf-8'))
    else:
        api_(res)


def file_manager(res: server.BaseHTTPRequestHandler):
    """
    When the browser visit the site ,just return file
    file manager just serve basic file service.
    """
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
        error_page = share_memory.PAGES.ERROR_PAGE % {
            'code': 404,
            'explain': str(ans),
            'message': '404 ERROR'
        }
        res.send_response(404)
        res.send_header('content-type', 'text/html')
        res.send_header('content-length', str(len(str(error_page))))
        res.end_headers()

        res.wfile.write(error_page.encode('utf-8'))
