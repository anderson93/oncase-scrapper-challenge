import scrapy

class OlharDigitalLinksScrapper(scrapy.Spider):
    name = "olhardigital-links"

    allowed_domains = ['olhardigital.com.br']

    collection_name = "olhardigital-links"
    # Pegando os links para serem scrappeados
    def __init__(self,limit_pages=None, *args, **kwargs):
        super(OlharDigitalLinksScrapper, self).__init__(*args, **kwargs)
        if limit_pages is not None:
            self.limit_pages = int(limit_pages)
        else:
            self.limit_pages = 5

    def start_requests(self):
        urls = [f'https://olhardigital.com.br/noticias/{page}' for page in range(1, self.limit_pages)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Salvando os links em csv para serem usados
    def parse(self, response):
        news = response.css("div.blk-items")[0] 
        urls = news.css("a::attr(href)").getall()
        for url in urls:
            yield {
                    'url':'http:'+url
                    }