#!/usr/bin/env python
# __author__= 'w8ay'
import os

import sys


class spiderplusg(object):

    def __init__(self,plugin,disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        sys.path.append(plugin)
        self.plugin = os.getcwd()+'/' +plugin

    def list_plusg(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(filter_func, os.listdir(self.plugin))
        return list(dir_exploit)

    def work(self,url,html):
        for plugin in self.list_plusg():
            m = __import__(plugin.split('.')[0])
            try:
                Spider = getattr(m, 'Spider')
                p = Spider()
                s =p.run(url,html)
            except Exception as e:
                print(e )