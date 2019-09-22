import scrapy

class CanalTechLinksScrapper(scrapy.Spider):
    name = "canaltech-links"

    allowed_domains = ['canaltech.com.br']

    collection_name = "canaltech-links"
    # Pegando os links para serem scrappeados
    def start_requests(self):
        urls = [f'https://canaltech.com.br/ultimas/p{page}' for page in range(1,5)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Salvando os links em csv para serem usados
    def parse(self, response):
        urls = response.css('div.row').css('a::attr(href)').getall()
        for url in urls:
            if (url.split('/')[1] != 'video') & (url.split('/')[1] != 'podcast') & (url != '/ultimas/'):
                yield {
                        'url':'https://canaltech.com.br'+url
                        }
            else:
                pass