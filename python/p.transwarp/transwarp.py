#! coding: utf-8

import os
import urllib
from bs4 import BeautifulSoup

url_home = 'http://www.transwarp.cn'
url_download = 'http://www.transwarp.cn/about/download'


def read_download_page():
    """read_download_page"""
    respose = urllib.urlopen(url_download)
    return respose.read()


def get_urls_div():
    """get_urls_div"""
    soup = BeautifulSoup(read_download_page())
    urls = []
    for div in soup.find_all('div', class_='download_item'):
        fn = os.path.split(div.a['href'])[-1]
        fext = os.path.splitext(fn)[1]
        name = div.span.string
        fn = fn if name in fn else name + fext
        urls.append((fn.encode('utf-8'), div.a['href'].encode('utf-8')))
    return urls


def get_urls_a():
    """get_urls_a"""
    soup = BeautifulSoup(read_download_page())
    # <a href="/pdf/product_technology/v4_3/some.pdf" class="fr">...</a>
    return [(os.path.split(a['href'])[-1].encode('utf-8'),
             a['href'].encode('utf-8'))
            for a in soup.find_all('a', class_='fr')]


def main():
    """main"""
    # for cnt, (text, url) in enumerate(get_urls_div()):
    #     fn = os.path.join('data/div', text.decode('utf-8'))
    #     print 'saving', cnt, text
    #     # if not os.path.exists(fn):
    #     #     urllib.urlretrieve(url_home + url, fn)

    for cnt, (text, url) in enumerate(get_urls_a()):
        fn = os.path.split(url)[-1].decode('utf-8')
        fn = os.path.join('data/a', fn)
        print 'saving', cnt, fn
        if not os.path.exists(fn):
            urllib.urlretrieve(url_home + url, fn)

if __name__ == '__main__':
    main()
