print("Enter 3 number as Hour & minute & second:")
hour = int(input())
min = int(input())
sec = int(input())

second = hour * 3600 + min * 60 + sec
print("Result of your time is :", second, "seconds")

print("Enter seconds:")
seconds = int(input())
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec1 = (seconds % 3600) % 60


print("Your time is:    ", hours,":",minutes,":",sec1)
