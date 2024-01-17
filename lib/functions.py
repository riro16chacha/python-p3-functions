#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()
def greet(name):
    print(f"Hello, {name}!")
    
user_name = "Chacha"
greet(user_name)
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

programmer_name = "Peter"
greet_with_default(programmer_name)
greet_with_default()
def add(num1, num2):
    return num1 + num2
result = add(2, 2)
print(result)

def halve(number):
    return number / 2
answer = halve(10)
print(answer)
