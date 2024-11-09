# Projeto API Avatar - #7DaysOfCode

Este projeto faz parte do desafio **#7DaysOfCode** oferecido pela [Alura](https://www.alura.com.br). O objetivo do desafio é aprender e colocar em prática conhecimentos sobre APIs e desenvolver soluções utilizando ferramentas poderosas do ecossistema Python. Durante o desenvolvimento, você aprenderá a fazer requisições para APIs, processar dados JSON, e interagir com diferentes serviços para alcançar o resultado desejado.

## Descrição do Projeto

Neste projeto, explorei a API do **Avatar: A Lenda de Aang** para obter informações sobre personagens e suas afiliações. Utilizando Python, desenvolvi um script que faz requisições HTTP à API, extrai dados como **nome** e **afiliações** dos personagens e, em seguida, traduz as afiliações para o português.

O código desenvolvido faz o seguinte:

- Faz requisições à API do **Avatar**.
- Extrai dados JSON da resposta da API.
- Traduz as informações de afiliação dos personagens para o português.
- Imprime o nome e a afiliação traduzida de cada personagem.

Através deste desafio, estou aprimorando minhas habilidades em trabalhar com **requisições HTTP**, **tradução de dados** e a manipulação de respostas **JSON**.

## Ferramentas Utilizadas

As principais ferramentas e bibliotecas utilizadas no projeto são:

- **Python**: Linguagem de programação escolhida para desenvolver o script.
- **Requests**: Biblioteca para fazer requisições HTTP e obter dados da API.
- **Deep Translator**: Utilizada para traduzir os dados de afiliação para português de forma prática.
- **Django**: Framework utilizado para criar uma interface web para interagir com os dados, incluindo a criação de uma aplicação Django para rodar localmente.
  
## Instruções de Uso

### Instalação

Clone o repositório:

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Crie e ative um ambiente virtual:

```sh
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

### Execução

Após instalar as dependências, você pode executar o script principal do projeto:

```sh
python app.py
```

Além disso, para rodar o servidor Django, use o seguinte comando:

```sh
python manage.py runserver
```

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador para ver a página inicial.

### Exemplo de Uso

Após rodar o script, será exibida no console uma lista dos personagens de Avatar, contendo o nome e a afiliação (traduzida para português). Exemplo de saída:

```
Nome: Aang, Afiliação: Templo do Ar do Sul
Nome: Zuko, Afiliação: Nação do Fogo
Nome: Katara, Afiliação: Tribo da Água do Sul
```

## Sobre o Desafio #7DaysOfCode

O desafio #7DaysOfCode é uma iniciativa da Alura para promover a prática constante e o aprendizado sobre programação em um período de sete dias. Cada dia traz um desafio novo para ajudar a consolidar o conhecimento e criar algo significativo ao final do desafio.

Você pode participar, compartilhar seu progresso e conectar-se com outros participantes nas redes sociais utilizando as seguintes hashtags:

- **#7DaysOfCode**: Para compartilhar o progresso.
- **@aluraonline**

## Autor

Este projeto foi desenvolvido por [Seu Nome]. Se tiver alguma sugestão ou dúvida, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Conecte-se Comigo!

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/eng.gabrielsf) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/gabriel-souza-fonseca-5764701ab) 
