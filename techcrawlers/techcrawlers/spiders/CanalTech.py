import pandas as pd
import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy

def timeparser(time_to_be_parsed):
    FULL_MONTHS = {' de janeiro de ': '/01/', ' de fevereiro de ': '/02/', 
                    u' de março de ': '/03/', ' de abril de ': '/04/',
                    ' de maio de ': '/05/', ' de junho de ': '/06/',
                    ' de julho de ': '/07/', ' de agosto de ': '/08/',
                   ' de setembro de ': '/09/', ' de outubro de ': '/10/',
                   ' de novembro de ': '/11/', ' de dezembro de ': '/12/'}
    time_to_be_parsed = time_to_be_parsed.split('|')[1][1:-1].lower().replace(' às', '')
    for word, initial in FULL_MONTHS.items():
        time_to_be_parsed = time_to_be_parsed.replace(word, initial)
    return datetime.datetime.strptime(time_to_be_parsed, "%d/%m/%Y %Hh%M")

class OlharDigitalScrapper(scrapy.Spider):
    name = "canaltech-links"

    allowed_domains = ['canaltech.com.br']
    def start_requests(self):
        # Diretório de urls
        # Apesar de ser facil capturar as notícias através do site RSS do portal,
        # perderiamos a possibilidade de pegar também informações como as tags relacionadas a notícia,
        # portanto para esse site continuarei pegando o site normal ao invés de ir pelo 
        # caminho mais prático que seria o RSS
        return map(lambda x: scrapy.Request(url=x, callback=self.parse), pd.read_csv('canaltech-links.csv')['url'].values)

    def parse(self, response):
        # Definindo o nome da pasta
        file = response.url.split('/')
        for i, text in enumerate(file):
            if text == 'canaltech.com.br':
                aux = i+2
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
        paragraphs = [BeautifulSoup(text).get_text() for text in response.css('div.p402_premium').xpath('.//p').getall()]
        # Tornando todos os paragrafos em um único elemento, isso se faz necessário por causa da formatação HTML
        # da página, que é quebrada no meio por links de artigos relacionados
        writtentext = ' '.join(paragraphs)
        title = response.css('section').xpath('.//h1/text()').get()
        tags = file[3]
        autor = response.css('div.col-xs.by-time').xpath('.//span/a/text()').get()

        if 'editado' in autor:
            editor = autor.split('por')[1][1:]
            autor = autor.split(',')[0]
            assert editor is not None
        else:
            editor = None
            assert editor is None


        time_to_parse = response.css('div.col-xs.by-time').xpath('.//span/text()').getall()[1]
        timepub = timeparser(time_to_parse)

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
                        'hora da publicação':timepub, 
                        'hora de acesso':acessedtime, 
                        'url':response.url
                        }
        #yield or give the scraped info to scrapy
        yield scraped_info