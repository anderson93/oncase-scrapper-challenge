import scrapy

class GizModoLinksScrapper(scrapy.Spider):
    name = "gizmodo-links"

    allowed_domains = ['gizmodo.uol.com.br']

    collection_name = "gizmodo-links"
    # Pegando os links para serem scrappeados
    def __init__(self,limit_pages, *args, **kwargs):
        super(GizModoLinksScrapper, self).__init__(*args, **kwargs)
        if limit_pages is not None:
            self.limit_pages = int(limit_pages)
        else:
            self.limit_pages = 5

    # Pegando os links para serem scrappeados
    def start_requests(self):
        urls = [f'https://gizmodo.uol.com.br/page/{page}' for page in range(1, self.limit_pages)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Salvando os links em csv para serem usados
    def parse(self, response):
        urls = response.css("article").xpath(".//h3/a/@href").getall()
        for url in urls:
            yield {
                    'url' : url
                  }