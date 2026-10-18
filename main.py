
import requests
from config import API_KEY
from urllib.parse import quote
from pathlib import Path


def create_img(text):# Заголовки запроса (ключ передаётся как Bearer-токен)
    headers = {
        "authorization": "Bearer %s" % API_KEY
    }

    # Текстовый запрос: описываем, какую картинку хотим получить
    prompt = text

    # URL для генерации: промпт передаётся прямо в адресе
    url = "https://gen.pollinations.ai/image/%s" % quote(text)

    # Параметры генерации
    params = {
        "model": "tongyi-mai/z-image-turbo",  # модель по умолчанию
        "width": 1024,    # ширина изображения
        "height": 1024,   # высота изображения
        "seed": -1       # для повторяемого результата (-1 = случайный)
    }

    # Отправляем GET-запрос: сервер сразу возвращает готовую картинку
    response = requests.get(url, params=params, headers=headers, timeout=120)
    print(response.status_code)

    if response.status_code == 200:
        # Расширение файла берём по типу ответа (jpeg / png / svg)
        content_type = response.headers.get("content-type", "")
        ext = {"image/png": "png", "image/svg+xml": "svg"}.get(content_type, "jpg")

        filename = "cat.%s" % ext
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Картинка сохранена в", filename)
        return filename
        
    else:
        # Текст ошибки: 401 — нет ключа, 402 — кончился баланс, 429 — слишком часто
        return response.text
       


