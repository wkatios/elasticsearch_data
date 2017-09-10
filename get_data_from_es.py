#!/usr/bin/python
# coding:utf-8


import json
import os
import sys
import time
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
"""
注意： 导出数据许多时候会有上限的限制

Result window is too large, from + size must be less than or equal to: [10000] but was [20000].
See the scroll api for a more efficient way to request large data sets.
This limit can be set by changing the [index.max_result_window] index level setting.

解决方法： see http://blog.csdn.net/qq_18145031/article/details/53489370

PUT _settings
{
    "index": {
        "max_result_window": "10000000"
    }
}

更好的办法，是用scroll ，但是这个需要大改代码




"""

class exportEsData():
    size = 10000

    def __init__(self, url, index, type, target_index):
        self.url = url + "/" + index + "/" + type + "/_search"
        self.index = index
        self.type = type
        self.target_index = target_index  # 替换原有的index
        self.file_name = self.target_index + "_" + self.type + ".json"

    def exportData(self):
        print("export data begin...\n")
        begin = time.time()
        try:
            os.remove(self.file_name)
        except:
            # os.mknod(self.file_name)
            pass
        # print self.url
        msg = urllib2.urlopen(self.url).read()
        # print(msg)
        obj = json.loads(msg)
        num = obj["hits"]["total"]
        start = 0
        end = num / self.size + 1
        print end
        # end = 10
        while (start < end):
            tmpurl = self.url + "?from=" + str(start * self.size) + "&size=" + str(self.size)
            print tmpurl
            msg = urllib2.urlopen(tmpurl).read()
            time.sleep(1)
            self.writeFile(msg)
            start = start + 1
        print("export data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

    def export_single_field(self):
        print("export single field data begin...\n")
        begin = time.time()
        try:
            os.remove(self.file_name)
        except:
            # os.mknod(self.file_name)
            pass
        # print self.url
        msg = urllib2.urlopen(self.url).read().decode('utf-8')
        # print(msg)
        obj = json.loads(msg)
        num = obj["hits"]["total"]
        print num
        start = 0
        end = num / self.size + 1
        # end = 10
        print end
        tmp = []
        while (start < end):
            print start
            tmpurl = self.url + "?from=" + str(start *self.size) + "&size=" + str(self.size)
            print tmpurl
            msg = urllib2.urlopen(tmpurl).read().decode('utf-8')
            time.sleep(1)
            msgs = json.loads(msg)
            msgs = msgs['hits']['hits']
            for msg in msgs:
                # print msg
                # break
                msg=msg['_source']['udpinput']['log_raw']
                # print m[
                #print msg.split('\n')[0]
                tmp.append(msg.split('\n')[0])
            # self.writeFile("\n".join(tmp))
        #
            start = start + 1
            if start%5==0:
                print start
                #open('./log_sample.txt','a+').write("\n".join(tmp))
                #tmp=[]
        #print tmp
        #open('./log_sample.txt','w').write("\n".join(tmp))
        open('./log_sample.txt','w').write("\n".join(tmp))
        print("export data end!!!\n total consuming time:" + str(time.time() - begin) + "s")


    def writeFile(self, msg):
        obj = json.loads(msg)
        vals = obj["hits"]["hits"]
        try:
            f = open(self.file_name, "a")
            for val in vals:
                # prepare for bulk insert，注意格式
                meta_json = {"index": {"_index": self.target_index, "_type": val["_type"], "_id": val["_id"]}}
                val_json = val["_source"]
                # m = json.dumps(meta_json, ensure_ascii=False)
                v = json.dumps(val_json, ensure_ascii=False)
                # f.write(m + "\n")
                f.write(v + "\n")
        finally:
            f.flush()
            f.close()


class importEsData():
    def __init__(self, url, index, type):
        self.url = url
        self.index = index
        self.type = type
        self.file_name = self.index + "_" + self.type + ".json"

    def importData(self):
        print("import data begin...\n")
        begin = time.time()
        try:
            s = os.path.getsize(self.file_name)
            f = open(self.file_name, "r")
            data = f.read(s)
            # 此处有坑: 注意bulk操作需要的格式(以\n换行)
            self.post(data)

        finally:
            f.close()
        print("import data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

    def post(self, data):
        print data
        print self.url
        req = urllib2.Request(self.url, data)
        r = urllib2.urlopen(req)
        response = r.read()
        print response
        r.close()


if __name__ == '__main__':
    '''
        Export Data
        e.g.
                            URL                    index        type
        exportEsData("http://1.1.1.1:9200","watchdog","mexception").exportData()

        export file name: watchdog_mexception.json
    '''
    # exportEsData("http://1.1.1.1:9200","watchdog","mexception").exportData()
    try:
        #server = sys.argv[1].strip()
        #topic = sys.argv[2].strip()
        #index = sys.argv[3].strip() # sample cc-iprobe-4a859fff6e5c4521aab187eee1cfceb8-2017.08.09
        # exportEsData("http://%s:9200"%server, index, topic, topic).exportData()
        exportEsData("http://1.1.1.1:9200", "index", "topic","topic").export_single_field()
    except:
        print "usage: get_data_from_es.py <ES_Server> <TOPIC> <Index>"
    # exportEsData("http://127.0.0.1:9200", "forum", "TOPIC", "chat").exportData()

    '''
        Import Data
        *import file name:watchdog_test.json    (important)
                    "_" front part represents the elasticsearch index
                    "_" after part represents the  elasticsearch type
        e.g.
                            URL                    index        type
        mportEsData("http://1.1.1.1:9200","watchdog","test").importData()
    '''
    # importEsData("http://10.100.142.60:9200","watchdog","test").importData()
    # importEsData("http://127.0.0.1:9200/_bulk", "chat", "CHAT").importData()
    # importEsData("http://127.0.0.1:9200/_bulk", "chat", "TOPIC").importData()
