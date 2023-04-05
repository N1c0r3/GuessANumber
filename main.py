import random  #Needed to generate a random number
import winsound #For sounds
import time #to set a timer
import sys #needed because sys.exit() had to be used at one point instead of break


def start(): # Function to start or exit the game
    Start = input("Start game? Y/N: " ) #Ask the user for an input
    if Start == "Y":
        game()    #Input "Y" starts game() function
    elif Start == "N":
        print("See you next time")  #Input "N" prints message and no further code is called


def game(): # This function contains the game itself
    r = random.randrange(1, 100) #Generates a random int between 1 and 100
    counter = 1 #Sets counter for tries to one because the winning try wont be counted later
    print("Guess a number between 1 and 100. You have 60 Seconds! Type Quit to exit at any time \nThe Game will start in a few Seconds..")
    time.sleep(5) #No further code will be called for 5 Seconds to give the user time to read the Instructions
    timer = 60 #Sets the timer for the game to 60 seconds
    currenttime = time.time() #Returns seconds passed since Jan. 1st 1970
    while True:
        inp = input("Enter your number:") #Ask the User to enter a guess

        if time.time() > currenttime + timer: #Calls start() Function if the timer is exceeded
            print("Time is up")
            start()

        if inp.casefold() =="quit": #Quits the program with sys.exit when typing Quit or quit
            print("See you next time!")
            sys.exit()

        try:  #Checks user input for integer if not a Error message is shown
           a = int(inp)
        except ValueError:
           print("Please enter a valid number")
           continue

        if int(a) > 100: #Prints a notification when a number higher than 100 is entered
            print("Please Enter a number between 1 and 100")
        elif int(a) < r: #Plays a sound and tells the user that the number is to low. Also sets counter +1
            winsound.PlaySound("lost", winsound.SND_FILENAME)
            print("Your number is to low. Try higher")
            counter = counter + 1
        elif int(a) > r: #Plays a sound and tells the user that the number is to high. Also sets counter +1
            winsound.PlaySound("lost", winsound.SND_FILENAME)
            print("Your Number is to high. Try lower")
            counter = counter + 1
        else: #Plays the sound for winning, Shows the user the amount of tries and calls the start() function again
            winsound.PlaySound("win", winsound.SND_FILENAME)
            print("Congratulations! You guessed the number with {} tries.".format(counter))
            start()

start()