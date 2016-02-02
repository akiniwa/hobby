#! coding: utf-8
"""baidu map api"""

import hashlib
import json
import urllib
import urllib2

SAFE = "/:=&?#+!$,;'@()*[]"
API_ADDRESS = '/geocoder/v2/?output=json&ak={0}&address={1}'
API_LOCATION = '/geocoder/v2/?output=json&ak={0}&pois=0&location={1}'
AK = 'SGp4w5XOv8UGmuWbuVwZKk3g'
SK = '1nFEN6KfRc7nySZMVCMf6xVvhYRuniQo'

ADDRESSES = [
    '北京市',
    '上海市',
    '广州市',
    '深圳市',
    '武汉市',
    '南京市',
    '天津市',
    '成都市',
    '宁波市',
    '西安市',
    '重庆市',
    '廊坊市'
]

LOCATIONS = [
    '39.9299857781,116.395645038',
    '31.24916171,121.487899486',
    '23.1200491021,113.307649675',
    '22.5460535462,114.025973657',
    '30.5810841269,114.316200103',
    '32.0572355018,118.778074408',
    '39.1439299033,117.210813092',
    '30.6799428454,104.067923463',
    '29.8852589659,121.579005973',
    '34.2777998978,108.953098279',
    '29.5446061089,106.530635013',
    '39.5186106251,116.703602223'
]


def to_address(location):
    """
    to_address
    http://api.map.baidu.com/geocoder/v2/
    ?ak=E4805d16520de693a3fe707cdc962045
    &callback=renderReverse
    &location=39.983424,116.322987
    &output=json
    &pois=1
    """
    url = parse_url(location, api='location')
    return call_api(url)


def to_location(address):
    """
    to_location
    http://api.map.baidu.com/geocoder/v2/
    ?ak=E4805d16520de693a3fe707cdc962045
    &address=百度大厦
    &callback=renderOption
    &city=北京市
    &output=json
    """
    url = parse_url(address, api='address')
    return call_api(url)


def parse_url(para='', api='address'):
    '''print url'''
    querystr = API_ADDRESS if 'address' == api else API_LOCATION
    encoded = urllib.quote(querystr.format(AK, para), safe=SAFE)
    sn = hashlib.md5(urllib.quote_plus(encoded + SK)).hexdigest()
    url = 'http://api.map.baidu.com{0}&sn={1}'
    return url.format(encoded, sn)


def call_api(url):
    """call_api"""
    response = urllib2.urlopen(url)
    return response.read()


def parse_address(json_str):
    """parse_address"""
    json_decode = json.loads(json_str)
    addr = json_decode['result']['addressComponent']
    # return (addr['province'], addr['city'])
    return (addr['province'].encode('utf-8'), addr['city'].encode('utf-8'))


def parse_location(json_str):
    """parse_location"""
    json_decode = json.loads(json_str)
    location = json_decode['result']['location']
    return (location['lat'], location['lng'])


def get_locations():
    """get_locations"""
    for address in ADDRESSES:
        json_str = to_location(address)
        (lat, lng) = parse_location(json_str)
        # print '{0},{1}'.format(lat, lng)
        print '{0}\t{1}\t{2}'.format(address, lat, lng)


def get_addresses():
    """get_addresses"""
    for location in LOCATIONS:
        json_str = to_address(location)
        # print location
        (province, city) = parse_address(json_str)
        print '{0}\t{1}\t{2}'.format(location, province, city)

# get_locations()
get_addresses()
