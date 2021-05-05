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


class ShareMemory(object):
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
