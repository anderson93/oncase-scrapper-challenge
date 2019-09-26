import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy
from techcrawlers.mongo_connector import MongoConnector


class OlharDigitalScrapper(scrapy.Spider):
    name = "olhardigital"
    allowed_domains = ['olhardigital.com.br']

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
        for i, text in enumerate(file):
            if text == 'noticia':
                aux = i+1
            else:
                pass
        filename = file[aux]
        # Nome da pasta principal onde ficarão os arquivos
        main_dir = file[2]
        #TODO: salvar em pasta personalizada do portal de noticias referente -> file[2]
        if os.path.isdir(main_dir):         # Checa se o diretório existe
            pass
        else:
            os.mkdir(main_dir)              # Caso contrário, o cria
        
        with open(os.path.join(main_dir, filename), 'wb') as f:
            f.write(response.body)

        # Limpeza das tags da notícia
        # Why do it the hard way? -> https://stackoverflow.com/a/34532382
        paragraphs = [BeautifulSoup(text).get_text() for text in response.css('div.mat-txt').xpath('.//p').getall()] 
        # Tornando todos os paragrafos em um único elemento, isso se faz necessário por causa da formatação HTML
        # da página, que é quebrada no meio por links de artigos relacionados
        writtentext = ' '.join(paragraphs)
        title = response.css('div.mat-imagem').xpath(".//h1/text()").get()
        tags = list(set([x.lower() for x in response.css('div.mat-tags').xpath(".//span/text()").getall()]))
        autor, datepub, hourpub = response.css('div.mat-meta').xpath(".//span/text()").getall()
        if 'editado' in autor:
            editor = autor.split('por')[1][1:]
            autor = autor.split(',')[0]
            assert editor is not None
        else:
            editor = None
            assert editor is None

        timepub = datetime.datetime.strptime(datepub+' '+hourpub, "%d/%m/%Y %Hh%M")
        acessedtime = datetime.datetime.now()

        # Checando a consistência dos dados
        assert title is not None
        assert writtentext is not None
        assert autor is not None
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
                        'paragraphsnumber':len(paragraphs),
                        'website': 'OlharDigital'
                        }

        #yield or give the scraped info to scrapy
        yield scraped_info