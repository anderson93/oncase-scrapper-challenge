## Da decisão do framework:
- Afim de poder realizar o trabalho mais completo e escalável possível, escolhi o uso do framework Scrapy, pois em [alguns pontos](https://www.accordbox.com/blog/scrapy-tutorial-1-scrapy-vs-beautiful-soup/#conclusion) ele supera o seu rival BeautifulSoap, tornando-o a melhor opção para soluções em indústria. 

## Da decisão do backend:
- Ao estudar mais sobre o Scrapy, descobri que ele já tinha conexões de backend com o MongoDB, o que facilitaria a segunda parte do projeto de conexão com o backend.

## Da estrutura da aplicação:
- Apesar de ser facil capturar as notícias através do site RSS do portal, perderiamos a possibilidade de pegar também informações como as tags relacionadas a notícia, portanto escolhi scrappear os sites normais ao invés de ir pelos sites do RSS.

## Exclusão de categorias:
- No site CanalTech, resolvi excluir certas categorias de notícias que eram geralmente posts sobre podcasts ou promocionais do video do canal deles, a decisão foi baseada no fato de que as notícias não possuíam muito texto no corpo, tornando-as pouco relevantes ao objetivo.

## Limpeza das tags:
- Foi necessário também a limpeza das tags para formatação dos dados, evitando casos como "YouTube" e "youtube" na mesma notícia.

## Header HTTP:
- Quando o python faz as requisições no site do GizModo, o servidor não respondia devido a falta de um header http, então nas configurações do Scrapy foi possível a implementação de uma função que aleatoriamente seleciona um novo header, evitando assim as falhas de requisições.

## Limpeza dos dados:
- Devido a estrutura do fluxo de trabalho do Scrapy, a limpeza dos dados foi feita na própria função "parse", que é a função que captura os dados e os insere no MongoDB.