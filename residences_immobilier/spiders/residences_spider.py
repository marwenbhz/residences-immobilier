# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from residences_immobilier.items import ResidencesImmobilierItem



class ResidencesSpiderSpider(scrapy.Spider):
    name = 'residences_spider'
    allowed_domains = ['residences-immobilier.com']
    start_urls = ['https://www.residences-immobilier.com/fr/annonces.html']
    '''
    custom_settings = {
    'LOG_FILE': 'logs/residences-immobilier.log',
    'LOG_LEVEL':'ERROR'
     }
    '''


    def __init__(self, *args, **kwargs):
        super(ResidencesSpiderSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        print('PROCESSIGN...' + response.url)

        villes_link = response.css('ul.departement > a::attr(href)').extract()
        villes_name = response.css('ul.departement > a::text').extract()


        for i in range(0, len(villes_link)):
            yield Request(villes_link[i], callback=self.parse_ville, meta={'ville_link' : villes_link[i], 'ville_name': villes_name[i]})
        

    def parse_ville(self, response):    
        item = ResidencesImmobilierItem()
        item['VILLE_LINK'] = response.url
        item['VILLE_NAME'] = response.meta.get('ville_name')
        yield item