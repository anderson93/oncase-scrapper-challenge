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

echo -n 'Deseja um começo cold start (realizarei um drop caso já exista a base 
tech_news e eliminarei também os logs da pasta)?
Y ou n: '
read coldstart
# Fazendo o drop na base, para que seja realizado o cold start
if [ $coldstart == 'Y' ]
then
    (python3 drop_tech_db.py)
    (rm -rf /techcrawlers/logs)
fi
# Adquirindo as informações do usuário
echo -n 'Quantas páginas das notícias do portal OlharDigital você deseja: '
read limit_pages_olhardigital

echo -n 'E agora do CanalTech: '
read limit_pages_canaltech

echo -n 'E para finalizar, GizModo: '
read limit_pages_gizmodo

mkdir ./techcrawlers/logs

# Criando as bases de links
(cd ./techcrawlers && scrapy crawl olhardigital-links -a limit_pages=$limit_pages_olhardigital --logfile ./logs/olhardigital-links.log)
printf 'Links do OlharDigital capturados! 1/3\n'

(cd ./techcrawlers && scrapy crawl canaltech-links -a limit_pages=$limit_pages_canaltech --logfile ./logs/canaltech-links.log)
printf 'Links do CanalTech capturados! 2/3\n'

(cd ./techcrawlers && scrapy crawl gizmodo-links -a limit_pages=$limit_pages_gizmodo --logfile ./logs/gizmodo-links.log)
printf 'Links do GizModo capturados! 3/3\n'

# Scrappeando os dados
(cd ./techcrawlers && scrapy crawl olhardigital --logfile ./logs/olhardigital-scrapper.log)
printf 'Páginas do OlharDigital capturadas! 1/3\n'

(cd ./techcrawlers && scrapy crawl canaltech --logfile ./logs/canaltech-scrapper.log)
printf 'Páginas do CanalTech capturadas! 2/3\n'

(cd ./techcrawlers && scrapy crawl gizmodo --logfile ./logs/gizmodo-scrapper.log)
printf 'Páginas do GizModo capturadas! 3/3\n\n'

printf '######################################################################\n'
printf '######################################################################\n'
printf '                               JOB DONE!\n'
printf '######################################################################\n'
printf '######################################################################\n\n'
