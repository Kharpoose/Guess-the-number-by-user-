import random


def computer_guess(x):
    high = x
    low = 1
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            gues = low 
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (H), too low (L) or correct (C) ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

    print(f"yeyy I guessed right {guess} is correct number!!")


computer_guess(50)