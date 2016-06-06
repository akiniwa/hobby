#! coding: utf-8
"""producer for rabbitmq"""

import pika

credentials = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('192.168.99.100',
                                        credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange='hello-exchange',
                         type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)

msgs = [
    'hello',
    'world',
    'form',
    'rabbitmq',
    'quit',
    ]


def msg_producer():
    """msg_procuder"""
    for msg in msgs:
        print msg
        msg_prop = pika.BasicProperties()
        msg_prop.content_type = 'text/plain'

        channel.basic_publish(body=msg,
                              exchange='hello-exchange',
                              properties=msg_prop,
                              routing_key='hola')

msg_producer()
