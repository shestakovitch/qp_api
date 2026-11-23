import requests


BASE_URL = "https://api.quizplease.ru/api"

# --------------------------------------------------
# 1. Получение расписания Белграда
# --------------------------------------------------

def get_games():
    url = f"{BASE_URL}/games/schedule/163"

    response = requests.get(url)
    response.raise_for_status()

    result = response.json()

    if result["status"] != "ok":
        print("Ошибка получения расписания")
        return []

    return result["data"]["data"]

def show_games(games):
    print("\nРАСПИСАНИЕ QUIZ PLEASE — БЕЛГРАД")
    print("=" * 55)

    for index, game in enumerate(games, start=1):
        print(f"\n{index}. {game['title']} #{game['game_number']}")
        print(f"Дата: {game['date']}")
        print(f"Место: {game['place']['title']}")
        print(f"Адрес: {game['place']['address']}")
        print(f"Цена: {game['current_price']} дин.")
        print(f"Свободные места: {game['people_have_places_to_reserve']}")
        print(f"Ссылка: {game['link_short']}")
        print(f"ID игры: {game['id']}")

    print("\n" + "=" * 55)