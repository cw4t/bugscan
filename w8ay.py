#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys

from lib.core.craw import SpiderMain
from lib.core import webdna

def main():
    root = "http://bbs.emlog.net"
    disallow = ['sql_inject.py', 'xss_check.py']
    threadNum = 10
    #CMdna
    wb = webdna.Webdna(root)
    r = wb.run()
    if(r):
        print("CMS识别结果",r)
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw(disallow)

if __name__ == '__main__':
    main()