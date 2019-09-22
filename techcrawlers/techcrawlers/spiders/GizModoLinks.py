import scrapy

class GizModoLinksScrapper(scrapy.Spider):
    name = "gizmodo-links"

    allowed_domains = ['gizmodo.uol.com.br']

    collection_name = "gizmodo-links"

    # Pegando os links para serem scrappeados
    def start_requests(self):
        urls = [f'https://gizmodo.uol.com.br/page/{page}' for page in range(1,5)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Salvando os links em csv para serem usados
    def parse(self, response):
        urls = response.css("article").xpath(".//h3/a/@href").getall()
        for url in urls:
            yield {
                    'url' : url
                  }