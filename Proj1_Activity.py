# World 3 - to get freshened up and to be splashed by the water bomb 

def world_3_start(): 

# Welcome the player and give a brief introduction about the activity. 
    print(f"Welcome to the world three, {user_name}. I am Eaindra, who is in charge of this world! \
As the vibe of the festival goes up, you must also be feeling very sweaty and tired. \
Why not freshen yourself up? In this activity, you are to GET HIT by water balloons. \
You will be playing 5 rounds and out of those 5 rounds, you are to be hit at least 3 times by the water balloons. \
Be careful of the balloons with colors! \
It is fine if you get hit by them but you won't want to visit the next world with colors and sweat. \
At the end of this activity, not only will you feel refreshed, you will also be getting 5 coins! \
I will tell you about the cultural design behind this game at the end, so try your best and good luck!!")
    world_3() #Direct them to world_3()

def world_3():
    import random #Import random package to make the water bomb come from random direction
    import time #Import time package to delay the world directory so that the user can take some break.
    global correct_round #Make sure the correct rounds in this function is global.

#Create a list of directions to choose from 
    direction_orig = ['north', 'east', 'west', 'south', 'above', 'left', 'right']
        
#Set the initial values of round and correct rounds. 
    rounds = 1
    correct_round = 0

#Put the game play into a while-loop until they have played 5 rounds. 
    while rounds <= 5: 
#Make a copy of the list to ensure that all the directions are in the list after each loop.
        direction_copy = direction_orig.copy() 
#Choose a random direction out of the list of directions for the water balloon.
        direction1 = random.choice(direction_orig) 
#Remove that direction from the copied list to ensure that none of the colored balloon would have the same direction as water balloon
        direction_copy.remove(direction1) 
#Choose a random direction from the copied list for colored balloons. 
        direction2 = random.choice(direction_copy) 
        direction3 = random.choice(direction_copy)
        direction4 = random.choice(direction_copy)
#Ask the user if they are ready and display the directions that the balloons are coming from.             
        print("Are you ready for the rounds? Let's go!")
        print(f"\
The water balloon is coming from the {direction1}. \
The pink colored balloons are coming from the {direction2}. \
The green balloons are coming from {direction3}. The blue ones are coming from the {direction4}.")

#Ask the user to type in their answer. 
        user_direction = str(input(f"Round {rounds}, which way will you move? (north, east, west, south, above, left, right): "))

#Checking the user's answers in an if-loop
        if user_direction == direction1: 
            print(f"Good job, {user_name}!")
            time.sleep(1) #For user to take a break
            correct_round +=1 #Increase the correct round to 1 when they are correct
        elif (user_direction == direction2) or (user_direction == direction3) or (user_direction == direction4): 
            print("Oh no! You are covered with colors now. Don't get yourself painted, okay?")
        elif user_direction in direction_orig: 
            print("You didn't get hit by anything but you are feeling more tired now.")
        else: 
            print("\
I'm sorry but I cannot understand your input. \
Can you try to give the answer from the choices and with lower case in the next rounds perhaps?")
        rounds +=1 #Add the rounds
    world_3_end() #When the while-loop has ended, direct them to the end of world 3.

#The end of world 3 where the purpose of the game was told, the coins are added to the main program and asked whether they wanted to play bonus round or not. 
def world_3_end(): 
    global coins, bonus_coins #Make sure the coins are not local to the function. 

#The statement for the purpose of the game is assigned to a variable since it will be used twice. 
    purpose_of_game = "This world is based on the water festival that I used to experience in my home country, Myanmar. \
On April 2nd week, 5 days of water festival is celebrated. It is a celebration to welcome the Burmese New Year.\
 It's a national holiday as well so every office and shops are closed (except for restaurants and shopping malls). \
Stages are built all across the city, at the head of the road, and,\
in front of the city hall for everyone to get sprayed by the water. \
It is a festival where you played with water the whole day to get rid of the scorching heat of the summer. \
Not only does it cool the summer heat, getting sprinkled by water also represent \
that you are being cleansed from your demerits as you welcomed the new year. \
Wikipedia would say otherwise, but I grew up knowing of this representation. \
The last day of the festival is the Burmese New Year's day. \
On that day, everyone would cease to play and they would welcome the new year by doing good deeds. \
Since it is in April, I am not able to go back to celebrate so I thought of sharing this culture with you. \
:) I hope you enjoyed it!"

#Ask if the user want to play the bonus round or not. 
    bonus_answer =  str(input("All the 5 rounds have finished. Do you want to play a bonus round? \
You can earn bonus coins if you do. (y/n): "))
# Checking the user's answers for bonus round with an if-loop. 
    if bonus_answer == "y": 
        print(f"Okay. Let the game begin! But before the bonus game begin, let me tell you about the story behind this world. {purpose_of_game}")
        world_3a() #Direct them to the bonus world
    elif bonus_answer == "n":
        print(f'Well, then, let me tell you about the inspiration behind this activity {purpose_of_game}')
#Check if they got hit by the water balloons 3 times.  
        if correct_round == 3: 
            print(f"Congratulations, {user_name}! You have earned 5 coins. Here's also a towel to dry yourself. Good luck with the other worlds!")
            coins += 5 #Add the coins
            corridor() #Direct them to the corridor
        elif correct_round < 3: 
            print("I'm sorry. You have to play the game again.")
            world_3() #Direct them to the game again if they are not hit by the water balloons 3 times. 

# Bonus round to earn bonus coins. 
def world_3a(): 
    global coins, bonus_coins #Make sure the coins are not local to the function.
    import time #Importing the time package for user to take a break. 

# Welcome the user to the bonus round. 
    print(f"Welcome to the bonus round, {user_name}. You will have to answer two personal questions about me. Ready? Here goes!")
    time.sleep(2) #For the user to take a break. 

#Ask the two personal questions. 
    answer1 = int(input("How long does the water festival last? Please answer with an integer number: "))
    answer2 = int(input("For how many days do the people of Myanmar play with water? Please answer with an integer numeber: "))

#Putting the statement in variable since it is being used 3 times.    
    directing_to_corridor = "You are being directed to the main program of the game..."
    
#Checking the user's answer with and if-loop and alocating bonus coins. 
    if answer1 == 5 and answer2 == 4: 
        print(f"Correct! You have earned 2 bonus coin. {directing_to_corridor}")
        time.sleep(2)
        bonus_coins +=2
    elif answer1 != 5 or answer2 !=4: 
        print(f"One of your answer was wrong. You were able to only earn one bonus coins. {directing_to_corridor}")
        bonus_coins +=1
        time.sleep(2)
    elif answer1 != 5 and answer2 != 4: 
        print(f"Both of your answer was wrong. You were not able to earn any bonus coins. :( {directing_to_corridor}")
        time.sleep(2)
        corridor()

user_name = input("What's your name?" )
world_3_start()