from downoad_images import download_images
import requests
from dotenv import load_dotenv
import os
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа для скачивания фотографий Земли с космоса от NASA'
    )
    parser.add_argument('--number', help='Введите колличество изображений', type=int, default=5)
    args = parser.parse_args()
    token = os.environ['TOKEN']
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for image in range(args.number):
        name = response.json()[image]['image']
        year, mouth, day = response.json()[image]['date'].split('-')
        day, time = day.split()
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{mouth}/{day}/png/{name}.png'
        file_name = f'epic_{image+1}.png'
        download_images(img_url, file_name, token)


if __name__ == '__main__':
    main()