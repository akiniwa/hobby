# -*- coding: utf-8 -*-

import os
from PIL import Image

working_dir = r'D:\pic\160817.bdp'
temping_dir = r'D:\pic\zzzz'

for f in os.listdir(working_dir):
    pic = os.path.join(working_dir, f)
    img = Image.open(pic)
    print img.size
    width, height = img.size
    left, top = 0, 65
    box = (left, top, left + width, top + height)
    area = img.crop(box)
    pic_new = os.path.join(temping_dir, f)
    area.save(pic_new)
    # break
