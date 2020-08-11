# -*- coding: utf-8 -*-
import scrapy

g_url = "https://www.ubereats.com"
e = '?slr=1'

class NearMeSpider(scrapy.Spider):
    name = 'near_me'
    allowed_domains = [f'ubereats.com']
    start_urls = [f'https://www.ubereats.com/near-me{e}/']

    # def start_requests(self):
    #     yield scrapy.Request(url=f'https://www.ubereats.com/near-me{e}/', callback=self.parse)
    
    def parse(self, response):
        near_me_links = response.xpath('//*[@class="aw"]/@href').getall()
        for u in near_me_links:
            u = f'{g_url}{u}{e}'
            yield scrapy.Request(url=u, callback=self.parse_near_me)

    def parse_near_me(self, response):
        restaurants = response.xpath('//*[@class="ek bk bl au el al aj em dk"]/a/@href').getall()
        for r in restaurants:
            r = f'{g_url}{r}{e}'
            yield scrapy.Request(url=r, callback=self.parse_restaurant)
    
    def parse_restaurant(self, response):
        res_name = response.xpath('//*[@class="c6 cv ba as dl"][1]/text()').get()
        print("\n\n", res_name)

        yield res_name

