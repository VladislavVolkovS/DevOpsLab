from functions import *

print("Введите первое число")

a = int(input())

print("Введите второе число")

b = int(input())

print("Введите операцию")

operation = str(input())

if operation == "+":
    print(summ(a, b))

if operation == "-":
    print(summ(a, -b))

if operation == "*":
    print(multyply(a, b))
    
if operation == "/":
    print(divide(a, b))

if operation == "^":
    print(pow(a, b))