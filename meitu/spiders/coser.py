# -*- coding: utf-8 -*-

# Author : CandyMI by 2019.9

import scrapy
from meitu.items import BaseItem

class CoserSpider(scrapy.Spider):
    article_list = []
    name = 'coser'
    custom_settings = { "ITEM_PIPELINES": { "meitu.pipelines.CoserPipeline" : 300 } }
    start_urls = ['https://www.ilemiss.net/cosplay/']

    def parse(self, response):
        for index in range(len(response.xpath('//div[@class="imainbox"]/ul/li')) + 1) :
            image_name = response.xpath('//div[@class="imainbox"]/ul/li[{}]//img/@alt'.format(index)).extract_first()
            image_url = response.xpath('//div[@class="imainbox"]/ul/li[{}]//img/@src'.format(index)).extract_first()
            link_url = response.xpath('//div[@class="imainbox"]/ul/li[{}]//a/@href'.format(index)).extract_first()
            if not image_name or not image_url or not link_url :
                continue
            article = BaseItem(image_name = image_name, image_url = image_url, link_url = link_url, dir = image_name)
            self.article_list.append(article)
            yield article
        # # 是否需要对下一页的数据进行抓取
        # if response.xpath('//span[text() = "下一页"]').re_first('>(.*)<') is not None :
        #     next_page = response.xpath('//div[@class="wlistpages"]/a[{}]//@href'.format(len(response.xpath('//div[@class="wlistpages"]/a')) - 1)).extract_first()
        #     yield scrapy.Request(url = next_page, callback = self.parse)
        #
        # # 对每个文章的数据使用指定的方法进行解析
        # for item in self.article_list :
        #     yield scrapy.Request(url = item['link_url'], callback = self.article_parse, meta = item)

    # def article_parse(self, response):
    #     image_url  = response.xpath('//div[@class="contentpic"]/img/@src').extract_first()
    #     image_name = response.xpath('//div[@class="contentpic"]/img/@alt').extract_first()
    #     if image_url and image_name :
    #         yield BaseItem(image_name = image_name, image_url = image_url, dir = response.meta['dir'])
    #
    #     art_url = response.urljoin(response.xpath('//span[@class="nextpage"]/a/@href').extract_first())
    #     if response.xpath('//span[@class="nextpage"]') :
    #         yield scrapy.Request(url = art_url , callback = self.article_parse, meta = response.meta)
