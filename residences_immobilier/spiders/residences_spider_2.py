# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from residences_immobilier.items import ResidencesImmobilierItem



class ResidencesSpiderSpider(scrapy.Spider):
    name = 'residences_spider_2'
    allowed_domains = ['residences-immobilier.com']
    start_urls = ['https://www.residences-immobilier.com/fr/recherche.html?lang=FR&departement=&district=&villes=&tri=&fromGG=&setLocDep=&TypeAnnonceV=on&ville_dep=&enlarge_search=0&TypeBien=&nb_piece=&bdgMin=&bdgMax=&surfMin=&surfMax=&keywords=']
    
    custom_settings = {
    'LOG_FILE': 'logs/residences-immobilier.log',
    'LOG_LEVEL':'ERROR'
     }


    def __init__(self, *args, **kwargs):
        super(ResidencesSpiderSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        print('PROCESSIGN...' + response.url)

        
        #relative_next_url = response.xpath('//a[@class="wrap-pagination-item js-page-next"]/@href').extract_first()
        relative_next_url = response.css('ul.pagination > li > a::attr(href)').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)




