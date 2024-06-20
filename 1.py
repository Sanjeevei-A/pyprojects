import random
def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while guess != random_number:
        guess =int( input(f'Guess a Number between {x}:'))
        print(guess)
        if guess<random_number:
            print("You are too low!")
        elif guess>random_number:
            print("You are too high!")
        else:
            print(f"Horray! you have found the answer.The answer is  {random_number}")
            

guess(1)

