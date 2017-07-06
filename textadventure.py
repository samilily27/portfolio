#variables
name=""
Join=""
petdog=""
feed=""
bite=""
restart=""
playgame=""

#intro,ask for name, whether they want to continue
# if no restart the program
print ("Hi stranger! My name is Bob.")
name=input("What's your name?")
print ("Hi "+ name + "!")
Join = input("Would you like to join me?")
if Join == "yes" or Join=="Yes" or Join=="YES":
  print("Great! Let's go!I see a dog up ahead!")
else:
  print ("Sorry for asking...")
  exit()

#encounter with the dog - no
petdog=input("Should we pet the dog?")
if petdog == "yes" or petdog=="Yes" or petdog=="YES":
    print("Aw he is so cute!")
    print("Haha he's barking")
else:
    print ("He's chasing me!!!!")
    print("A cliff is approaching. He's cornered us. We should've pet the dog.")
    print("*falls off*")
    exit() 

#see goose - no
print("I see a gooose! Let's go to the pond?")
feed = input("Should we feed the goose?")
if feed == "yes" or feed =="Yes" or feed=="YES":
    print("aww the goose loves the food!")
else:
    print ("owww!! it bit me:(")
    bite = input("does it look infected?")
    if  bite== "yes" or bite=="Yes" or bite=="YES":
        print("Let's go to the hospital!")
        print("I'm okay! Let's go on another hike soon.")
        print("See ya...")
        exit()
    else:
        print ("*continues walking..falls..dies*")
        print("You could've helped him")
        exit() 

#leads to happy ending with animal tips
print("Hey it's getting late.")
playgame=input("Do you want to play a game?")
if playgame == "yes" or playgame =="Yes" or playgame=="YES":
    print("I'm thinking of a number 1 to 20")
    #game
    
    import random 
    attempts = 1
    bobsnumber = random.randint(1,20)
    isCorrect = False
    guess = int(input("Take a guess: "))
    while  bobsnumber != guess and attempts < 6:
        if guess <  bobsnumber:
            print("Higher...")
        elif guess > bobsnumber:
            print("Lower...")
        guess = int(input("Take a guess: "))
        attempts = attempts + 1
    if attempts == 6:
        print("\nSorry you reached the maximum number of tries")
        print("The secret number was ", bobsnumber) 
    else:
        print("\nYou guessed it! The number was " , bobsnumber)
        print("You guessed it in ", attempts,"attempts")
        
    #game

    print("Good game.  What a long day!")
    print("See ya later")
    exit()
        
else:
    print ("Awww well see you later.")
    exit()
        
