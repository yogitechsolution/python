#Guess number program!

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break 
else: # It will execute only when 1st while cond executed successfully without reaching break
    print("Sorry, You failed!")


#Guess: 1
#Guess: 2
#Guess: 3

#Guess: 9
#You won!
#Guess: 1
#Guess: 2

#Guess: 9   ----because of adding break
#You won!

#Guess: 1  ---After adding else part of while loop
#Guess: 2
#Guess: 3
#Sorry, You failed!