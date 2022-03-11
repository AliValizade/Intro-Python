print("Enter your weight in kg:")
weight = float(input())
print("Enter your height in meters:")
height = float(input())

BMI = weight / height**2

if BMI < 18.5:
    print("You are Thin")
elif 18.5 < BMI < 24.9:
    print("YOu are Normal")
elif 25 < BMI < 29.9:
    print("You are OverWeight")
elif 30 < BMI < 34.9:
    print("You are Fat")
elif 35 < BMI < 39.9:
    print("You are Very Fat")
else:
    print("Number wrong")