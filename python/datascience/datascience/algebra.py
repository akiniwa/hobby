#! coding: utf-8
"""
linear algebra
==============

is there anything more useless or less useful than algebra? -- billy connolly

"""

import math
from functools import partial


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_substract(v, w):
    """substracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


vector_sum = partial(reduce, vector_add)


def vector_sum(vectors):
    """vector_sum"""
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c is a number v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """compute the vector whose ith element
    is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    """magnitude"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_substract(v, w))


def distance(v, w):
    """distance"""
    return math.sqrt(squared_distance(v, w))


def distance(v, w):
    """distance"""
    return magnitude(vector_substract(v, w))


def shape(A):
    """shape of a matrix"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    """get_row i or matrix A"""
    return A[i]


def get_column(A, j):
    """get_column j of matrix A"""
    return [A_i[j] for A_i in A]


def make_matirx(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    """ 1's on the diagonal, 0's everywhere else"""
    return 1 if i == j else 0


if __name__ == '__main__':
    height_weight_age = [70,   # inches
                         170,  # pounds
                         40]    # years

    grades = [95,  # exam1
              80,  # exam2
              75,  # exam3
              60]   # exam4

    print vector_add([1, 2], [2, 1])

    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[1, 2],
         [3, 4],
         [5, 6]]

    print shape(A)
    print shape(B)

    identity_matrix = make_matirx(5, 5, is_diagonal)
    print identity_matrix

    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

    def is_friends(i, j):
        """(i, j) or (j, i) in friendships"""
        return 1 if (i, j) in friendships or (j, i) in friendships else 0

    friendships_matrix = make_matirx(10, 10, is_friends)
    print friendships_matrix
    print friendships_matrix[0][2] == 1
    print friendships_matrix[0][8] == 1
