# encoding: utf-8

import os
from wand.api import library
import wand.color
import wand.image

base_dir = '/Users/gree2/Downloads/glyph-iconset-master/svg/'
file_n = 'si-glyph-abacus.svg'
file_i = os.path.join(base_dir, file_n)
file_o = os.path.join(base_dir, file_i.replace('.svg', '.png'))

with wand.image.Image() as image:
    with wand.color.Color('transparent') as background_color:
        library.MagickSetBackgroundColor(image.wand, background_color.resource)
    with open(file_i) as svg_file:
        image.read(filename=file_i)
        # image.read(blob=svg_file.read(), format="svg")
        image.resize(1024, 1024)
        png_image = image.make_blob("png32")
    with open(file_o, "wb") as out:
        out.write(png_image)
