# oncase-scrapper-challenge
Projeto para cumprimento de tarefa desafio definida pelo processo de seleção da empresa Oncase Intelligence Consulting33

<!-- ÍNDICE -->
## Índice

* [Sobre o Projeto](#sobre-o-projeto)
  * [Feito com](#feito-com)
* [Início](#início)
  * [Prerequisitos](#prerequisitos)
    * [MongoDb - Linux](#mongodb---linux)
  * [Instalação](#instalação)
* [Uso](#uso)
* [Roadmap](#roadmap)
* [Contribuição](#contribuição)
* [Licença](#licença)
* [Contato](#contato)
* [Reconhecimentos](#reconhecimento)



<!-- SOBRE O PROJETO -->
## Sobre o Projeto

Projeto para cumprimento de tarefa desafio definida pelo processo de seleção da empresa Oncase Intelligence Consulting. O projeto consiste em desenvolver um processo de web crawling para estruturar dados de portais concorrentes de notícias, agregar métricas sobre essesdados e disponibilizar as informações. 

O tema escolhido nesse projeto é o de tecnologia, agregaremos então as notícias de três portais: [OlharDigital](https://olhardigital.com.br), [CanalTech](https://canaltech.com.br) e [GizModo](https://gizmodo.uol.com.br).

### Feito com

* [Scrapy](https://scrapy.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [MongoDB](https://www.mongodb.org)
* [PyMongo](https://api.mongodb.com/python/current/)


<!-- INÍCIO -->
## Início

Para que possamos dar início à aquisição dos dados, será necessário o cumprimento das seguintes etapas explicadas abaixo.

### Prerequisitos

Primeiramente teremos de configurar o MongoDB para que possamos usa-lo.

#### MongoDb - Linux

- [RedHat](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
- [Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [Debian](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/)
- [SUSE](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-suse/)
- [Amazon Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/)

#### MongoDb - MacOS
```sh
brew tap mongodb/brew
brew install mongodb-community@4.2
brew services start mongodb-community@4.2
```
- Para mais informações sobre como [instalar o MongoDB no MacOS.](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

### Instalação
 
1. Clone o repositório
```sh
git clone https://github.com/anderson93/oncase-scrapper-challenge.git
```
2. Instalação dos pacotes do Python 3.7.4:
```sh
pip3 install -r requirements.txt
```

<!-- EXEMPLOS DE USO -->
## Uso

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

Veja a seção [open issues](https://github.com/anderson93/oncase-scrapper-challenge/issues) para uma lista de melhorias sugeridas e problemas/bugs conhecidos.

### TODO: arquivo do log do projeto: ideias, decisões e reflexões ao longo do projeto.

<!-- CONTRIBUIÇÃO -->
## Contribuição

Contribuições é o que faz a comunidade open source forte e um maravilhoso ambiente para aprender, se insipirar e criar. Quaisquer contribuições serão **efusivamente bem vindas.**

1. Fork o projeto
2. Crie seu ramo (`git checkout -b feature/FabulosoFeature`)
3. Dê commit nas suas melhorias (`git commit -m 'Adicionando Fabulosidade'`)
4. Dê push para o ramo (`git push origin feature/FabulosoFeature`)
5. Abra um Pull request!
6. ???
7. Profit!



<!-- LICENÇA -->
## Licença

Distribuída sob a licença MIT. Veja `LICENSE` para mais informações.

<!-- CONTATO -->
## Contato

Anderson Henrique de Oliveira Conceição - [email](mailto:anderson93@gmail.com)

Project Link: [https://github.com/anderson93/oncase-scrapper-challenge](https://github.com/anderson93/oncase-scrapper-challenge)

<!-- RECONHECIMENTOS -->
## Reconhecimentos

* Obrigado a Oncase por me fornecer essa oportunidade de demonstrar o um pouco do meu conhecimento através deste desafio.
* Agradeço também a comunidade Open-Source sem a qual jamais estaríamos desenvolvendo tecnologia e soluções a nivel industrial tão facilmente.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/anderson-hoc/