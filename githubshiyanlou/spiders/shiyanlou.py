# -*- coding: utf-8 -*-
import scrapy
from githubshiyanlou.items import GithubshiyanlouItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    allowed_domains = ['github.com']
    start_urls = []
    base_url = 'https://github.com/shiyanlou?tab=repositories&page={}'
    for i in range(1, 5):
        start_urls.append(base_url.format(i))

    def parse(self, response):
        # print(response.url)
        item = GithubshiyanlouItem()
        for i in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            item['name'] = i.xpath('div[1]/h3/a/text()').extract()[0].strip()
            item['update_time'] = i.xpath('div[3]/relative-time/@datetime').extract()[0]
            yield item
