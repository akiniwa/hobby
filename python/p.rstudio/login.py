# coding: utf-8

import base64
import requests
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import jiphy
import js2py

# jiphy.to.javascript(python_code)

js = """function(b, a, c) {var d = new $; d.X(c, a); b = d.N(b); d = ""; for (a = 0; a + 3 <= b.length; a += 3) { c = parseInt(b.substring(a, a + 3), 16); d += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(c >> 6) + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(c & 63) } if (a + 1 == b.length) { c = parseInt(b.substring(a, a + 1), 16); d += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(c << 2) } else if (a + 2 == b.length) {c = parseInt(b.substring(a, a + 2), 16); d += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(c >> 2) + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt((c & 3) << 4) } for (; (d.length & 3) > 0;) d += "="; return d };"""


def to_python():
    """to_python"""
    with open('encrypt.js') as f:
        print jiphy.to.python(f.read())


def bin2hex(binStr):
    return binascii.hexlify(binStr)


def hex2bin(hexStr):
    return binascii.unhexlify(hexStr)


def get(url):
    """get"""
    session = requests.session()
    respose = session.get(
        url,
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
        }
    )
    return respose
# 'apparent_encoding',
# 'close',
# 'connection',
# 'content',
# 'cookies',
# 'elapsed',
# 'encoding',
# 'headers',
# 'history',
# 'is_permanent_redirect',
# 'is_redirect',
# 'iter_content',
# 'iter_lines',
# 'json',
# 'links',
# 'ok',
# 'raise_for_status',
# 'raw',
# 'reason',
# 'request',
# 'status_code',
# 'text',
# 'url'


def print_respose(respose):
    """print_respose"""
    print '*' * 50
    print respose.status_code
    print respose.url
    print respose.text


url_home = 'http://localhost:8787'
url_auth = url_home + '/auth-public-key'
username = 'rstudio'
password = 'rstudio'
v = 'Svj0fDhGabnS%2F0TwQ6B%2FFDtPdSJPYJXchfSyNyFDDCMMLE5ErLzljcIfyxVAB2Uzs45xf65abjRCIOo8c7rxm%2Bp5zz7QEVTyYjZgWgnhLyEPmL6v2aRZqnV%2BGmJt4rVV2BIh%2Fb8rRjJrmdhjedkiogT3Ky%2FSyTXo948JSm%2F0MZw%3D'
pubkey = '010001:AFFEEADF16265BEB0E5524CAE0B11EA8CBEED8B6A24FD26062C31682E00BC647B1B92721C5A383BDF56C934F96322508F978AA0EF31E22B159D8FEB9AF7C01E5A0EE8F5E47EC18C0D2FF68EFCFE0429689B9723D4A958F8388A3AB2CB92134E9C121D80D5BF6B3AB5242EDAE888BA24EC7F91E2EAE9DF7B741A7B13366B36CBF'


def test_login():
    """test_login"""
    # home = get(url_home)
    pubkey = get(url_auth).text
    exp, mod = pubkey.split(':')
    print exp, mod
    # Svj0fDhGabnS%2F0TwQ6B%2FFDtPdSJPYJXchfSyNyFDDCMMLE5ErLzljcIfyxVAB2Uzs45xf65abjRCIOo8c7rxm%2Bp5zz7QEVTyYjZgWgnhLyEPmL6v2aRZqnV%2BGmJt4rVV2BIh%2Fb8rRjJrmdhjedkiogT3Ky%2FSyTXo948JSm%2F0MZw%3D
    # oGvCnFbpLkHYJD3wAq2ticwswkIv7FVOWuKrUsBCWMtOTaa7CW0z2CoA9daYmhK3Pz24+deHqW82+bPjShtNBxED82Hh9W10R2PQWP1qaTKRBAfwzQyBuq/OX2bZiwcRK1bSv0VS/Hm9qzVof67hx/fhlcex5jgoAmundrKwMJA=

    exp = long(exp, 16)
    mod = long(mod, 16)  # truncated for clarity
    rsa = RSA.construct((mod, exp))
    message = rsa.encrypt('{}\n{}'.format(username, password), 16)
    print message
    # print bin2hex(message)
    # message = map(bytes_to_long, message)
    # print message
    message = base64.encodestring(str(message[0]))
    print message
    print v

    # {
    #     'persist': '0',
    #     'appUri': '',
    #     'clientPath': '%2Fauth-sign-in',
    #     'v': '',
    # }

if __name__ == '__main__':
    # to_python()
    test_login()
    # import js2py
    # with open('encrypt.js') as f:
    #     obj = js2py.eval_js(f.read())
    #     print dir(obj)
    #     encrypt = obj.encrypt
    #     exp, mod = pubkey.split(':')
    #     encrypt('{}\n{}'.format(username, password), exp, mod)
