import scrapy

class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        # Extracting image URLs
        for img in response.css('img.thumbnail'):
            img_url = response.urljoin(img.attrib['src'])
            yield {
                'image_urls': [img_url]
            }

        # Following links to other pages
        for a in response.css('a'):
            yield response.follow(a, callback=self.parse)