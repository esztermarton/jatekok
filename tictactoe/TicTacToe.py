from GameSetup import setup_game, new_game
from OneRound import play_round
from GameUtils import print_board

# print_board(game_configuration["board"])
result = {
    "game_state": "",
    "message": ""
}
play = True
print("success 1")
while play:
    print("success 2")

    result["game_state"] = False
    print("success 3")

    game, player1, player2 = setup_game()
    print("success 4")

    while not result["game_state"]:
        print("success 5")
        result = play_round(game, player1, player2)
        print("success 6")

    print(result["message"])
    play = new_game()

