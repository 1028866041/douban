# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        #print(response.text)

        movies=response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for data in movies:
            item= DoubanItem()
            #db_item['']= data.xpath('.//div[@class="item"]//em/text()')
            item['item']= data.xpath('.//div[@class="info"]//a//span[1]/text()').extract()
            print(item['item'])
            item['star']= data.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()
            print(item['star'])
            item['quote']= data.xpath('.//div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            print(item['quote'])
            '''
            picture= data.xpath('.//div[@class="item"]/div[@class="pic"]/a/img')
            for i in picture:
                content_s= "".join(i)
                db_item['pic']= content_s
            '''
            yield(item)
        '''
        link= response.xpath(".//div/span[@class='next']/link/@href/text()")
        if link:
            link=link[0]
            yield(scrapy.Request("https://movie.douban.com/top25"+str(link), callback=self.parse))
        '''
