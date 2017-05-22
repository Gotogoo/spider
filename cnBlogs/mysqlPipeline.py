# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

class MysqlPipeline(object):
    #采用同步机制写入mysql
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','941113'
        ,'cnblogsdb',charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self,item,spider):
        insert_sql = ("insert into cnblogsinfo(title, link, date, view) VALUES (%s, %s, %s, %s)") 
        self.cursor.execute(insert_sql, (item["title"], item["link"], item["date"], item["view"]))
        self.conn.commit()
        return item

'''
from twisted.enterprise import adbapi
class MysqlTwistedPipline(object):
    #异步插入mysql
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        #传入settings的参数
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print (failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        #根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        print (insert_sql, params)
        cursor.execute(insert_sql, params)
'''