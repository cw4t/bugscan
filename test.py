import json
import os

import sys

from script import xss_check
from lib.core import Plugs,webdna
from script import email_search

if __name__ == '__main__':
    url = "http://www.moonsec.com/"
    wb = webdna.Webdna(url)
    wb.run()

    pass

