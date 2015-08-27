#! coding: utf-8
"""ch02"""

import nltk
from nltk import Text
from nltk.corpus import gutenberg, webtext, nps_chat, brown, reuters, inaugural, udhr
from nltk.probability import FreqDist
# from nltk.book import *

def fun01():
    """fun01"""
    print gutenberg.fileids()
    # emma by jane austen
    emma = gutenberg.words('austen-emma.txt')
    # how many words it contains
    print len(emma)
    print Text(emma).concordance("surprize")

def fun02():
    """fun02"""
    for fileid in gutenberg.fileids():
        num_chars = len(gutenberg.raw(fileid))
        num_words = len(gutenberg.words(fileid))
        num_sents = len(gutenberg.sents(fileid))
        num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
        # average word length average sentence length
        print int(num_chars/num_words), int(num_words/num_sents),
        # number of times each vocabulary item appers in the text
        print int(num_words/num_vocab), fileid

def fun03():
    """fun03"""
    macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
    print macbeth_sentences[1037]
    longest_len = max([len(s) for s in macbeth_sentences])
    print [s for s in macbeth_sentences if len(s) == longest_len]

def fun04():
    """fun04"""
    for fileid in webtext.fileids():
        print fileid, webtext.raw(fileid)[:50]

def fun05():
    """fun05"""
    chatroom = nps_chat.posts("10-19-20s_706posts.xml")
    print chatroom[123]

def fun06():
    """fun06"""
    print brown.categories()
    print brown.words(categories='news')[:60]
    print brown.words(fileids=['cg22'])[:60]
    print brown.sents(categories=['news', 'editorial', 'reviews'])

def fun07():
    """fun07"""
    news_text = brown.words(categories='news')
    fdist = FreqDist([w.lower() for w in news_text])
    # modals = ['can', 'could', 'may', 'might', 'must', 'will']
    modals = ['who', 'when', 'where', 'what', 'why']
    for modal in modals:
        print modal + ':', fdist[modal],

def fun08():
    """fun08"""
    cfd = nltk.ConditionalFreqDist((genre, word) \
        for genre in brown.categories() \
        for word in brown.words(categories=genre))
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfd.tabulate(conditions=genres, samples=modals)

def fun09():
    """fun09"""
    print reuters.fileids()[:50]
    print reuters.categories()[:50]

def fun10():
    """fun10"""
    print reuters.categories('training/9865')
    print reuters.categories(['training/9865', 'training/9880'])
    print reuters.fileids('barley')[:50]
    print reuters.fileids(['barley', 'corn'])[:50]

def fun11():
    """inaugural address corpus"""
    print inaugural.fileids()
    print [fileid[:4] for fileid in inaugural.fileids()]

    cfd = nltk.ConditionalFreqDist((target, fileid[:4]) \
        for fileid in inaugural.fileids() \
        for w in inaugural.words(fileid) \
        for target in ['america', 'citizen'] \
        if w.lower().startswith(target))
    cfd.plot()

def fun12():
    """annotated text corpus"""
    # http://www.nltk.org/data
    # http://www.nltk.org/howto
    pass

def fun13():
    """corpora in other languages"""
    # print nltk.corpus.cess_esp.words()[:50]
    # print nltk.corpus.floresta.words()[:50]
    # print nltk.corpus.indian.words('hindi.pos')[:50]
    # print nltk.corpus.udhr.fileids()
    # print nltk.corpus.udhr.words('Javanese-Latin1')[11:50]
    for word in nltk.corpus.udhr.words('Chinese_Mandarin-GB2312'):
        print word.encode('utf-8'),

def fun14():
    """cfd plot"""
    languages = ['Chickasaw', 'English', 'German_Deutsch', \
        'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
    cfd = nltk.ConditionalFreqDist((lang, len(word)) \
        for lang in languages \
        for word in udhr.words(lang + '-Latin1'))
    cfd.plot(cumulative=True)

def fun15():
    """freq dist plot"""
    raw_text = udhr.raw('Chinese_Mandarin-GB2312')
    FreqDist(raw_text).plot()

fun15()
