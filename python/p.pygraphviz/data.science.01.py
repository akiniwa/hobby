#! coding: utf-8

from __future__ import division
import pygraphviz as pgv

users = [
    {'id': 0, 'name': 'hero'},
    {'id': 1, 'name': 'dunn'},
    {'id': 2, 'name': 'sue'},
    {'id': 3, 'name': 'chi'},
    {'id': 4, 'name': 'thor'},
    {'id': 5, 'name': 'clive'},
    {'id': 6, 'name': 'hicks'},
    {'id': 7, 'name': 'devin'},
    {'id': 8, 'name': 'kate'},
    {'id': 9, 'name': 'klein'},
]

friendships = [
    (0, 1), (0, 2),
    (1, 2), (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6), (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]


for user in users:
    user['friends'] = []

for i, j in friendships:
    users[i]['friends'].append(users[j])
    users[j]['friends'].append(users[i])


def number_of_friends(user):
    """number_of_friends"""
    return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connnections = total_connections / num_users
print total_connections, avg_connnections

num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

sorted(num_friends_by_id,
       key=lambda (user_id, num_friends): num_friends,
       reverse=True)


def save_to(fmt):
    """save_to"""
    G = pgv.AGraph(directed=False)
    for friendship in friendships:
        G.add_edge(*friendship)
    G.layout(prog='dot')
    G.draw('data.science.01.{}'.format(fmt))


def friends_of_friend_ids_bad(user):
    """friends_of_friend_ids_bad"""
    return [foad['id']
            for friend in user['friends']
            for foad in friend['friends']]

save_to('png')
save_to('dot')
# [0, 2, 3, 0, 1, 3]
# include 0, 3 twice
# print friends_of_friend_ids_bad(users[0])

# print [friend['id'] for friend in users[0]['friends']]
# print [friend['id'] for friend in users[1]['friends']]
# print [friend['id'] for friend in users[2]['friends']]
