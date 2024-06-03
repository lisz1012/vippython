# Author: lisz1012
# Creation date and time: 6/2/24 5:02 PM

import sys
import time
import urllib.request as req
import math

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(24.0))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print('------------------')
print(time.time())
print(time.localtime(time.time()))
print('------------------')
print(req.urlopen('http://www.baidu.com').read())
print(math.pi)

