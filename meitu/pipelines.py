# -*- coding: utf-8 -*-

# Author : CandyMI by 2019.9

# 这里简单的解释一下 self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1].
# 其实就是 '/static/sexy/文章名称/xxx.jpg' 拼接而成的路径.

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class SexyPipeline(ImagesPipeline):
    prefix = 'sexy'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]

class MMPipeline(ImagesPipeline):
    prefix = 'mm'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]


class JapanPipeline(ImagesPipeline):
    prefix = 'japan'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]


class KoreaPipeline(ImagesPipeline):
    prefix = 'korea'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]

class CoserPipeline(ImagesPipeline):
    prefix = 'anime'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]

class AnimePipeline(ImagesPipeline):
    prefix = 'anime'
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta = item)

    def file_path(self, request, response=None, info=None):
        return self.prefix + '/' + request.meta['dir'] + '/' + request.meta['image_url'].split('/')[-1]
