def summ(a, b):
    return a + b


def multyply(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow(a, q):
    return a ** q



print("Введите первое число")

a = int(input())

print("Введите второе число")

b = int(input())

print("Введите операцию")

operation = str(input())

if str == "+":
    print(summ(a, b))

if str == "-":
    print(summ(a, -b))

if str == "*":
    print(multyply(a, b))
    
if str == "/":
    print(divide(a, b))

if str == "^":
    print(pow(a, b))