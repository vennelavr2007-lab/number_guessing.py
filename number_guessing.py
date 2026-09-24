import random
number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
if guess == number:
    print("Correct! You won!")
else:
    print("Wrong! The number was", number)

OUTPUT:
Guess a number (1-10): 6
Wrong! The number was 10
