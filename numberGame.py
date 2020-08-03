import random
number = random.randint(1,20)

print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
print('DEBUG: Secret number is ' + str(number))
for i in range(1,7):
    if i == 6:
        print('Nope. The number I was thinking of was ' + str(number))
    else:
        print('Take a guess')
        guess = input()

        try:
            if int(guess) == number and i == 1:
                print('Impressive, ' + name + '! The number was ' + str(number) + ' and \
you guessed it on the first try!')
                break
            elif int(guess) == number:
                print('Good job, ' + name + '! The number was ' + str(number) + ' and you \
guessed it in ' + str(i) + ' tries.')
                break
            elif int(guess) < number:
                print('Your guess is too low. Tries left: ' + str(6-i) + '.')
            else:
                print('Your guess is too high. Tries left: ' + str(6-i) + '.')
        except:
            print('You did not enter a number. Tries left: ' + str(6-i) + '.')
