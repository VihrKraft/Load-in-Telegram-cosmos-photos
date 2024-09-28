from downoad_images import download_image
import requests
from dotenv import load_dotenv
import os
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа для скачивания фотографий Земли с космоса от NASA'
    )
    parser.add_argument('--images_count', help='Введите колличество изображений', type=int, default=5)
    args = parser.parse_args()
    token = os.environ['NASA_API_TOKEN']
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_images = response.json()
    for image_number in range(args.images_count):
        name = epic_images[image_number]['image']
        year, mouth, day = epic_images[image_number]['date'].split('-')
        day, time = day.split()
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{mouth}/{day}/png/{name}.png'
        file_name = f'epic_{image_number+1}.png'
        download_image(img_url, file_name, token)


if __name__ == '__main__':
    main()