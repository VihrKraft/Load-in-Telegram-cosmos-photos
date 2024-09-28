# Космический Телеграм

Проект позволит скачивать космические фотографии, а так же загружать их в Телеграм-канал.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения

Для работы `epic.py` и `nasa_apod.py` нужен Api токен, который можно получить на [сайте Nasa](https://api.nasa.gov/). Его нужно поместить в файл `.env`, например:
```
NASA_API_TOKEN=yVIsfJkKxUC3e79bCSRghopBpT5TAQzwmhsMvfKy
```

Для публикации фотографий в Телеграм-канал нужно создать бота, добавить его в канал и сделать админом (подробнее [здесь](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#03)). Токен бота и id чата тоже должны быть помещены в файл `.env`. Вот пример:
```
TELEGRAM_BOT_TOKEN=66785732344:HHTlqnXh3LHu4Mo-D2mrOgQKkT4BsrCUxPv
TELEGRAM_CHAT_ID=cosmos_photos_bot
```

### Как запустить

За скачивание изображений Земли отвечает файл `epic.py`: 
```
python epic.py
```

Для скачивания определенного колличества фотографий нужно ввести аргумент `--images_count` и число после него:
```
python epic.py --images_count 7
```

За скачивание изображений дня отвечает `nasa_apod.py`:
```
python nasa_apod.py
```

Так же как и с `epic.py` для скачивания определенного колличества картинок нужно ввести `--images_count` и число:
```
python nasa_apod.py --images_count 12
```

За скачивание изображений запусков отвечает `fetch_spacex_images.py`:
```
python fetch_spacex_images.py
```

Для загрузки определенной картинки нужен id запуска:
```
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```

За публикацию картинок в Telegram отвечает `telegram_bot.py`:
```
python telegram_bot.py
```

Для настройки промежутка времени между публикациями картинок в канал нужно использовать аргумент `--id`, после которого нужно написать колличество времени в секундах:
```
python telegram_bot.py --id 100
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).