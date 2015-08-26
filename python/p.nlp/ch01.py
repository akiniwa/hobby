
"""natural language processing"""
from __future__ import division
from nltk.book import *
from nltk.probability import FreqDist
from nltk.util import bigrams

def fun01():
    """print text"""
    print text1
    print text2

def fun02():
    """concordance"""
    print text1.concordance("monstrous")

def fun03():
    """similar"""
    print text1.similar("monstrous")
    print text2.similar("monstrous")

def fun04():
    """common context"""
    print text2.common_contexts(["monstrous", "very"])

def fun05():
    """dispersion plot"""
    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

def fun06():
    """generate text"""
    # print text3.generate()
    print len(text3), len(set(text3))
    print text3.count("smote")

def lexical_diversity(text):
    """lexical_diversity"""
    return len(text) / len(set(text))

def percentage(count, total):
    """percentage"""
    return 100 * count / total

def fun07():
    """fun7"""
    print lexical_diversity(text3)
    print lexical_diversity(text5)
    print percentage(text4.count("a"), len(text4))

def fun08():
    """fun8"""
    print sent1
    print sent2
    print sent3
    print sent1 + sent2 + sent3

def fun09():
    """index"""
    print text4[173]
    print text4.index("awaken")
    # slicing
    print text5[16715:16735]

def fun10():
    """frequency distribution"""
    fdist1 = FreqDist(text1)
    # print fdist1
    vocabulary1 = fdist1.keys()
    # print vocabulary1[:50]
    fdist1.plot(50, cumulative=True)

def fun11():
    """selection of words"""
    V = set(text1)
    long_words = [word for word in V if len(word) > 15]
    print sorted(long_words)

def fun12():
    """words longer than 7 chars and occur more than 7 times"""
    fdist1 = FreqDist(text5)
    print sorted([w for w in set(text5) if len(w) > 7 and fdist1[w] > 7])

def fun13():
    """collocations and bigrams"""
    print list(bigrams(['more', 'is', 'said', 'than', 'done']))
    print text4.collocations()
    print text8.collocations()

def fun14():
    """counting other things"""
    # print [len(w) for w in text1]
    fdist1 = FreqDist([len(w) for w in text1])
    # print fdist1.keys()
    # print fdist1.items()
    # word length 3 => 50223
    print fdist1[3]
    print fdist1.max()
    # frequency 20%
    print fdist1.freq(3)

def fun15():
    """operating on every element"""
    # print [w.upper() for w in text1]
    print len(set(text1))
    print len(set([word.lower() for word in text1]))
    print len(set([word.lower() for word in text1 if word.isalpha()]))

fun15()
