import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from datetime import date, time
import json
import datetime
import time
from needbot.items import SsensebotItem
import image

#selenium dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support import expected_conditions as EC
from scrapy.loader.processors import Join, MapCompose
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

class needbot(Spider):
	name = "needbot"
	allowed_domains = ["needsupply.com"]

	def __init__(self, domain="https://needsupply.com/mens/brands/calvin-klein-jeans-est-1978", *args, **kwargs):
		self.start_urls = [domain]
		LOGGER.setLevel(logging.WARNING)
		opts = ChromeOptions()
		opts.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(chrome_options=opts, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
		self.driver.set_window_size(1500, 768)
		
	def parse(self, response):
		self.driver.get(response.url)
		self.wait = WebDriverWait(self.driver, 500)
		items = []
		productlist = []
		productlist = self.driver.find_elements_by_xpath('//div[@class="product-grid row"]/div')
		print(len(productlist))
		i = 1
		image_urls = []
		while (i < len(productlist)):
			item = SsensebotItem()
			searchstring = '//*[@id="product-search-results"]/div[2]/div[2]/div[2]/div['+str(i)+']'
			elem = self.driver.find_element_by_xpath(searchstring)
			elem.click()
			self.driver.implicitly_wait(10)	
			#scrape it  
			item['brand'] = self.driver.find_element_by_xpath('//div[@class="product-heading col-12 d-lg-block d-none"]/h2[@class="brand-name"]/a').text
			item['name'] = self.driver.find_element_by_xpath('//div[@class="product-heading col-12 d-lg-block d-none"]/h3[@class="product-name"]').text
			item['price'] = self.driver.find_element_by_xpath('//div[@class="product-heading col-12 d-lg-block d-none"]/div[@class="prices"]/div[@class="price"]/span/span/span').text
			item['description'] = self.driver.find_element_by_xpath('//div[@id="product-description"]/pre').text
			imglist = self.driver.find_elements_by_xpath('//ol[@class="carousel-indicators"]/li')
			item['image_urls'] = []
			count=0
			for img in imglist:
				hover = ActionChains(self.driver).move_to_element(img)
				hover.perform()
				time.sleep(5)
				image_urls.append(img.find_element_by_xpath('//div[@class="carousel-item active"]/img').get_attribute('src'))
				item['image_urls'].append(img.find_element_by_xpath('//div[@class="carousel-item active"]/img').get_attribute('src'))
				count = 1 + count
			#and get out  
			self.driver.execute_script("window.history.go(-1)")
			i = i + 1
			items.append(item)

		return items
		return image_urls