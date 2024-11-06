# Blog Scraper - Extração de Dados de Posts de Blog

Este script foi desenvolvido para extrair dados de posts de blog de um site, coletando informações como título, data de publicação, categoria, conteúdo e imagem destacada. O script utiliza o **Selenium** para simular um navegador e lidar com conteúdo dinâmico carregado via JavaScript.

## Funcionalidades

- **Título**: Extrai o título do post.
- **Data de Publicação**: Extrai a data de publicação do post.
- **Categoria**: Extrai a categoria do post.
- **Imagem Destacada**: Extrai o URL da imagem destacada (não faz download da imagem, apenas armazena a URL).
- **Conteúdo**: Concatena todo o texto do conteúdo do post.

### Requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `requests`: Para fazer requisições HTTP.
  - `beautifulsoup4`: Para parsear o HTML.
  - `selenium`: Para simular o navegador e carregar conteúdo JavaScript.
  - `csv`: Para salvar os dados em formato CSV.
  
  Instale as dependências com o comando:
  ```bash
  pip install requests beautifulsoup4 selenium
  ```

- **WebDriver**: Para usar o Selenium com o navegador Chrome, baixe o **ChromeDriver** correspondente à sua versão do Chrome:
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
  - Ou utilize o **GeckoDriver** para Firefox.

  Certifique-se de que o WebDriver esteja no seu PATH ou forneça o caminho completo para ele no script.

## Como Usar

1. **Baixar os Scripts**:
   - `importer.py`: Script principal que faz a extração de dados do blog.
   - `importer_selenium.py`: Versão com Selenium que simula um navegador para carregar conteúdo dinâmico.

2. **Executar o Script**:
   - Abra o terminal ou linha de comando na pasta onde os scripts estão.
   - Execute o script com:
     ```bash
     python3 importer_selenium.py
     ```
   - O script irá buscar as URLs dos posts do sitemap (`https://novaturismo.com.br/sitemap.xml`), acessar cada post e extrair as informações.

3. **Resultados**:
   - Os dados extraídos serão salvos em um arquivo CSV chamado `blog_posts.csv`.
   - O script salva o **src da imagem destacada** ao invés de baixar a imagem.

## Estrutura do CSV

O arquivo CSV gerado conterá as seguintes colunas:

- **Titulo**: O título do post.
- **Data de publicação**: A data de publicação do post.
- **Categoria**: A categoria do post.
- **Imagem Destacada**: A URL da imagem destacada (não o arquivo, apenas o link).
- **Conteudo**: O conteúdo completo do post.

## Exemplo de CSV

```csv
Titulo, Data de publicação, Categoria, Imagem Destacada, Conteudo
"Western Union: uma excelente opção para envio de dinheiro para a sua viagem à Argentina", "2024-11-05", "Outros", "https://novaturismo.com.br/images/ilustracao-1.jpg", "Texto completo do conteúdo do post..."
```

## Como Funciona

1. O script faz uma requisição HTTP ao **sitemap.xml** do site, que contém as URLs dos posts do blog.
2. Para cada URL, o script usa **Selenium** para carregar o conteúdo da página, aguardar o carregamento do JavaScript e então extrair os dados necessários.
3. O script salva os dados extraídos em um arquivo CSV, e a URL da imagem destacada é registrada.

## Observações

- **Lazy Load**: O script foi projetado para lidar com sites que carregam conteúdo dinamicamente através de JavaScript (lazy loading).
- **Execução Headless**: O script usa o Selenium em modo headless, ou seja, sem abrir uma janela de navegador, para otimizar o desempenho.
