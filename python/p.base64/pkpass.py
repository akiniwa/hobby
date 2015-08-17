"""pkpass base64 decode"""
import base64
import json

def encode():
    """encode komovie.pkpass"""
    with open('komovie.pkpass', 'rb') as fin, open('komovie.base64', 'wt') as fout:
        base64.encode(fin, fout)

def decode():
    """decode komovie.base64"""
    with open('komovie.base64', 'rt') as fin, open('komovie-out.pkpass', 'wb') as fout:
        base64.decode(fin, fout)

def decode_api():
    """decode json from java api"""
    with open('pkpass.base64', 'rt') as ftest, open('pkpass.pkpass', 'wb') as fout:
        fout.write(base64.b64decode(json.load(ftest)['komovie_pkpass']))

# komovie.pkpass => komovie.base64
encode()
# komovie.base64 => komovie-out.pkpass
decode()
# pkpass.base64  => pkpass.pkpass
decode_api()
