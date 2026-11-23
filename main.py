from game_info import get_games, show_games
from registration import register_team



def main():

    games = get_games()

    if not games:
        print("Игры не найдены")
        return

    show_games(games)

    try:
        choices = input(
            "\nВведи номера игр через пробел (например: 1 3 5): "
        )
        choices = [int(x.strip()) for x in choices.split(" ")]

    except ValueError:
        print("Нужно вводить числа через пробел")
        return

    # Проверяем номера
    if any(choice < 1 or choice > len(games) for choice in choices):
        print("Один или несколько номеров указаны неверно")
        return

    # Убираем дубликаты, сохраняя порядок
    choices = list(dict.fromkeys(choices))

    for choice in choices:

            selected_game = games[choice - 1]

            print("\n" + "=" * 40)
            print("Выбрана игра:")
            print(selected_game["title"], "#", selected_game["game_number"], sep='')
            print(selected_game["date"])

            confirm = input("Перейти к регистрации? (y/n): ")

            if confirm.lower() == "y":
                register_team(selected_game)
            else:
                print("Регистрация пропущена")

    print("\nОбработка выбранных игр завершена")


if __name__ == "__main__":
    main()