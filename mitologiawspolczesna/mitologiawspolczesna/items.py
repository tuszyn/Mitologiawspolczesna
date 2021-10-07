# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose


class MitologiawspolczesnaItem(scrapy.Item):

    tytul = scrapy.Field()
    tresc = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=Join())
    link = scrapy.Field()
    # name = scrapy.Field()
