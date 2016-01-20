#! coding: utf-8
'''rename ebooks'''

import glob
import os
import shutil


def rename_ebooks(path):
    '''rename_ebooks'''
    for fullname in glob.glob(r'{}*.pdf'.format(path)):
        (_, filename) = os.path.split(fullname)
        filename = filename \
                .replace(',', '.') \
                .replace('-', '.') \
                .replace('_', '.') \
                .replace(' ', '.') \
                .lower()
        newname = os.path.join(path, filename)
        if fullname != newname:
            print filename
            shutil.move(fullname, newname)

rename_ebooks('/Users/hqlgree2/Downloads/')
