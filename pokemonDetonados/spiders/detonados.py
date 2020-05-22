# -*- coding: utf-8 -*-
import scrapy
from pokemonDetonados.items import DetonadosItem


class DetonadosSpider(scrapy.Spider):
    name = 'detonados'
    allowed_domains = ['https://pokemythology.net/detonados/']
    start_urls = ['https://pokemythology.net/detonados/']

    def parse(self, response):

        for item in response.css('table'):
            detonado = item.css('tbody tr')
            # images
            images = []
            image1 = detonado.css('td p img::attr(src)')[0].get()
            image2 = detonado.css('td p img').get()
            images.append(image1)
            images.append(image2)
            detonado = DetonadosItem(images=images)
            yield detonado
