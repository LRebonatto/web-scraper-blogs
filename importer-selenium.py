from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
import os

# Configuração do Selenium para rodar em modo headless (sem abrir janela)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# URL do sitemap
SITEMAP_URL = "https://novaturismo.com.br/sitemap.xml"

# Pasta para salvar imagens
IMAGES_FOLDER = "imagens_destacadas"
os.makedirs(IMAGES_FOLDER, exist_ok=True)


def fetch_sitemap_urls(sitemap_url):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, "xml")
    urls = [loc.text for loc in soup.find_all("loc") if "/blog/" in loc.text]
    return urls


def scrape_post_data(driver, url):
    driver.get(url)
    time.sleep(2)  # Aguarda 2 segundos para garantir que o JavaScript seja executado

    # Espera o carregamento do título como condição para seguir com a extração dos dados
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, "h1.blog-show-title.text-center")
    except Exception:
        print(f"Erro: o título não foi carregado em {url}")
        return None

    # Extrair campos de dados
    title = title_element.text
    publication_date = driver.find_element(By.CSS_SELECTOR, ".blog-show-data").text if driver.find_elements(
        By.CSS_SELECTOR, ".blog-show-data") else None
    category = driver.find_element(By.CSS_SELECTOR,
                                   ".blog-show-categorias .categoria-link").text if driver.find_elements(
        By.CSS_SELECTOR, ".blog-show-categorias .categoria-link") else None

    # Extrair conteúdo concatenado
    content_elements = driver.find_elements(By.CSS_SELECTOR, ".blog-show-content .ctt-text p")
    content = " ".join([element.text for element in content_elements])

    # Baixar imagem destacada
    image_element = driver.find_element(By.CSS_SELECTOR, ".ctt-image img") if driver.find_elements(By.CSS_SELECTOR,
                                                                                                   ".ctt-image img") else None
    image_path = None
    if image_element:
        image_url = image_element.get_attribute("src")
        image_name = os.path.join(IMAGES_FOLDER, os.path.basename(image_url))

        # Baixa a imagem
        import requests
        img_data = requests.get(image_url).content
        with open(image_name, "wb") as img_file:
            img_file.write(img_data)
        image_path = image_name

    return {
        "Titulo": title,
        "Data de publicação": publication_date,
        "Categoria": category,
        "Imagem Destacada": image_path,
        "Conteudo": content
    }


def main():
    # Inicia o navegador com o Selenium
    driver = webdriver.Chrome(options=chrome_options)
    post_urls = fetch_sitemap_urls(SITEMAP_URL)
    csv_filename = "blog_posts.csv"

    # Campos do CSV
    fieldnames = ["Titulo", "Data de publicação", "Categoria", "Imagem Destacada", "Conteudo"]

    # Abre o arquivo CSV
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Itera sobre as URLs dos posts
        for post_url in post_urls:
            print(f"Extraindo dados de: {post_url}")
            post_data = scrape_post_data(driver, post_url)
            if post_data:
                writer.writerow(post_data)
            else:
                print(f"Falha ao extrair dados de {post_url}")
            break

    driver.quit()
    print(f"Dados salvos no arquivo {csv_filename}")


if __name__ == "__main__":
    main()
