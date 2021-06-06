"""
Serve package

@author: Tang142857
@project: live_serve
@file: __init__.py
@date: 2021-05-03
Copyright(c): DFSA Software Develop Center
"""
__all__ = ['serve']

import os
import sys

sys.path.append(os.path.dirname(__file__))
# add myself to path to let the import more convenient
import share_memory
