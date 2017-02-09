#!/usr/bin/env python
#-*- coding:utf-8 -*-

from lib.core import downloader,common
import sys,os

payload = []
filename = os.path.join(sys.path[0],"data","xss.txt")
f = open(filename)
for i in f:
    payload.append(i.strip())

class Spider:
    def run(self,url,html):
        download = downloader.HtmlDownloader()
        urls = common.urlsplit(url)
        if urls is None:
            return False
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("my_Payload",_payload)
                #我们需要对URL每个参数进行拆分,测试
                _str = download.request(_url)
                if _str is None:
                    return False
                if(_str.find(_payload)!=-1):
                    return "xss found:%s"%url
        return False

