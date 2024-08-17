import os
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    chat_id = '@cosmos_photos_2_0'
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

if __name__ == '__main__':
    main()