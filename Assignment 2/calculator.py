import math
while True:
    op = input()
    if op == "exit":
        break
    elif op == "sin" or op == "log" or op == "tan" or op == "cot" or op == "factorial":
        a = int(input())
    else:        
        a = int(input())
        b = int(input())

    if op == "+":
        result = a + b

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        if b != 0:
            result = a / b
        else:
            result = "Can't divid by zero"

    elif op == "^":
        result = a ** b

    elif op == "sin":
        result = math.sin(a)

    elif op == "log":
        result = math.log10(a)

    elif op == "tan":
        result = math.tan(a)

    elif op == "cot":
        if math.tan(a) != 0:
            result = 1 / math.tan(a)
        else:
            result = "Cot can't be calculated "

    elif op == "factorial":
        result = math.factorial(a)


    else:
        result = "Unknown Error"

    print(result)
