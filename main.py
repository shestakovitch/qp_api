from game_info import get_games, show_games
from registration import register_team
from logger import setup_logging


def main():
    logger = setup_logging()

    logger.info("Программа запущена")

    games = get_games()

    if not games:
        logger.warning("Игры не найдены")
        print("Игры не найдены")
        return

    show_games(games)

    try:
        choices = input(
            "\nВведи номера игр через пробел (например: 1 3 5): "
        )
        choices = [int(x) for x in choices.split()]

    except ValueError:
        logger.warning("Пользователь ввёл некорректные номера игр")
        print("Нужно вводить числа через пробел")
        return

    # Проверяем номера
    if any(choice < 1 or choice > len(games) for choice in choices):
        logger.warning("Введены номера игр вне допустимого диапазона: %s", choices)
        print("Один или несколько номеров указаны неверно")
        return

    # Убираем дубликаты, сохраняя порядок
    choices = list(dict.fromkeys(choices))

    logger.info("Выбраны номера игр: %s", choices)

    for choice in choices:

        selected_game = games[choice - 1]

        game_title = selected_game["title"]
        game_number = selected_game["game_number"]
        game_date = selected_game["date"]

        logger.info(
            "Выбрана игра: %s #%s, дата: %s",
            game_title,
            game_number,
            game_date
        )

        print("\n" + "=" * 65)
        print("Выбрана игра:")
        print(game_title, "#", game_number, sep='')
        print(game_date)

        confirm = input("Перейти к регистрации? (y/n): ")

        if confirm.lower() == "y":
            logger.info("Начата регистрация на игру #%s", game_number)

            try:
                register_team(selected_game)
                logger.info("Регистрация на игру #%s завершена", game_number)

            except Exception:
                logger.exception(
                    "Ошибка при регистрации на игру #%s",
                    game_number
                )

        else:
            logger.info("Регистрация на игру #%s пропущена", game_number)
            print("Регистрация пропущена")

    logger.info("Обработка выбранных игр завершена")
    print("\nОбработка выбранных игр завершена")


if __name__ == "__main__":
    main()