from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import MitologiawspolczesnaItem


class MitwspSpider(CrawlSpider):
    name = "mitwsp"
    allowed_domains = ["mitologiawspolczesna.pl"]
    start_urls = ["http://mitologiawspolczesna.pl/blog/"]

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="(//div[@class='iw-so-blog'])[2]//div/a"), callback="parse_item", follow=True
        ),
        Rule(LinkExtractor(restrict_xpaths="(//li[@class='iw-so-blog-next'])[2]/a")),
    )

    def parse_item(self, response):
        loader = ItemLoader(item=MitologiawspolczesnaItem(), response=response)
        loader.add_xpath("tytul", "//h1/text()")
        loader.add_xpath(
            "tresc",
            "//div[@class='entry-content entry--item']/*[not(self::div[@class='wp_rp_wrap  wp_rp_vertical'])]//text()",
        )
        loader.add_value("link", response.url)

        yield loader.load_item()
