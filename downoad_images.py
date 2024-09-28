from pathlib import Path
import requests
import os


def download_image(url, file_name, token=''):
    Path("images").mkdir(parents=True, exist_ok=True)
    file_path = f'images/{file_name}'
    payload = {
        'api_key': token,
    }   
    response = requests.get(url, params=payload)
    response.raise_for_status() 
    with open(file_path, 'wb') as file:
        file.write(response.content)