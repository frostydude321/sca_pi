import random
i = 0

while i < 10:
    random_number = random.randint(1,10)
    guessed_number = int(raw_input("Guess an integer (between 1 and 10): "))
    print 'random_number is ', random_number
    if guessed_number != random_number:
                    print 'Your guess was not correct. Please try again'
 
