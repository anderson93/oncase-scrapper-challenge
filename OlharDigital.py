import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy

class OlharDigitalScrapper(scrapy.Spider):
    name = "olhardigital"
    allowed_domains = ['olhardigital.com.br']
 
    def start_requests(self):
        # Diretório de urls
        # Apesar de poder pegar mais facilmente as notícias através do site RSS do portal,
        # perderiamos a possibilidade de pegar também informações como as tags relacionadas a notícia,
        # portanto para esse site continuarei pegando o site normal ao invés de ir pelo 
        # caminho mais prático que seria o RSS
        fetch("https://olhardigital.com.br/noticias/")  
        # urls parsed
        news = response.css("div.blk-items")[0] 
        urls = news.css("a::attr(href)").getall()
        for url in urls:
            yield scrapy.Request(url='http:'+url, callback=self.parse)

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
        tags = response.css('div.mat-tags').xpath(".//span/text()").getall() 
        autor, datepub, hourpub = response.css('div.mat-meta').xpath(".//span/text()").getall()
        if 'editado' in autor:
            editor = autor.split('por')[1][1:]
            autor = autor.split(',')[0]
        else:
            editor = None
        timepub = datetime.datetime.strptime(datepub+' '+hourpub, "%d/%m/%Y %Hh%M")
        acessedtime = datetime.datetime.now()

        # Checando a consistência dos dados
        assert title is not None
        assert writtentext is not None
        assert autor is not None
        assert editor is not None
        assert tags is not None
        assert timepub is not None
        assert acessedtime is not None
        assert url is not None

        # TODO: Definir arquivo de carregamento para a base
        # Itens de saída:
        # title
        # writtentext
        # autor
        # editor
        # tags
        # timepub
        # acessedtime
        # url

        self.log('Saved file %s' % filename)
