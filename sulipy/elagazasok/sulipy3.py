import random
def guess_number():
    num = random.randint(1, 5)
    num_guess = int(input("Guess a number between 1 and 5: "))
    if num == num_guess:
        print("You guessed correctly!")
    elif num < num_guess:
        print("Your guess was too high!")
    else:
        print("Your guess was too low!3")
    


guess_number()
