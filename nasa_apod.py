import requests
from downoad_images import download_images
from os.path import splitext
from urllib.parse import urlsplit
import os
import argparse


def getting_an_extension(url):
    url = urlsplit(url)
    path, extension = splitext(url.path)
    return extension


def main():
    parser = argparse.ArgumentParser(
        description='Программа для скачивания фотографий дня NASA'
    )
    parser.add_argument('--images_count', help='Введите колличество изображений', default=30)
    args = parser.parse_args()
    token = os.environ['TOKEN']
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': token,
        'count': args.images_count,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links_images = response.json()
    for image_number, image_link in enumerate(links_images):
        image_link = image_link['url']
        extension = getting_an_extension(image_link)
        file_name = f'nasa_apod_{image_number+1}{extension}'
        download_images(image_link, file_name)


if __name__ == '__main__':
    main()