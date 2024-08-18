import os
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    chat_id = '@cosmos_photos_2_0'
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    bot.send_photo(chat_id=chat_id, photo=open('images/nasa_apod_1.jpg', 'rb'))


if __name__ == '__main__':
    main()