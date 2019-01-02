from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from residences_immobilier.spiders.residences_spider import ResidencesSpiderSpider

process = CrawlerProcess(get_project_settings())
process.crawl(ResidencesSpiderSpider)
process.start()

