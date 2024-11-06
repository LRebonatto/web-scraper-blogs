import requests
from bs4 import BeautifulSoup
import os
import csv

# Definindo cabeçalhos para evitar bloqueio
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

# URL do sitemap
SITEMAP_URL = "https://novaturismo.com.br/sitemap.xml"

# Pasta para salvar imagens
IMAGES_FOLDER = "imagens_destacadas"
os.makedirs(IMAGES_FOLDER, exist_ok=True)


def fetch_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "xml")
    urls = [loc.text for loc in soup.find_all("loc") if "/blog/" in loc.text]
    return urls


def scrape_post_data(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrair campos com os seletores especificados
    title = soup.select_one("h1.blog-show-title.text-center").get_text(strip=True) if soup.select_one(
        "h1.blog-show-title.text-center") else None
    publication_date = soup.select_one(".blog-show-data").get_text(strip=True) if soup.select_one(
        ".blog-show-data") else None
    category = soup.select_one(".categoria-link").get_text(strip=True) if soup.select_one(".categoria-link") else None
    content_elements = soup.select(".ctt-text")
    content = " ".join([element.get_text(strip=True) for element in content_elements]) if content_elements else ""

    # Baixar imagem destacada
    image_url = soup.select_one(".ctt-image img")["src"] if soup.select_one(".ctt-image img") else None
    image_path = None
    if image_url:
        image_name = os.path.join(IMAGES_FOLDER, os.path.basename(image_url))
        img_data = requests.get(image_url).content
        with open(image_name, "wb") as img_file:
            img_file.write(img_data)
        image_path = image_name

    # Retornar dicionário com dados extraídos
    return {
        "Titulo": title,
        "Data de publicação": publication_date,
        "Categoria": category,
        "Imagem Destacada": image_path,
        "Conteudo": content
    }


def main():
    post_urls = fetch_sitemap_urls(SITEMAP_URL)
    all_posts_data = []

    # Nome do arquivo CSV
    csv_filename = "blog_posts.csv"

    # Definindo cabeçalhos do CSV
    fieldnames = ["Titulo", "Data de publicação", "Categoria", "Imagem Destacada", "Conteudo"]

    # Abre o arquivo CSV para escrita
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Iterar por cada post e coletar dados
        for post_url in post_urls:
            print(f"Extraindo dados de: {post_url}")
            post_data = scrape_post_data(post_url)
            writer.writerow(post_data)
            all_posts_data.append(post_data)

    print(f"Dados salvos no arquivo {csv_filename}")


if __name__ == "__main__":
    main()
