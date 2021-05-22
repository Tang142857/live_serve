"""
Some data may be share here ,
normally: loger,date base serve.
Because python will only load the model once ,
other imports is its refer ,so we can do this

@author: Tang142857
@project: workspace
@file: share_memory.py
@date: 2021-05-05
Copyright(c): DFSA Software Develop Center
"""
import sys
import os


def get_user_home():
    return os.path.expanduser('~')


class Logger(object):
    def __init__(self):
        self.log_file_path = get_user_home() + '.log/live_serve.log'

    def log(self, pattern, *arg):
        """
        Log the status to file and consol
        use --debug to close the function.
        Don not use \n.
        """
        string = (pattern % arg) + '\n'
        sys.stderr.write(string)
        if '--debug' in sys.argv:
            return
        else:
            with open(self.log_file_path, 'a') as f:
                f.write(string)


logger = Logger()


class ShareMemory(object):
    def __init__(self):
        pass

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
