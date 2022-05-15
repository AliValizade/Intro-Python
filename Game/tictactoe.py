def check():
    if game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X":
        print("Player 1 win")

game = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]
for row in game:
    print(row)

while True:    
    print("Player 1")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0 <= col <=2:
            if game[row][col] == " ":
                game[row][col] = "X"
                break
            else:
                print("try again")
        else:
            print("not in range")
    for row in game:
            print(row)
            check()
    print("Player 2")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0 <= col <=2:
            if game[row][col] == " ":
                game[row][col] = "O"
                break
            else:
                print("try again")
        else:
            print("not in range")
    for row in game:
            print(row)
            check()