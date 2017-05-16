#! coding: utf-8
'''kafka-python usage'''

KAFKA_SERVER = '192.168.0.108:9092'


def kafka_consumer():
    '''kafka consumer'''
    from kafka import KafkaConsumer

    # To consume messages
    consumer = KafkaConsumer('glances',
                             # group_id='my-group',
                             bootstrap_servers=[KAFKA_SERVER])
    for message in consumer:
        # message value is raw byte string -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))


if __name__ == '__main__':
    kafka_consumer()
