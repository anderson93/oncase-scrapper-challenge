import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy
from techcrawlers.mongo_connector import MongoConnector

# As informações de tempo estão em português, então converto-as para o horário padrão
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

def autorparse(autor, response):
    # Algumas paginas possuem a formatação diferente, sendo então necessária essa mudança
    if autor is not None:
       pass
    else:
        try:
            autor = response.css('div.col-xs.by-time').xpath('.//span/text()').get().split('\n')[1] 
        except AttributeError:
            autor = response.css('div.col-xs.by-time').xpath('.//span/text()').get()
        assert autor is not None
    # Algumas vezes aconeceu de aparecer essa string inicial
    if 'Por' in autor:
        autor = autor.replace('Por ','')
    else:
        pass
    # Deixando mais uniforme
    if autor[-1] == ' ':
        autor = autor[:-1]
    else:
        pass
    return autor

class CanalTechScrapper(scrapy.Spider):
    name = "canaltech"

    allowed_domains = ['canaltech.com.br']

    collection_name = "news_data"
    def start_requests(self):
        # Diretório de urls
        # A cada página esse elemento se repete, retiro para evitar conflitos na função parse


        # Removendo artigos de video, pois além da formatação ser diferente, proveem uma 
        # leve explicação somente do video exemplo: https://canaltech.com.br/video/hands-on/apple-iphone-11-unboxinghands-on-11959/
        # - assim como podcast: https://canaltech.com.br/podcast/podcast-canaltech/ct-news-20092019-redmi-8a-xiaomi-lanca-smartphone-bateria-poderosa-3073/

        mongo_provider = MongoConnector(None,None)
        return [scrapy.Request(url=x['url'], callback=self.parse) for x in mongo_provider.get_collection(self.name+'-links').find({})]

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
        
        if os.path.isdir(main_dir):         # Checa se o diretório existe
            pass
        else:
            os.mkdir(main_dir)              # Caso contrário, o cria
        
        with open(os.path.join(main_dir, filename), 'wb') as f:
            f.write(response.body)

        # Limpeza das tags da notícia
        # Why do it the hard way? -> https://stackoverflow.com/a/34532382
        paragraphs = [BeautifulSoup(text, features="lxml").get_text() for text in response.css('div.p402_premium').xpath('.//p').getall()]
        # Tornando todos os paragrafos em um único elemento, isso se faz necessário por causa da formatação HTML
        # da página, que é quebrada no meio por links de artigos relacionados
        writtentext = ' '.join(paragraphs)
        title = response.css('section').xpath('.//h1/text()').get()
        tags = file[3].lower()
        # Limpeza do texto do autor
        autor = autorparse(response.css('div.col-xs.by-time').xpath('.//span/a/text()').get(), response)
        # Algumas notícias são post de propagandas pagas, por isso não tem a data de publicação
        try:
            timepub = timeparser(response.css('div.col-xs.by-time').xpath('.//span/text()').getall()[1])
            assert timepub is not None
        except IndexError:
            timepub = None
            assert timepub is None

        acessedtime = datetime.datetime.now()

        # Checando a consistência dos dados
        assert title is not None
        assert writtentext is not None
        assert autor is not None
        assert tags is not None
        assert acessedtime is not None
        assert response.url is not None

        scraped_info = {
                        'title': title, 
                        'writtennews':writtentext, 
                        'autor' :autor, 
                        'tags':tags, 
                        'horapublicado':timepub, 
                        'horaconsulta':acessedtime, 
                        'url':response.url,
                        'paragraphsnumber':len(paragraphs),
                        'website': 'CanalTech'
                        }
        #yield or give the scraped info to scrapy
        yield scraped_info