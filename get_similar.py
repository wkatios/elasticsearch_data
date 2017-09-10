#coding=utf-8
# from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""
给出字典文件
给出待比较目标（多行）
对于每一行，遍历得到相似度值(tfidf?)，得到最大值，以及对应的样本行号
"""

import re
import json
nums = range(10)
class MyCorpus(object):
    def __iter__(self):
        # for line in open('./unique.txt'):   # 样本库
        for aline in open(u'./unique_regex.txt'):   # 样本库
            # print aline
            a=eval(aline)
            line=a[0]
            # print type(eval(line))
            for i in nums:
                line = line.replace(str(i),'')
            yield line.split()

from gensim import corpora, models, similarities
Corp = MyCorpus()
unique_dict = corpora.Dictionary(Corp)
corpus = [unique_dict.doc2bow(text) for text in Corp]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
index = similarities.MatrixSimilarity(corpus_tfidf)

q_file = open(u'./log_sample.txt')  # 待比较的目标文件
# q_file = open('./tmp_1W.txt')  # 待比较的目标文件
lines = q_file.readlines()
print len(lines)
q_file.close()

# unique_lines = open('./unique.txt').readlines()
unique_lines = open('./unique_regex.txt').readlines()

new_uniq_list = []
new_regex_list = []
# print lines[2457:2460]

num_test=0
# for query in lines[450:500]:
# for query in lines[3257:3259]:
import time
starttime=time.time()
print starttime
# for query in lines[2217505:2217506]:
for query in lines:
    num_test+=1
    query = query.strip()
    # print 'query:',query
    # print len(query)
    tmp_query = ''
    tmp_query = query
    for i in nums:
        tmp_query = tmp_query.replace(str(i),'')    # 将所有的数字移除掉，视作无用信息（停用词）
    vec_bow = unique_dict.doc2bow(tmp_query.split())
    vec_tfidf= tfidf[vec_bow]
    sims = index[vec_tfidf]
    similarity = list(sims)                         #相似度列表
    max_similar = max(similarity)                   #最大相似度
    pos_of_line = similarity.index(max_similar)   #对应文本库中行号


    if max_similar<0.5:     # 对于相似度实在很低的，单独列出
        tmp_str = "%s %s"%(max_similar, query.strip())
        new_uniq_list.append(tmp_str)
        print 'similar= ', max_similar
        print query.strip()
        print unique_lines[pos_of_line]
        print '=============\n'
        open("./to_fix_line.txt", "w").write("\n".join(new_uniq_list))
    else:
        pattern= eval(unique_lines[pos_of_line])[1]
        info = eval(unique_lines[pos_of_line])[2]
        msg = re.search(eval(pattern), query.decode('utf-8'))
        # print pattern
        # print eval(unique_lines[pos_of_line])[0]
        if msg:
            pass
            # print msg
            # print msg.groups()
            # print info
            # print eval(info)['action']
            #print eval(info)
            #print '=============\n'
        else:
            msg = re.search(eval(pattern), query)
            if msg:
                pass
                # print msg
                # print msg.groups()
                # print info
                # print eval(info)['action']
            else:
                print  num_test
                new_regex_list.append(query)
                open("./to_fix_regex.txt", "w").write("\n".join(new_regex_list))
    if num_test%1000000==0:
        print num_test

endtime=time.time()
print 'spend time %ss'%(endtime-starttime)
# open("./to_fix_line.txt","w").write("\n".join(new_uniq_list))   # 保存到单独文件，需要处理后，加入unique.txt中去