import json
import requests

from config import *


def register_team(game):

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
            "field_id": 22062, #telegram
            "value": TELEGRAM_NAME
        }]
    }

    print("\nПроверь данные:") #лишнее
    print(json.dumps(payload, indent=4, ensure_ascii=False))

    confirm = input("\nОтправить регистрацию? (y/n): ")

    if confirm.lower() != "y":
        print("Регистрация отменена")
        return

    url = f"{BASE_URL}/games/records"

    headers = {
        "Accept": "application/json",
        "Origin": "https://beg.quizplease.com",
        "Referer": "https://beg.quizplease.com/"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print("\nHTTP статус:", response.status_code)

    try:
        result = response.json()
    except ValueError:
        print(response.text)
        return

    print(json.dumps(result, indent=4, ensure_ascii=False))

    if result.get("status") == "success":
        data = result["data"]

        print("\nРЕГИСТРАЦИЯ СОЗДАНА!")
        print("ID регистрации:", data["id"])
        print("Название команды:", data["game_team"]["title"])
        print("Токен регистрации:", data["public_token"])
        print("Количество мест:", data["seats"]["seats_total"])
        print("Свободных мест:", data["seats"]["seats_free"])
    else:
        print("\nНе удалось зарегистрировать команду")