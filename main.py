from game_info import get_games, show_games



def main():

    games = get_games()

    if not games:
        print("Игры не найдены")
        return

    show_games(games)

    # try:
    #     choice = int(input("\nВыбери номер игры: "))
    # except ValueError:
    #     print("Нужно ввести число")
    #     return
    #
    # if choice < 1 or choice > len(games):
    #     print("Неверный номер игры")
    #     return
    #
    # selected_game = games[choice - 1]
    #
    # print("\nВыбрана игра:")
    # print(selected_game["title"])
    # print(selected_game["date"])
    #
    # confirm = input("Перейти к регистрации? (y/n): ")
    #
    # if confirm.lower() == "y":
    #     register_team(selected_game)


if __name__ == "__main__":
    main()