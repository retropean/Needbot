BOT_NAME = 'needbot'
SPIDER_MODULES = ['needbot.spiders']
NEWSPIDER_MODULE = 'needbot.spiders'
DOWNLOAD_DELAY = 6
RANDOMIZE_DOWNLOAD_DELAY = True
ROBOTSTXT_OBEY = False

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [503]
REDIRECT_ENABLED=False

ITEM_PIPELINES = {'needbot.pipelines.SsensebotPipeline': 300, 
				  'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'imagestore'