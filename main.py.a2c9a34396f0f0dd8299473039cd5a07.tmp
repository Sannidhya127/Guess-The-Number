import random


print("Welcome to Guess The Number!.... You get 5 chances to guess a number between 0 to hundred with hints in between. If you guess it correct, you win, or else you are looser!!.\nReadyyyy!!!!!!")

numbers = list(range(0, 101))

RandomNumber = random.choice(numbers)
for i in range(5):
    num = int(input("Enter the number you guessed: "))
    if num == RandomNumber:
        print("You won the game!!")
        break
    elif num > RandomNumber:
        print("Try a smaller number")
    elif num < RandomNumber:
        print("Try a greater number")
    elif num > 100:
        print("The number is lesser than 100")
    else:
        pass
