import requests
from pathlib import Path
from urllib.parse import urlsplit
from os.path import splitext
from dotenv import load_dotenv
import os
import argparse


def download_images(url, file_name, token=''):
    file_path = f'images/{file_name}'
    payload = {
        'api_key': token,
    }   
    response = requests.get(url, params=payload)
    response.raise_for_status() 
    with open(file_path, 'wb') as file:
        file.write(response.content)


def getting_an_extension(url):
    url = urlsplit(url)
    path, extension = splitext(url.path)
    return extension
    

def nasa_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': token,
        'count': 30,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links_images = response.json()
    for image_number, image_link in enumerate(links_images):
        image_link = image_link['url']
        extension = getting_an_extension(image_link)
        file_name = f'nasa_apod_{image_number+1}{extension}'
        download_images(image_link, file_name)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status() 
    links_images = response.json()["links"]['flickr']['original']
    for image_number, image_link in enumerate(links_images):
        file_name = f'space_{image_number+1}.jpg'
        download_images(image_link, file_name)



def epic(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for image in range(5):
        name = response.json()[image]['image']
        year, mouth, day = response.json()[image]['date'].split('-')
        day, time = day.split()
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{mouth}/{day}/png/{name}.png'
        file_name = f'epic_{image+1}.png'
        download_images(img_url, file_name, token)


load_dotenv()
Path("images").mkdir(parents=True, exist_ok=True)
token = os.environ['TOKEN']
epic(token)
nasa_apod(token)
fetch_spacex_last_launch()
