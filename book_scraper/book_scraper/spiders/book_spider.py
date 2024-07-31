import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["author.today"]
    start_urls = ["https://author.today/work/tag/бесплатно?ysclid=lz9im1q89l625738659"]

    def parse(self, response):
        rows = response.xpath('//div[contains(@class, "book-row-content")]')
        for row in rows:
            name = row.xpath('.//div[1]/a/text()') .get().strip()
            author = row.xpath('.//div[2]/a/text()') .get().strip()
            genre = row.xpath('.//div[3]/a[2]/text()') .get().strip()
            annotation = row.xpath('.//div[6]/text()') .get().strip()           
            yield {
                'name' : name,
                'author' : author,
                'genre' : genre,
                'annotation' : annotation
            }
       
