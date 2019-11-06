import scrapy

class SsensebotItem(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	brand = scrapy.Field()
	imgname = scrapy.Field()
	material = scrapy.Field()
	description = scrapy.Field()
	origin = scrapy.Field()
	image_urls=scrapy.Field()
	images=scrapy.Field()
pass