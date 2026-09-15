#Python random number Guessing game
import random

guesses = 0
is_running = True

print("====Welcome to Predictor====")
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
num = random.randint(low,high)
print(f"Select a Number between {low} and {high}: ")
while is_running :
    guess = int(input("Guess: "))
    guesses += 1
    if num == guess:
        print("================================")
        print(" Ohoi Captain, you guessed it !")
        print(f"        Total guesses: {guesses}   ")
        print("================================")
        break
    else:
        print("-----Incorrect Guess------")

