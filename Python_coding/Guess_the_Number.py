import random
guess_made = 0
name = input(' hello ! What is your Name ? \n')
number =random.randint(1, 20)
print ('Well, {0} , i am thinking of a number between 1 and 20. '.format(name))
while guess_made < 6:
  guess = int(input('Take a guess: '))
  guess_made += 1
  if guess < number :
    print ('Your guess is too low')
  if guess > number:
    print ("Your guess is too high")
  if guess == number:
    break
if guess == number:
  print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guess_made))
else:
  print ('Nope. The number I was thinking of was {0}'.format(number))