import os
import telegram
from dotenv import load_dotenv
import random
import time
import argparse


def main():
    load_dotenv()
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    parser = argparse.ArgumentParser(
        description='Программа для автоматической загрузки изображений в Telegram'
    )
    parser.add_argument('--delay', help='Укажите время задержки между отправкой фотографий (в секундах)', type=int, default=14400)
    args = parser.parse_args()
    while True:
        images = os.listdir("images")
        random.shuffle(images)
        for image in images:
            file_path = f'images/{image}'
            with open(file_path, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(args.delay)


if __name__ == '__main__':
    main()