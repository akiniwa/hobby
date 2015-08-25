
"""natural language processing"""
from __future__ import division
from nltk.book import *
from nltk.probability import FreqDist

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

fun10()
