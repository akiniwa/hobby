#! coding: utf-8
'''kafka-python usage'''

KAFKA_SERVER = '192.168.0.108:9092'


def simple_producer():
    '''simple producer'''
    from kafka import SimpleProducer, KafkaClient

    # To send messages synchronously
    kafka = KafkaClient(KAFKA_SERVER)
    producer = SimpleProducer(kafka)

    # Note that the application is responsible for encoding messages to type bytes
    producer.send_messages('topic', b'some message')
    producer.send_messages('topic', b'this method', b'is variadic')
    # Send unicode message
    producer.send_messages('topic', u'你怎么样?'.encode('utf-8'))

if __name__ == '__main__':
    simple_producer()