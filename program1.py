import random

print('**********************************************')
print('             Number Game                      ')
print('**********************************************')
print('')

the_number = random.randint(0, 100)
guess = -1
name = input(str(' Player, what is your name ? '))
while guess != the_number:
    guess_text = input(' Guess Text between 0 & 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print(' Hello {} Number you entered  {} low' .format(name, guess))
    elif guess > the_number:
        print(' Hello {} Number you entered  {} high' .format(name, guess))
    else:
        print(' Hello {}  you win.  Number you entered  {} = Random number {} ' .format(name, guess,the_number))
