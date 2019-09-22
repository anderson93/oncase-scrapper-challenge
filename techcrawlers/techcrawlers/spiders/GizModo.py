import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy
from techcrawlers.mongo_connector import MongoConnector

def timeparser(time_to_be_parsed):
    FULL_MONTHS = {' de janeiro de ': '/01/', ' de fevereiro de ': '/02/', 
                    u' de março de ': '/03/', ' de abril de ': '/04/',
                    ' de maio de ': '/05/', ' de junho de ': '/06/',
                    ' de julho de ': '/07/', ' de agosto de ': '/08/',
                   ' de setembro de ': '/09/', ' de outubro de ': '/10/',
                   ' de novembro de ': '/11/', ' de dezembro de ': '/12/'}
    for word, initial in FULL_MONTHS.items():
        time_to_be_parsed = time_to_be_parsed.replace(word, initial)
    return datetime.datetime.strptime(time_to_be_parsed, "%d/%m/%Y %H:%M")

class GizModoScrapper(scrapy.Spider):
    name = "gizmodo"
    allowed_domains = ['gizmodo.uol.com.br']
    collection_name = "news_data"

    def start_requests(self):
        # Diretório de urls
        # Apesar de ser facil capturar as notícias através do site RSS do portal,
        # perderiamos a possibilidade de pegar também informações como as tags relacionadas a notícia,
        # portanto para esse site continuarei pegando o site normal ao invés de ir pelo 
        # caminho mais prático que seria o RSS
        mongo_provider = MongoConnector(None,None)
        return [scrapy.Request(url=x['url'], callback=self.parse) for x in mongo_provider.get_collection(self.name+'-links').find({})]

    def parse(self, response):
        # Definindo o nome da pasta
        file = response.url.split('/')
        filename = file[3]
        # Nome da pasta principal onde ficarão os arquivos
        main_dir = file[2]

        if os.path.isdir(main_dir):         # Checa se o diretório existe
            pass
        else:
            os.mkdir(main_dir)              # Caso contrário, o cria
        
        with open(os.path.join(main_dir, filename), 'wb') as f:
            f.write(response.body)

        # Limpeza das tags da notícia
        # Why do it the hard way? -> https://stackoverflow.com/a/34532382
        paragraphs = [BeautifulSoup(text, features="lxml").get_text() for text in response.css('div.postContent.bodyCopy.entry-content.clearfix').xpath('.//p').getall()] 
        # Tornando todos os paragrafos em um único elemento, isso se faz necessário por causa da formatação HTML
        # da página, que é quebrada no meio por links de artigos relacionados
        writtentext = ' '.join(paragraphs)
        title = response.css("header")[1].xpath(".//h1/text()").get() 
        tags = response.css('div.postTags-list').xpath('.//a/text()').getall() 
        autor = response.css('div.postMeta--author-author.metaFont.fn').xpath('.//a/text()').get()   
        editor = None
        timepub = timeparser(response.css('div.metaFont.metaDate').xpath('.//abbr/text()').get().replace('@', ''))

        acessedtime = datetime.datetime.now()

        # Checando a consistência dos dados
        assert title is not None
        assert writtentext is not None
        assert autor is not None
        assert editor is None
        assert tags is not None
        assert timepub is not None
        assert acessedtime is not None
        assert response.url is not None

        scraped_info = {
                        'title': title, 
                        'writtennews':writtentext, 
                        'autor' :autor, 
                        'editor':editor, 
                        'tags':tags, 
                        'horapublicado':timepub, 
                        'horaconsulta':acessedtime, 
                        'url':response.url,
                        'website': 'GizModo'
                        }

        #yield or give the scraped info to scrapy
        yield scraped_info