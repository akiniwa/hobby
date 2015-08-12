
mp3_file = "Ender's Game mp3\\00.01 - Earth Unaware\\00.01 - Earth Unaware Part1.mp3"

# ###########################
def cut_mp3(fn, sec, total):
	import pymp3cut
	
	argv = ['pymp3cut', '-q', '-p', '%s,%s,%s' % (fn.split('.')[0], sec, total), fn]
	pymp3cut.mp3cut(argv)

# cut_mp3(fn='EarthUnawareP1.mp3', sec=1000, total='16:00:00')
# cut_mp3(fn='EarthUnawareP2.mp3', sec=1000, total='16:00:00')

# cut_mp3(fn='EarthAfireP1.mp3', sec=1000, total='16:00:00')
# cut_mp3(fn='EarthAfireP2.mp3', sec=1000, total='16:00:00')

# ###########################
def print_tag():
	import os
	import pmpcmp3
	import string
	import sys

	# argv = ['pmpcmp3', '--cat']
	argv = ['pmpcmp3']

	for i in range(1, 24):
		argv.append('EarthUnawareP1-%s.mp3' % string.zfill(i, 4))
	
	pmpcmp3.main(argv, sys.stdout, os.environ)

# print_tag()


# ###########################
def delete_id3(fn):
	from mutagen.id3 import ID3
	audio = ID3(fn)
	audio.delete()

# delete_id3()

def create_id3(fn):
	from mutagen.id3 import ID3
	audio = ID3(fn)
	audio.save()

# ###########################
def tag_mp3(prfix, end, tag):
	import eyed3
	import string
	for i in range(1, end + 1):
		fn = '%s-%s.mp3' % (prfix, string.zfill(i, 4))
		print fn
		audio = eyed3.load(fn)
		audio.tag.artist = tag['artist']
		audio.tag.album = tag['album']
		audio.tag.album_artist = tag['album_artist']
		audio.tag.genre = tag['genre']
		audio.tag.title = tag['title'] % string.zfill(i, 2)
		audio.tag.track_num = i
		audio.tag.save()

tag = {
	'artist': u'Orson Scott Card',
	'album': u'Earth Afire One',
	'album_artist': u'Orson Scott Card and Aaron Johnston',
	'genre': u'Audiobook',
	'title': u'Earth Afire One - %s'
}
tag_mp3(prfix='EarthAfireP1', end=29, tag=tag)

tag = {
	'artist': u'Orson Scott Card',
	'album': u'Earth Afire Two',
	'album_artist': u'Orson Scott Card and Aaron Johnston',
	'genre': u'Audiobook',
	'title': u'Earth Afire Two - %s'
}
tag_mp3(prfix='EarthAfireP2', end=27, tag=tag)


# ###########################
def mp3_length():
	from mutagen.mp3 import MP3
	audio = MP3(mp3_file)
	print audio.info.length, audio.info.bitrate
	print dir(audio.info)

# mp3_length()


# ###########################
def easyid3_keys():
	from mutagen.easyid3 import EasyID3
	print EasyID3.valid_keys.keys()


# easyid3_keys()


# ###########################
def mutagen_file():
	import mutagen
	audio = mutagen.File('..\EarthAfireP1.mp3', easy=True)
	# audio = mutagen.File(mp3_file, easy=True)
	print audio.pprint()

# mutagen_file()


# ###########################
def guess_mimetype():
	from eyed3.utils import guessMimetype

	mtype = guessMimetype('EarthAfireP1.mp3')
	print mtype
	mtype = guessMimetype(mp3_file)
	print mtype

# guess_mimetype()