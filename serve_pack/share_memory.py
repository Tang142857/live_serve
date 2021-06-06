"""
Some data may be share here ,
normally: logger,date base serve.
Because python will only load the model once ,
other imports is its refer ,so we can do this

@author: Tang142857
@project: workspace
@file: share_memory.py
@date: 2021-05-05
Copyright(c): DFSA Software Develop Center
"""
import os
import sys


def get_user_home():
    return os.path.expanduser('~/')


def load_file(path: str):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return 'SERVER\'S FILE EXCEPTION'


class Logger(object):
    def __init__(self):
        self.log_file_path = get_user_home() + '.log/live_serve.log'
        self.log_directory = get_user_home() + '.log'

    def log(self, string: str):
        """
        Log the status to file and console
        use --debug to close the function.
        Don not use \n.
        """
        if '--debug' in sys.argv:
            return
        else:
            try:
                with open(self.log_file_path, 'a') as f:
                    f.write(string)
            except FileNotFoundError:
                # create the directory and retry
                os.makedirs(self.log_directory)
                with open(self.log_file_path, 'a') as f:
                    f.write(string)


logger = Logger()


class ShareMemory(object):
    def __init__(self):
        self.server_pack_path = os.path.dirname(__file__) + '/'

    def __str__(self):
        """Just for pretty print."""
        result = ''
        for attribute_name in dir(self):
            if attribute_name.startswith('_'):
                continue
            else:
                result += attribute_name + ' -> ' + str(
                    getattr(self, attribute_name)) + '\n'
        return result


memory = ShareMemory()


class StaticPageModels(object):
    def __init__(self):
        self.PAGES_PATH = memory.server_pack_path + 'pages/'
        self.ERROR_PAGE = load_file(self.PAGES_PATH + 'error.html')


PAGES = StaticPageModels()

if __name__ == '__main__':
    # test the logger
    logger.log('test log\n')
