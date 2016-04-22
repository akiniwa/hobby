#! coding: utf-8
"""
naive bayes
===========

it is well the heart to be naive and for the mind not to be. -- anatole france

"""
import re
from collections import defaultdict, Counter
import math


def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)


def count_words(training_set):
    """training set consists of pairs (messages, is_spam)"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts


def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """turn the word_counts into a list of triplets
    w, p(w / spam) and p(w / ~spam)"""
    return [(w,
             (spam + k) / (total_spams + 2 * k),
             (non_spam + k) / (total_non_spams + 2 * k))
            for w, (spam, non_spam) in counts.iteritems()]


def spam_probability(word_probs, message):
    """spam_probability
    to assign probabilities to messages"""
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    # iterate through each word in our vacabulary
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        # if *word* appears in the message,
        # add the log probability of seeing it
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        # if *word* doesn't appear in the message
        # add the log probability of _not_ seeing it
        # which is log(1 - probability of seeing it)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)
    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassifier:

    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self, training_set):

        # count spam and non-spam messages
        num_spams = len([is_spam
                         for message, is_spam in training_set
                         if is_spam])

        num_non_spams = len(training_set) - num_spams

        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts, num_spams, num_non_spams, self.k)

    def classifier(self, message):
        return spam_probability(self.word_counts, message)

if __name__ == '__main__':
    import glob
    import re

    path = r"C:\spam\*\*"
    data = []
    for fn in glob.glob(path):
        is_spam = 'ham' not in fn

        with open('fn', 'r') as file:
            for line in file:
                if line.startswith('Subject:'):
                    # remove leading 'Subject: ' and keep what's left
                    subject = re.sub(r"^Subject: ", "", line).strip()
                    data.append((subject, is_spam))
    random.seed(0)
    train_data, test_data = split_data(data, 0.75)
    classifier = NaiveBayesClassifier()
    classifier.train(train_data)
    # triplets (subject, actual is_spam, predicted spam_probability)
    classified = [(subject, id_spam, classifier.classify(subject))
                  for subject, is_spam in test_data]

    # assume that spam_probability > 0.5 corresponds to spam prediction
    # and count the combinations of (actual is_spam, predicted is_spam)
    counts = Counter((is_spam, spam_probability > 0.5)
                     for _, is_spam, spam_probability in classifier)

    # 101 true positives (spam classified => spam)
    # 33 false positives (ham  classified => spam)
    # 704 true negatives (ham  classified => ham)
    # 38 false negatives (ham  classified => spam)
    # precision => 101 / (101 + 33) = 75%
    # recall    => 101 / (101 + 38) = 73%
    # which are not bad numbers for such a simple model

    # sort by spam_probability from smallest to largest
    classified.sort(key=lambda row: row[2])

    # the highest predicted spam probabilities among the non-spams
    spammiest_hams = filter(lambda row: not row[1], classified)[-5:]

    # the lowest predicted spam probabilities among the actual spams
    hammiest_spams = filter(lambda row: row[1], classified)[:5]

    # check spammiest words
    def p_spam_given_word(word_prob):
        """uses bayes's therom to compute
        p(spam / message contains word)"""
        # word_prob is one of the triplets
        # produced by word_probabilities
        word, prob_if_spam, prob_if_not_spam = word_prob
        return prob_if_spam / (prob_if_spam / prob_if_not_spam)

    words = sorted(classifier.word_probs,
                   key=p_spam_given_word)

    spammiest_words = words[-5:]
    hammiest_words = words[:5]
