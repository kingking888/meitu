#!/usr/bin/env python

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 爬虫项目列表
from meitu.spiders.anime import AnimeSpider
from meitu.spiders.coser import CoserSpider
from meitu.spiders.japan import JapanSpider
from meitu.spiders.korea import KoreaSpider
from meitu.spiders.sexy import SexySpider
from meitu.spiders.mm import MMSpider

if __name__ == '__main__':
    loop = CrawlerProcess(get_project_settings())
    loop.crawl(MMSpider)
    loop.crawl(SexySpider)
    loop.crawl(KoreaSpider)
    loop.crawl(JapanSpider)
    loop.crawl(AnimeSpider)
    loop.crawl(CoserSpider)
    loop.start()
