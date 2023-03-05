from random import randint 

number = randint(1,100)
done = 0
guesses = 0

guess = input("guess the number: ")

while done<1:

    if int(guess) == int(number):
        
        guesses = guesses+1    
        print("good job, u got it in " + str(guesses) + " goes")
        done = 1
            
    else:
            
        if int(guess) > int(number):
            print("guess was too big")
        if int(guess) < int(number):
            print("guess was too smoll")

        guesses = guesses+1
        guess = input("\nguess the number: 
