import scrapy


class DmozScraper(scrapy.Spider):
    name='dmozbook'
    start_urls=['https://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
                'https://dmoz-odp.org/Computers/Programming/Languages/Python/FAQs%2C_Help%2C_and_Tutorials/',]

    def parse(self, response):
        for site in response.xpath('//div[@class = "title-and-desc"]'):
            yield {
                'name': site.xpath('.//div[@class="site-title"]/text()').extract_first(),
                'url': site.xpath('.//@href').extract_first(),
            }