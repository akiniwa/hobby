#! coding: utf-8
"""
datascience
===========

submodules:

- algebra
- bayes
- clustering
- data
- database
- decision
- gradient
- hypothesis
- knn
- mapreduce
- ml
- network
- neural
- nlp
- probability
- recommender
- regression
- statistics
- viz

"""

from __future__ import absolute_import

from .algebra import (vector_add, vector_substract, vector_sum,
                      scalar_multiply, vector_mean, dot, sum_of_squares,
                      magnitude, squared_distance, distance, shape,
                      get_row, get_column, make_matirx, is_diagonal)

from .bayes import (NaiveBayesClassifier, count_words,
                    spam_probability, tokenize, word_probabilities)

from .clustering import (KMeans, choosing_k, squared_clustering_errors)

# from datascience import *
__ALL__ = [
    'algebra',
    'bayes',
    'clustering',
    'data',
    'database',
    'decision',
    'gradient',
    'hypothesis',
    'knn',
    'mapreduce',
    'ml',
    'network',
    'neural',
    'nlp',
    'probability',
    'recommender',
    'regression',
    'statistics',
    'viz',
]
