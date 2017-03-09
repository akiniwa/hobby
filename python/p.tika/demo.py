# coding: utf-8

import inspect
doc = 'test.docx'
host = 'http://localhost:9998/tika'


def print_stars():
    """print_stars"""
    print('*' * 50)
    print(inspect.stack()[1][3])


def test_parser():
    """test_parser"""
    from tika import parser
    print_stars()
    parsed = parser.from_file(doc, host)
    # parsed = parser.from_file('test.png', host)
    print(parsed['metadata'])
    print(parsed['content'])


def test_detect():
    """test_detect"""
    from tika import detector
    print_stars()
    print(detector.from_file(doc))


def test_config():
    """test_config"""
    from tika import config
    print_stars()
    print(config.getParsers())
    print(config.getMimeTypes())
    print(config.getDetectors())


def test_language():
    """test_language"""
    from tika import language
    print_stars()
    print(language.from_file(doc))


if __name__ == '__main__':
    test_config()
    test_detect()
    test_language()
    test_parser()
