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
            # montando dados
            image1 = detonado.css('td')[0]
            dados = detonado.css('td')[1]
            image2 = detonado.css('td')[2]
            linkCod = dados.css('p')[1]
            # images
            images = []
            images.append(image1.css('p img::attr(src)').get())
            img2 = image2.css('p img::attr(src)').get()
            # tinha caso de não vim no p
            if img2 is not None:
                images.append(img2)
            else:
                #verificando se tem tag img
                img2 = image2.css('img::attr(src)').get()
                images.append(img2)
            # usando extract pq podem vim textos separados
            title = dados.css('p strong span::text').extract()
            # juntando textos em 1 só
            title = " ".join(title)
            link = linkCod.css('a::attr(href)').get()
            # se não vier o link inteiro
            if link[0] == '/':
                link = 'https://pokemythology.net/detonados' + link
            # se title for nulo
            if title is not None:
                detonado = DetonadosItem(images=images, title = title, link = link)
                yield detonado
