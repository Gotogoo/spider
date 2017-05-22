from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from cnBlogs.cnBlogs.spiders.cnBlogSpider import CnBlogsSpider

spider = CnBlogSpider.CnBlogsSpider()  
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()

'''
CREATE DATABASE cnblogsdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `cnblogsinfo` (
  `id` int(11) NOT NULL auto_increment,
  `title` text COMMENT '标题',   
  `link` text  COMMENT 'url链接',
  `date` datetime DEFAULT NULL  COMMENT '发布时间',
  `view` int(11) COMMENT '阅读'
  `description` text COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


#!/usr/bin/python
#coding=utf-8
import pygal
import json
import importlib,sys
# from urllib2 import urlopen  # python 2 syntax
from urllib.request import urlopen # python 3 syntax
import pymysql


from flask import Flask, Response
from pygal.style import DarkSolarizedStyle
from IPython.display import SVG
import sys,os
importlib.reload(sys)


app = Flask(__name__)

#----------------------------------------------------------------------
@app.route('/')
def demoDBMovies():
    
    conn = pymysql.connect(host='localhost',user='root',passwd='941113',db='cnblogsdb',charset='utf8')
   
    cursor = conn.cursor()
    sql = "select * from cnblogsinfo order by id DESC LIMIT 10"
    cursor.execute(sql)
    alldata = cursor.fetchall()

    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Best Top 10 movies in Douban'

    if alldata:
        for rec in alldata:
            #print (rec[0], rec[1])
            line_chart.add(rec[1], rec[0])

    line_chart.render_to_file('routes.svg')	
    
    cursor.close()
    conn.close()
    return Response(response=line_chart.render(), content_type='image/svg+xml')
#----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='127.0.0.1')
'''
    