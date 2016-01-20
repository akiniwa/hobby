import magic

# blob = open('bm_aad045.csv').read()
# m = magic.open(magic.MAGIC_MIME_ENCODING)
# m.load()
# encoding = m.buffer(blob)

import magic

blob = open('bm_aad045.csv').read()
m = magic.Magic(mime_encoding=True)
encoding = m.from_buffer(blob)
print(encoding)


# source = open('bm_aad045.csv')
# target = open('bm_aad045_utf8.csv', "w")
# target.write(unicode(source.read(), encoding).encode("utf-8"))

# source = 'bm_aad045.csv'
# target = 'bm_aad045_utf8.csv'
# import codecs
# BLOCKSIZE = 1048576 # or some other, desired size in bytes
# with codecs.open(source, "r", encoding) as sourceFile:
#     with codecs.open(target, "w", "utf-8") as targetFile:
#         while True:
#             contents = sourceFile.read(BLOCKSIZE)
#             if not contents:
#                 break
#             targetFile.write(contents)