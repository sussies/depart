#coding:utf-8
import pymongo
import urllib
import ConfigParser
import os,time
from pymongo import MongoClient


config = ConfigParser.ConfigParser()
print os.path.abspath('.')
#file_path = os.path.dirname(os.path.abspath('.')) + '/config.ini'
config.read('config.ini')
configInfo = config.get('dbType','dbHost')
print configInfo

class MongoManage(object):

    def __init__(self):
        pass

    def configInfo(self,pNode,cNode):
        config = ConfigParser.ConfigParser()
        #file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read('config.ini')
        configInfo = config.get(pNode,cNode)
        return configInfo


"""
list = []
wopen = open('','w+')
client = MongoClient('mongodb://172.18.21.171:27017')
db = client.test
db.authenticate('test','test')
with open('ids.txt') as fo:
    rids = fo.readlines()
    for rid in rids:
        rid = rid.strip('\r\n')
        cname = 'eventInfo' + rid
        list.append('%s  %s\n' % (cname,db[cname].count()))
        print cname,db[cname].count()
wopen.writelines(list)
wopen.close()
"""