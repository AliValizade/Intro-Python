import random

rand_number = random.randint(0, 40)
num_of_guess = 1
while True:
    
    user_number = int(input())

    if user_number == rand_number:
        print("💖💖💖💖💖✅Congratulation✅💖💖💖💖💖")
        break

    elif user_number < rand_number:
        print("😌 Go Up ⏫")

    elif user_number > rand_number:
        print("😌 Go Down ⏬")
    num_of_guess += 1

print("Number of your guesses is:", num_of_guess)
print("End of game, Come back soon🕛")

