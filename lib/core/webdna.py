#!/usr/bin/env python
# __author__= 'w8ay'


import sys, os, json, asyncio, hashlib, aiohttp


class CMSError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Webdna:
    def __init__(self, url):
        filename = os.path.join(sys.path[0], "data", "data.json")
        fp = open(filename)
        self.j = json.load(fp)
        self.url = url
        self.loop = None
        fp.close()

    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()

    async def whatweb(self, d, scode):
        if d["md5"]:
            md5 = self.getmd5(scode)
            if (md5 == d["md5"]):
                print(d)
                raise CMSError(d)
        else:
            re = d["re"]
            if (scode.decode("utf-8", "ignore").find(re) != -1):
                print(d)
                raise CMSError(d)

    async def fetch(self, d, session):
        _url = self.url
        url = _url + d["url"]
        async with session.get(url, timeout=10) as response:
            status = response.status
            if status != 200:
                return False
            scode = await response.read()
            if not scode:
                return
            await self.whatweb(d, scode)

    async def run1(self):
        # Fetch all responses within one Client session,
        # keep connection alive for all requests.
        async with aiohttp.ClientSession() as session:
            tasks = []
            for d in self.j:
                task = asyncio.ensure_future(self.fetch(d, session))
                tasks.append(task)
            await asyncio.gather(*tasks)
            # you now have all response bodies in this variable
            # print(responses)

    def run(self):
        loop = asyncio.get_event_loop()
        self.loop = loop
        result = {}
        try:
            future = asyncio.ensure_future(self.run1())
            loop.run_until_complete(future)
        except CMSError as e:
            result = str(e)
            # print(e)
            self.loop.stop()
        except Exception as e:
            print(e)
        return result