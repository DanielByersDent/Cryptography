#runtime 3.5 python

import hashlib


def modify(message):
    l = list(message)
    l(0) = l(0) ^ 1
    return bytes(1)
message = "Hello world from hash".encode()

sha256 = hashlib.sha256()
sha256.update(message)
d = sha256.digest()
print(d)

m = modify(message)
print(message)