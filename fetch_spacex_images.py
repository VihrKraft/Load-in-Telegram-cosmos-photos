import requests
import argparse
from downoad_images import download_image


def main():
    parser = argparse.ArgumentParser(
        description='Программа для скачивания фотографий запуска SpaceX'
    )
    parser.add_argument('--id', help='Введите id изображения', default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    url = f'https://api.spacexdata.com/v5/launches/{args.id}'
    response = requests.get(url)
    response.raise_for_status() 
    links_images = response.json()["links"]['flickr']['original']
    for image_number, image_link in enumerate(links_images, start=1):
        file_name = f'space_{image_number}.jpg'
        download_image(image_link, file_name)


if __name__ == '__main__':
    main()


