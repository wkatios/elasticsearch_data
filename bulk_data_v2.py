#coding: utf-8
"""
{'test':'123'}

"""

import time
from elasticsearch import Elasticsearch
from elasticsearch import helpers


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

es = Elasticsearch("1.1.1.1")
esindex_prefix = "index"
data_type = 'tcp'

try:
    data_type = sys.argv[1].strip()
except:
    pass
# indexes = ['dport', 'l4proto', 'ip_traffic','http_ack','sip_out','sip_in']
# indexes = ['tcp', 'dns']
# for i in indexes:
#     es.indices.create(index="%s-%s" % (esindex_prefix, i), ignore=400)

values = []
threshold = 99
totallines = open('./%s.data.json' % data_type).readlines()
total = len(totallines)
import random


while True:
    rand_flag = random.randint(1, total)
    lines = totallines[rand_flag:rand_flag+200]
    for msg in lines:
        value = msg.replace("\n", "").replace("\t", "")
        # print value
        value = value.replace(' false,', ' False,')
        value = value.replace(' true,',' True,')
        valuedic = eval(value)
        valuedic['@timestamp'] = time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
        esindex = "%s-%s"%(esindex_prefix,time.strftime('%Y.%m.%d'))
        values.append({
            "_index": esindex,
            "_type": data_type,
            "_source": valuedic
        })
        # sys.stdout.flush()

        if len(values) > threshold:
            helpers.bulk(es,values)
            values=[]
            time.sleep(2)
