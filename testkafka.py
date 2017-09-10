#coding=utf-8
from pykafka import KafkaClient
from pykafka import rdkafka
from pykafka import exceptions
from pykafka import simpleconsumer
import time
client = KafkaClient(hosts="1.1.1.1:9092")

# print client.topics
topic=client.topics['test']
print topic
import logging as log
# log.basicConfig(level=log.DEBUG)
'''
# with open('./tmp_1040W.txt','r') as file:
    tmp = file.readlines()
starttime =  time.time()
producer = topic.get_producer(use_rdkafka=True,max_request_size=100000000,
                              max_queued_messages=10000000,
                              max_retries=5,
                              )

num=0

for i in tmp[:30000]:
    num += 1

    # print i.strip('\n')
    producer.produce(i.strip('\n'))
producer.stop()
'''
consumer = topic.get_simple_consumer(
    consumer_group='test1',
    auto_commit_enable=True,
    auto_commit_interval_ms=1,
)

for message in consumer:
    print message
    if message is not None:
        print message.offset, message.value
        print type(message.value)

print topic.latest_available_offsets()

print time.time()-starttime
