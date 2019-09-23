#! /bin/bash

# Checando se existem algumas dependencias
if ! [ -x "$(command -v mongod)" ]; then
    echo 'Error: MongoDB não foi instalado ou não é acessível.' >&2
    exit 1
fi
if ! [ -x "$(command -v python3)" ]; then
    echo 'Warning: Python3 não foi instalado ou não é acessível.' >&2
fi

printf '######################################################################\n'
printf '######################################################################\n'
printf '                      Scrapper Oncase Challenge\n'
printf '######################################################################\n'
printf '######################################################################\n\n'
printf 'O objetivo deste projeto é a execução processo de web crawling 
paraestruturar dados de portais concorrentes de notícias, agregar 
métricas sobre essesdados e disponibilizar informações.\n\n'
printf 'Iremos agora iniciar os processos, portanto é então necessário
saber algumas informações.\n\n'

echo -n 'Deseja um começo cold start (realizarei um drop caso já exista a base tech_news)?
Y ou n: '
read coldstart
# Fazendo o drop na base, para que seja realizado o cold start
if [ $coldstart == 'Y' ]
then
    (python3 drop_tech_db.py)
fi
# Adquirindo as informações do usuário
echo -n 'Quantas páginas das notícias do portal OlharDigital você deseja: '
read limit_pages_olhardigital

echo -n 'E agora do CanalTech: '
read limit_pages_canaltech

echo -n 'E para finalizar, GizModo: '
read limit_pages_gizmodo

# Criando as bases de links
(cd ./techcrawlers && scrapy crawl olhardigital-links -a limit_pages=$limit_pages_olhardigital)
(cd ./techcrawlers && scrapy crawl canaltech-links -a limit_pages=$limit_pages_canaltech)
(cd ./techcrawlers && scrapy crawl gizmodo-links -a limit_pages=$limit_pages_gizmodo)

# Scrappeando os dados
(cd ./techcrawlers && scrapy crawl olhardigital)
(cd ./techcrawlers && scrapy crawl canaltech)
(cd ./techcrawlers && scrapy crawl gizmodo)

printf '######################################################################\n'
printf '######################################################################\n'
printf '                               JOB DONE!\n'
printf '######################################################################\n'
printf '######################################################################\n\n'