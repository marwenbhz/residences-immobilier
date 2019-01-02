# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResidencesImmobilierItem(scrapy.Item):
    # define the fields for your item here like:
    VILLE_NAME = scrapy.Field()
    VILLE_LINK = scrapy.Field()
