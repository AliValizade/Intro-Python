for i in range(20):
    print('i love you', i)
print(list(range(10)))
print(list(range(3, 10,)))
print(list(range(3, 10, 2)))

fruits = ["apple", "banana", "kiwi", "orange", "peach", "cherry", "mango", "strawberry"]

for j in range(len(fruits)):
    print(fruits[j], j)

name = "Ali"
print(len(name))

for j in range(len(fruits)):
    if len(fruits[j]) == 5:
        print(fruits[j], j)

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if 'y' in fruit:
        print("y:", fruit)

friends = ["ALi", "Reza", "Zari", "Pari"]
print(friends)

animals = ["🦄", "🐔", ""]