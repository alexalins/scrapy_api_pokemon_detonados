# -*- coding: utf-8 -*-
import scrapy


class DetonadosSpider(scrapy.Spider):
    name = 'detonados'
    allowed_domains = ['https://pokemythology.net/detonados/']
    start_urls = ['http://https://pokemythology.net/detonados//']

    def parse(self, response):
        pass
