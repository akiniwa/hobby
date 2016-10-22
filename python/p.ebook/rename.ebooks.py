#! coding: utf-8
'''rename ebooks'''

import glob
import os
import shutil


def rename_ebooks(path):
    '''rename_ebooks'''
    for fullname in glob.glob(os.path.join(path, '*.pdf')):
        (_, filename) = os.path.split(fullname)
        newname = filename     \
            .replace(',', '.') \
            .replace('-', '.') \
            .replace('_', '.') \
            .replace(' ', '.') \
            .replace('..', '.') \
            .lower()
        if fullname != newname:
            newname = os.path.join(path, newname)
            print newname
            shutil.move(fullname, newname)

rename_ebooks(r'C:/Users/Administrator/Downloads')
# rename_ebooks(r'/home/gree2/Downloads/')
# rename_ebooks(r'/Users/hqlgree2/Downloads/')
