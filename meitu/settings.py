# -*- coding: utf-8 -*-

# Author : CandyMI by 2019.9

BOT_NAME = 'meitu'

SPIDER_MODULES = ['meitu.spiders']
NEWSPIDER_MODULE = 'meitu.spiders'

# 日志级别
LOG_LEVEL = 'INFO'

# 日志存放文件夹
LOG_FILE = 'logs/spider.log'

# 静态文件存储文件夹
IMAGES_STORE = 'static'

# 需要注册的Item Pipelines
'''
ITEM_PIPELINES = {
    'meitu.pipelines.SexyPipeline': 30,
    'meitu.pipelines.KoreaPipeline': 30,
    'meitu.pipelines.JapanPipeline': 30,
    'meitu.pipelines.MMPipeline': 30,
    'meitu.pipelines.AnimePipeline': 30,
    'meitu.pipelines.CoserPipeline': 30,
}
'''

# 是否开启HTTP缓存
#HTTPCACHE_ENABLED = True

# request的超时时间(单位为秒), 超过这个时间的缓存request将会被重新下载。如果为0，则缓存的request将永远不会超时.
#HTTPCACHE_EXPIRATION_SECS = 0

# 存储HTTP缓存的目录. 如果为空, 则HTTP缓存将会被关闭.
# 如果为相对目录，则相对于项目数据目录(project data dir).
#HTTPCACHE_DIR = 'cache'

# 不缓存设置中的HTTP返回值(code)的request.
#HTTPCACHE_IGNORE_HTTP_CODES = []

# 如果启用, 在缓存中没找到的request将会被忽略(不下载)
# HTTPCACHE_IGNORE_MISSING = False

# 实现缓存存储后端的类
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 指定数据库模块, 数据库模块.
#HTTPCACHE_DBM_MODULE = "anydbm"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meitu (+http://www.yourdomain.com)'

# 是否遵循robots.txt规则
ROBOTSTXT_OBEY = True

# 是否关闭Cookie, 默认情况下为False
COOKIES_ENABLED = True

# 是否开启远程终端(默认为开启)
TELNETCONSOLE_ENABLED = True

# telnet终端使用的端口范围。如果设置为None或0, 则使用动态分配的端口。
TELNETCONSOLE_PORT = [6023, 6073]

# Scrapy downloader并发请求(concurrent requests)的最大值. (默认是: 16)
CONCURRENT_REQUESTS = 16

# 下载器在下载同一个网站下一个页面前需要等待的时间. 该选项可以用来限制爬取速度, 减轻服务器压力.
DOWNLOAD_DELAY = 3


# 对单个网站进行并发请求的最大值
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定, 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
# 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非 0, 下载延迟应用在IP而不是网站上。
# CONCURRENT_REQUESTS_PER_IP = 16

# 其它一些可选或不重要的参数值请自行配置, 这里仅列出常用配置.
