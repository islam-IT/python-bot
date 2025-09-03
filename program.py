import random

number = random.randint(1, 10)
guess = None

print("Угадай число от 1 до 10!")

while guess != number:
    guess = int(input("Введи число: "))
    if guess < number:
        print("Слишком мало!")
    elif guess > number:
        print("Слишком много!")

print("Ты угадал!")