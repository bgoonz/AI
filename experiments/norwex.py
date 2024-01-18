import os
import requests
from bs4 import BeautifulSoup
from markdown import markdown

def download_image(image_url, folder_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, 'product_image.jpg'), 'wb') as file:
            file.write(response.content)

def save_markdown(content, folder_name):
    with open(os.path.join(folder_name, 'product_details.md'), 'w') as file:
        file.write(markdown(content))

def extract_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # You need to find the correct tags and classes for these elements
    product_name = soup.find('tag_name', {'class': 'class_name'}).text.strip()
    product_price = soup.find('tag_name', {'class': 'class_name'}).text.strip()
    product_description = soup.find('tag_name', {'class': 'class_name'}).text.strip()
    image_url = soup.find('img', {'class': 'class_name'})['src']

    return product_name, product_price, product_description, image_url

def main(url):
    product_name, product_price, product_description, image_url = extract_product_details(url)
    folder_name = product_name.replace(' ', '_')

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    markdown_content = f"## {product_name}\n\n**Price:** {product_price}\n\n**Description:**\n{product_description}"
    save_markdown(markdown_content, folder_name)
    download_image(image_url, folder_name)

if __name__ == '__main__':
    url = 'https://www.norwex.com/p/pet-mitt?store=us'
    main(url)
