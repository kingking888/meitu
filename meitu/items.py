# -*- coding: utf-8 -*-

# Author : CandyMI by 2019.9

import scrapy

# 基本数据结构, 可继承后自行编写扩展或直接扩展.
class BaseItem(scrapy.Item):
    image_name = scrapy.Field() # 图片/文章名称
    image_url = scrapy.Field()  # 图片的下载路径
    link_url = scrapy.Field()   # 每一份文章的链接地址
    dir = scrapy.Field()        # 文件分类目录
