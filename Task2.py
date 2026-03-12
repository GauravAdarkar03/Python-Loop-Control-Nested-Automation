print("\n----- Tournament Matches -----")

tournament = [
    ["Player_A1", "Player_A2", "Player_A3"],  # Advanced
    ["Player_B1", "Player_B2", "Player_B3"],  # Beginner
    ["Player_I1", "Player_I2", "Player_I3"]   # Intermediate
]

stop_tournament = False

for group in tournament:
    for i in range(len(group)-1):
        player1 = group[i]
        player2 = group[i+1]

        print(f"Match: {player1} vs {player2}")

        if "I2" in player1 or "I2" in player2:
            print("Tournament player - found")
            stop_tournament = True
            break
