import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is the {guess} too high(H), too Low(L) or Correct(C)??').lower()
        if feedback=='h':
            high=guess -1
        elif feedback=='l':
            low=guess+1
    print("The computer has gussed the number")

computer_guess(100)


