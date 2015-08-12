#! -*- coding: utf-8 -*-
import os, sys
import Image

ppm_dir = "image/ppm/"
jpf_dir = "image/jpg/"

def ppm2jpg():
	ppms = os.listdir(ppm_dir)
	count = len(ppms)
	for ppm in ppms:
		(name, ext) = os.path.splitext(ppm)
		if ".ppm" != ext:
			continue
		try:
			im = Image.open(ppm_dir + ppm)
			im.save(jpf_dir + name + ".jpg")
			print "ok - " + str(count).rjust(3, '0') + ppm
		except IOError:
			print "no - " + str(count).rjust(3, '0') + ppm
		count -= 1

ppm2jpg()