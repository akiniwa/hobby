#! coding: utf-8
"""export jpg from pdf"""

import os
import Image

pdf_dir = 'D:\\ebooks\\data.store\\mq'
# img_dir = os.path.join(pdf_dir, 'images')
img_dir = os.path.join('D:\\pic', 'images')
command = 'C:\\xpdfbin-win-3.04\\bin64\\pdfimages.exe'


def pdf_to_ppm():
    """pdf_to_ppm"""
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    os.chdir(img_dir)
    for file in os.listdir(pdf_dir):
        if not file.endswith('.pdf'):
            continue
        full = os.path.join(pdf_dir, file)
        root = file.strip('.pdf')
        print 'process', file
        os.system('{} {} {}'.format(command, full, root))


def ppm_to_jpg():
    ppms = os.listdir(img_dir)
    for count, file in enumerate(ppms):
        (name, ext) = os.path.splitext(file)
        if not (file.endswith('.ppm') or file.endswith('pbm')):
            continue
        try:
            im = Image.open(os.path.join(img_dir, file))
            im.save(os.path.join(img_dir, name + '.png'))
            # print "ok -", str(count).rjust(3, '0'), file
        except IOError:
            print "no -", str(count).rjust(3, '0'), file


def ppm_cleanup():
    """ppm_cleanup"""
    print 'ppm cleanup'
    for file in os.listdir(img_dir):
        if not (file.endswith('.ppm') or file.endswith('.pbm')):
            continue
        os.remove(os.path.join(img_dir, file))


def pdf_to_jpg():
    """pdf_to_jpg"""
    pdf_to_ppm()
    ppm_to_jpg()
    ppm_cleanup()

if __name__ == '__main__':
    pdf_to_jpg()
