# string interpolation => formatting strings

userName = "Sara"
userFamily = "Moradi"
number_1 = 3
number_2 = 5

result = "user name is " + userName + " and user family is " + userFamily
print(result)
result2 = f"user name is {userName} and user family is {userFamily}"
print(result2)
print("user name is", userName, "and user family is", userFamily)

print(f"Sum is : {number_1 + number_2}")

# string index

print(userName[2])

