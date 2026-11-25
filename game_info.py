import logging
import requests
from config import BASE_URL

logger = logging.getLogger("qp_api")


def get_games():
    """
    Получение расписания Белграда
    """

    url = f"{BASE_URL}/games/schedule/163"

    logger.info("Запрос расписания игр Белграда")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        result = response.json()

        if result["status"] != "ok":
            logger.error("API вернул ошибку при получении расписания")
            print("Ошибка получения расписания")
            return []

        games = result["data"]["data"]

        logger.info("Получено игр: %s", len(games))

        return games

    except requests.exceptions.RequestException:
        logger.exception("Ошибка HTTP-запроса при получении расписания")
        return []

    except (ValueError, KeyError, TypeError):
        logger.exception("Ошибка обработки ответа API")
        return []


def show_games(games):
    logger.info("Вывод расписания игр в консоль")

    print("\nРАСПИСАНИЕ QUIZ PLEASE — БЕЛГРАД")
    print("=" * 65)

    for index, game in enumerate(games, start=1):
        print(f"\n{index}. {game['title']} #{game['game_number']}")
        print(f"Дата: {game['date']}")
        print(f"Место: {game['place']['title']}")
        print(f"Адрес: {game['place']['address']}")
        print(f"Цена: {game['current_price']} дин.")

    print("\n" + "=" * 65)

    logger.info("Расписание выведено в консоль")
