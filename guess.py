import random
ans = random.randint(0,10)
tries = 0
while tries < 3:
    guess = int(input('Enter your guess:'))

    if guess == ans:
        print('You guessed right!!')
        break
    else:
        print('Wrong guess.')

    tries += 1
