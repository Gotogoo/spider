# -*- coding: utf-8 -*-

import scrapy
import re
import time
from cnBlogs.cnBlogsItems import CnblogsItem

class CnBlogsSpider(scrapy.Spider):
    name = 'cnBlogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com']


    def parse(self, response):
        #/*[@id="post_list"]/div[@class="post_item"]
        for post_list in response.xpath('//*[@id="post_list"]/div[@class="post_item"]'):
            item = CnblogsItem()
            item['title'] = post_list.xpath('.//div[2]/h3/a/text()').extract()
            item['link'] = post_list.xpath('.//div[2]/h3/a/@href').extract()
            #//*[@id="post_list"]/div[1]/div[2]/div
            item['date'] = post_list.xpath('.//div[2]/div/text()').re(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')
            #item['date'] = re.compile(r'(\d{4}-\d{2}-\d{2})').search(post_list.xpath('.//div[2]/div/text()').extract()[-1]).group(1)
            #//*[@id="post_list"]/div[1]/div[2]/div/span[2]/a
            item['view'] = post_list.xpath('.//div[2]/div/span[2]/a/text()').re(r'阅读\((\d+)\)')
            #item['view'] = re.search(r'阅读\((\d+)\)',post_list.xpath('.//div[2]/div/span[2]/a/text()').extract()[0]).group(1)
            #item['view'] = re.compile(r'阅读\((\d+)\)').search(post_list.xpath('.//div[2]/div/span[2]/a/text()').extract()[0]).group(1)
        
            yield item
        #url跟进开始
        #获取下一页的url信息
        #//*[@id="paging_block"]/div/a[13]
        #//*[@id="paging_block"]/div/a[14]
        '''
        url = response.xpath('//*[@id="paging_block"]/div/a[contains(.//text(),"Next")]/@href').extract()
        if url :
            #将信息组合成下一页的url
            page = 'http://www.cnblogs.com' + url[0]
            print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',page)
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        #time.sleep(1000)
        #url跟进结束
        '''

        
if __name__ == "__main__":
    scrapy.cmdline.execute("scrapy crawl cnBlogs".split())
        
  
