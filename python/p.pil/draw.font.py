#! coding: utf-8

import Image
import ImageDraw
import ImageFont


def draw_something(fname, drawType, outpic):
    img = Image.open(fname)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    if drawType == "crossline":
        draw.line(((0, 0), (width-1, height-1)), fill=255)
        draw.line(((0, height-1), (width-1, 0)), fill=255)
        print "draw line"
    elif drawType == "arc":
        draw.arc((0, 0, width-1, height-1), 180, 270, fill=255)
        print "draw arc"

    img.save(outpic)


def draw_font(cnt, txt):
    font = ImageFont.truetype(r"C:\WINDOWS\Fonts\msyh.ttf", 40)
    # font = ImageFont.truetype(r"C:\WINDOWS\Fonts\SIMYOU.TTF", 40)
    img = Image.new("RGB", (400, 300))
    draw = ImageDraw.Draw(img)
    draw.ink = 0 + 255*256 + 0*255*256
    # draw.text((20, 120), unicode(txt, 'gbk'), font=font)
    draw.text((20, 120), txt, font=font)
    img.save("img{}.jpg".format(cnt))


if __name__ == '__main__':
    # img.show()
    # newimg = img.resize((300, 250), Image.BILINEAR)
    # newimg.save("a1_bmp.bmp")
    # rotimg = newimg.rotate(45)
    # rotimg.save("a1_new.jpg")
    # draw_something("a1.jpg", "crossline", "cross_line.jpg")
    # draw_something("a1.jpg", "arc", "arc.jpg")
    for cnt, txt in zip(range(4), u'三十而立'):
        draw_font(cnt, txt)
