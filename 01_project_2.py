print(
'''
                                        ****************GUESS THE NUMBER GAME*****************
                                         Rules:
                                         Here you have to guess a number that already guessed
                                         by the computer automatically. 
                                         If the number you guessed is same as the number that 
                                         computer guessed already then you will win.

                                            **The lower the guesses the higher the score** 
                                            **The higher the guesses the lower the score** 

                                        ****************************************************** 


'''
)

import random
a=0
b=100
# this function generates number from a to b once at time
random_number=random.randint(a,b)

guess_number_by_user=None
guesses=0


while (guess_number_by_user != random_number):

    print("****************************")
    guess_number_by_user=int(input("\nGuess the number: "))
# this counts the number of guesses 
    guesses+=1
    if guess_number_by_user>random_number:
        print("**Guess lower number please\n")

    if guess_number_by_user<random_number:
        print("**Guess higher number please\n")

    if guess_number_by_user==random_number:
        print("**Perfect guess!!\n")

# this shows the total guesses after winning
print(f"**You guessed the number in {guesses} guesses")

# Read and Write the high score.txt
with open("high score.txt", "r") as f:
    score = f.read()

if score == "":
    with open("high score.txt", "w") as f:
        f.write(str(guesses))

elif score<str(guesses):
     with open("high score.txt", "w") as f:
        f.write(str(guesses))



