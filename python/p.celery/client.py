# -*- coding: utf-8 -*-

import time
from tasks import add

result = add.delay(4, 4)

# while not result.ready():
#     print 'waiting...'
#     time.sleep(2)
#     print dir(result)
# print result.result

print result.get(timeout=2)
# print result.get(propagate=False)
