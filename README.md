# oncase-scrapper-challenge
Projeto para cumprimento de tarefa desafio definida pelo processo de seleção da empresa Oncase Intelligence Consulting33

<!-- ÍNDICE -->
## Índice

* [ASObre o Projeto](#sobre-o-projeto)
  * [Feito com](#feito-com)
* [Início](#inicio)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



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

Primeiramente teremos de configurar o MongoDB para que possamos usa-lo
* MongoDb - Linux
- [RedHat](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
- [Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [Debian](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/)
- [SUSE](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-suse/)
- [Amazon Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/)
* MongoDb - MacOS
```sh
brew tap mongodb/brew
brew install mongodb-community@4.2
brew services start mongodb-community@4.2
```
- Para mais informações sobre como [instalar o MongoDB no MacOS.](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

### Installation
 
1. Clone o repositório
```sh
git clone https://github.com/anderson93/oncase-scrapper-challenge.git
```
2. Instalação dos pacotes do Python 3.7.4:
```sh
pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo](https://github.com/github_username/repo)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png