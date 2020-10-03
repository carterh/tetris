def static_game():
    game_row = [0 for i in range(10)]
    game = [game_row for i in range(20)]
    game[0][0:4] = [1,1,3,1]
    return game

print(str(static_game()))
