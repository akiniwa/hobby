#! coding: utf-8

import os
import json
import urllib
import urllib2
import StringIO
import cookielib
from bs4 import BeautifulSoup

# current script file path
path = os.path.split(os.path.realpath(__file__))[0]
# data folder
path = os.path.join(path, 'data')
if not os.path.exists(path):
    os.makedirs(path)

header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'www.ele.me',
    'Origin': 'https://www.ele.me',
    'Referer': 'https://www.ele.me/shop/725427',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
}


def print_line(char='-'):
    """print_line"""
    print char * 100


def post(url, data, header):
    """post"""
    request = urllib2.Request(url,
                              urllib.urlencode(data),
                              header)
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open(request)
    return response.read().strip()


def get(url, header):
    """get"""
    request = urllib2.Request(url)
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open(request)
    return response.read().strip()


def download(url, prefix, food_id):
    """download"""
    if '' == url or '' == str(food_id):
        return
    if '100.100' in url:
        url = url.replace('100.100', '800.800')
    if '100x100' in url:
        url = url.replace('100x100', '800x800')
    fileimage = '{}.{}.jpg'.format(prefix, food_id)
    fileimage = os.path.join(path, fileimage)
    if not os.path.exists(fileimage):
        urllib.urlretrieve(url, fileimage)


def get_eleme(shop=''):
    """get_eleme"""
    url = 'https://www.ele.me/restapi/shopping/v1/menu?restaurant_id={}'
    filename = 'eleme.{}.json'.format(shop)
    filename = os.path.join(path, filename)
    if os.path.exists(filename):
        return
    with open(filename, 'wt') as f:
        f.write(get(url.format(shop), header))


def parse_eleme(shop=''):
    """parse_eleme"""
    filename = 'eleme.{}.json'.format(shop)
    filename = os.path.join(path, filename)
    if not os.path.exists(filename):
        return
    with open(filename) as f:
        json_str = f.read()
    body = json.loads(json_str)
    for catalog in body:
        cata_id = catalog['id'] if 'id' in catalog else ''
        cata_name = catalog['name'] if 'name' in catalog else ''
        for food in catalog['foods']:
            rest_id = food['restaurant_id']
            food_icon = food['image_path'] if 'image_path' in food else ''
            food_icon = food_icon if food_icon else ''
            for specfood in food['specfoods']:
                food_id = specfood['food_id']
                food_name = specfood['name']
                food_price = specfood['price']
                print rest_id, cata_id, cata_name,
                print food_id, food_name, food_price, food_icon
                # download(food_icon, 'eleme', food_id)


def shop_eleme(shop=''):
    """shop_eleme"""
    get_eleme(shop=shop)
    parse_eleme(shop=shop)


def get_baidu(shop=''):
    """get_baidu"""
    url = 'http://waimai.baidu.com/waimai/shop/{}'
    filename = 'baidu.{}.html'.format(shop)
    filename = os.path.join(path, filename)
    if os.path.exists(filename):
        return
    with open(filename, 'wt') as f:
        f.write(get(url.format(shop), header))


def parse_baidu(shop=''):
    """parse_baidu"""
    filename = 'baidu.{}.html'.format(shop)
    filename = os.path.join(path, filename)
    if not os.path.exists(filename):
        return
    with open(filename) as f:
        bs = BeautifulSoup(f.read())

    scripts = bs.find_all('script')
    for script in scripts:
        if 'waimai:widget/menu/basicinfo/basicinfo.js' in script.text:
            for line in script.text.split('\n'):
                if 'waimai:widget/menu/basicinfo/basicinfo.js' in line:
                    json_str = line[line.index('init(')+len('init('):-3]
    # print json.dumps(json.loads(json_str), indent=4)
    json_dat = json.loads(json_str)
    for takeout_menu in json_dat['takeout_menu']:
        # print json.dumps(takeout_menu, indent=4)
        cata_id = takeout_menu['category_id'] if 'category_id' in takeout_menu else '---'
        cata_name = takeout_menu['catalog'] if 'catalog' in takeout_menu else '---'
        items = takeout_menu['data']
        for item in items:
            food_id = item['item_id']
            food_name = item['name']
            food_icon = item['url']
            food_desc = item['description']
            if 0 < len(item['dish_activity']):
                food_price = item['dish_activity']['price']
            else:
                food_price = 0
            print cata_id, cata_name,
            print food_id, food_name, food_price, food_icon, food_desc
            download(food_icon, 'baidu', food_id)


def shop_baidu(shop=''):
    """shop_baidu"""
    get_baidu(shop=shop)
    parse_baidu(shop=shop)


def get_meituan(shop=''):
    """get_meituan"""
    url = 'http://i.waimai.meituan.com/restaurant/{}'
    filename = 'meituan.{}.html'.format(shop)
    filename = os.path.join(path, filename)
    if os.path.exists(filename):
        return
    with open(filename, 'wt') as f:
        f.write(get(url.format(shop), header))


def parse_meituan(shop=''):
    """parse_meituan"""
    filename = 'meituan.{}.html'.format(shop)
    filename = os.path.join(path, filename)
    if not os.path.exists(filename):
        return
    with open(filename) as f:
        bs = BeautifulSoup(f.read())

    divs = bs.find_all('div', class_='j-foodlist foodlist')
    for div in divs:
        cata_id = div.get('data-tagid')
        h3 = div.find('h3', class_='foodlist-label')
        cata_name = h3.text.encode('utf-8')
        lis = div.find_all('li', class_='j-fooditem')
        for li in lis:
            food_id = li.get('data-spuid')
            food_name = li.get('data-foodname')
            food_price = li.get('data-price')
            if li.find('img'):
                food_icon = li.find('img').get('data-src-retina')
            else:
                food_icon = ''
            # food_pack = li.get('data-pack')
            # food_stock = li.get('data-stock')
            print cata_id, cata_name,
            print food_id, food_name, food_price, food_icon
            download(food_icon, 'meituan', food_id)


def shop_meituan(shop=''):
    """shop_meituan"""
    get_meituan(shop=shop)
    parse_meituan(shop=shop)


if __name__ == '__main__':
    # shop_eleme(shop='725427')
    shop_meituan(shop='183419')
    # shop_baidu(shop='6909305013796471251')
