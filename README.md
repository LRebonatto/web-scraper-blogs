# Blog Post Scraper

Este repositório contém um script em Python para extrair dados de posts de blog de um site específico, com base em seletores CSS definidos. O script navega em URLs encontradas no sitemap do site, coleta informações específicas de cada post e salva os dados em um arquivo CSV. Além disso, ele baixa as imagens destacadas de cada post em uma pasta local.

## Funcionalidades

- Extração de dados de posts de blog, incluindo título, data de publicação, categoria, conteúdo e imagem destacada.
- Salvamento dos dados em um arquivo CSV.
- Download das imagens destacadas para uma pasta específica.

## Campos Extraídos

O script coleta os seguintes campos para cada post:

- **Título**: Selecionado com o seletor CSS `h1.blog-show-title.text-center`.
- **Data de Publicação**: Selecionado com o seletor `.blog-show-data`.
- **Categoria**: Selecionado com o seletor `.categoria-link`.
- **Imagem Destacada**: Selecionado com o seletor `.ctt-image img` e salvo localmente.
- **Conteúdo**: Todos os textos da classe `.ctt-text`, concatenados.

## Pré-requisitos

Certifique-se de que o Python 3 esteja instalado no seu sistema e que as bibliotecas necessárias estejam instaladas.

### Instalação de Dependências

Use o seguinte comando para instalar as dependências:

```bash
pip install requests beautifulsoup4 lxml
```

## Estrutura do Projeto

```plaintext
.
├── scraper.py            # Arquivo principal do script
├── blog_posts.csv        # Arquivo CSV gerado com os dados dos posts
├── imagens_destacadas/   # Pasta onde as imagens destacadas são salvas
└── README.md             # Este arquivo
```

## Como Usar

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seuusuario/blog-post-scraper.git
    cd blog-post-scraper
    ```

2. Execute o script:

    ```bash
    python scraper.py
    ```

3. O script irá:
   - Ler o sitemap em `https://novaturismo.com.br/sitemap.xml`.
   - Visitar cada URL de post de blog.
   - Extrair os dados e salvá-los em `blog_posts.csv`.
   - Salvar imagens destacadas em uma pasta chamada `imagens_destacadas`.

## Exemplo de Saída

Após executar o script, você verá um arquivo `blog_posts.csv` com o seguinte conteúdo:

```csv
Titulo,Data de publicação,Categoria,Imagem Destacada,Conteudo
"Western Union: uma excelente opção...","01/11/2024","Viagem","imagens_destacadas/imagem1.jpg","Conteúdo do post..."
```

### Observações

- Se o script não encontrar um campo específico, ele registrará o valor como `None`.
- Certifique-se de que o site alvo permite scraping de conteúdo antes de executar o script, respeitando os Termos de Serviço.

## Licença

Este projeto é de uso livre para fins educacionais e de demonstração.