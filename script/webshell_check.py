#!/usr/bin/env python
# __author__= 'w8ay'

#对每个.php结尾的文件进行一句话爆破
import os
import sys

from lib.core.downloader import HtmlDownloader

filename = os.path.join(sys.path[0],"data","web_shell.dic")
payload = []
f = open(filename)
a = 0
for i in f:
    payload.append(i.strip())
    a+=1
    if(a==999):
        break

class Spider:
    def run(self,url,html):
        if(not url.endswith(".php")):
            return False
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";' % _payload
            r = HtmlDownloader.post(url,post_data)
            if(r):
                print("webshell:%s"%r)
                return True
        return False
