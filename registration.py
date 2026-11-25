import json
import requests

from config import *
from logger import setup_logging
from sender import send_message

logger = setup_logging()


def register_team(game):
    logger.info("Начало регистрации команды. ID игры: %s", game["id"])

    print("\nРЕГИСТРАЦИЯ КОМАНДЫ")
    print("=" * 40)

    payload = {
        "title": TITLE,
        "captain": CAPTAIN,
        "phone": PHONE,
        "email": EMAIL,
        "comment": "",
        "people_count": PEOPLE_COUNT,
        "is_open_for_players": False,
        "joined_to_public_token": None,
        "count_paid": 0,
        "birthday_names": "",
        "is_first": False,
        "is_pay_now": False,
        "is_send_email": True,
        "is_personal_data_consent": True,
        "is_marketing_consent": False,
        "promo_ids": [],
        "certificate_ids": [],
        "payment_method": "cash",
        "table_size": None,
        "game_id": game["id"],
        "utm": {},
        "custom_fields": [{
            "field_id": 22062,  # telegram
            "value": TELEGRAM_NAME
        }]
    }

    url = f"{BASE_URL}/games/records"

    headers = {
        "Accept": "application/json",
        "Origin": "https://beg.quizplease.com",
        "Referer": "https://beg.quizplease.com/"
    }

    logger.info("Отправка запроса на регистрацию. ID игры: %s", game["id"])

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers
        )
    except requests.RequestException:
        logger.exception("Ошибка HTTP-запроса при регистрации. ID игры: %s", game["id"])
        print("\nОшибка отправки запроса")

        try:
            send_message(
                f"❌ Ошибка регистрации команды {TITLE}\n"
                f"ID игры: {game['id']}\n"
                f"Не удалось отправить запрос к API."
            )
        except requests.RequestException:
            logger.exception("Ошибка отправки уведомления в Telegram")

        return

    logger.info("Получен ответ API. HTTP статус: %s", response.status_code)

    print("\nHTTP статус:", response.status_code)

    try:
        result = response.json()
    except ValueError:
        logger.error("Не удалось разобрать JSON-ответ API. HTTP статус: %s", response.status_code)
        print(response.text)
        return

    print(json.dumps(result, indent=4, ensure_ascii=False))

    if result.get("status") == "success":
        data = result["data"]

        logger.info(
            "Регистрация успешно создана. ID регистрации: %s, ID игры: %s",
            data["id"],
            game["id"]
        )

        print("\nРЕГИСТРАЦИЯ СОЗДАНА!")

        message = (
            "Вы зарегистрировались на игру:\n\n"
            f"{game['title']} #{game['game_number']}\n"
            f"Дата: {game['date']}\n"
            f"Место: {game['place']['title']}\n"
            f"Адрес: {game['place']['address']}\n"
            f"Цена: {game['current_price']} дин."
        )

        try:
            send_message(message)
        except requests.RequestException:
            logger.exception("Ошибка отправки уведомления о регистрации в Telegram")

    else:
        error_message = result.get("message", "Причина не указана")

        logger.warning(
            "Не удалось зарегистрировать команду. ID игры: %s. Ответ API: %s",
            game["id"],
            error_message
        )

        print("\nНе удалось зарегистрировать команду")

        try:
            send_message(
                f"❌ Не удалось зарегистрировать команду {TITLE}\n"
                f"ID игры: {game['id']}\n"
                f"Причина: {error_message}"
            )
        except requests.RequestException:
            logger.exception("Ошибка отправки уведомления об ошибке регистрации в Telegram")
