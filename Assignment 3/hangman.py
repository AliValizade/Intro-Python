import random
word_bank = ["book", "moon", "tree", "sadjad", "university", "python", "c++", "apple", "corona"]

# i = random.randint(0, len(word_bank)-1)
# word = word_bank[i]

word = random.choice(word_bank)

user_correct_chars = []
joon = 6

while True:
    for i in range(len(word)):
        if word[i] in user_correct_chars:
            print(word[i], end="")
        else:
            print("-", end="")

    print("\n Please enter a character")
    user_char = input()
    if user_char in word:
        user_correct_chars.append(user_char)
        print("✅")

    else:
        joon = joon -1
        print("⚡")

    # if lost
    if joon == 0:
        print("Game Over ⛔")
        break

    # if won
    if len(word) == len(user_correct_chars):
        print("Congratulation💥, You won✅")
        break