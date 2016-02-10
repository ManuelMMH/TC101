import random

num=int(input("Guess the number: "))
r=int(num*random.random())+1

while num!=r:

    if num>r:
        print("The number is lower ,try again.")
        num=int(input("Guess the number: "))

    elif num<r:
        print("The number is higher ,try again.")
        num=int(input("Guess the number: "))

print("Nice! You guessed the number.")
