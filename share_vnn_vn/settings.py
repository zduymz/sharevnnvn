# -*- coding: utf-8 -*-

# Scrapy settings for share_vnn_vn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'share_vnn_vn'

SPIDER_MODULES = ['share_vnn_vn.spiders']
NEWSPIDER_MODULE = 'share_vnn_vn.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'share_vnn_vn (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
#    'share_vnn_vn.scrapy_mongodb.MongoDBPipeline',
    'share_vnn_vn.scrapy_elasticsearch.ElasticSearchPipeline'
}

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'sharevnnvn'

from scrapy import log
STICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'scrapy'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'ID'
ELASTICSEARCH_LOG_LEVEL= log.DEBUG

