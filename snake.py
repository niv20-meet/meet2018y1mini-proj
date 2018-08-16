
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random

turtle.tracer(1, 0)  # This helps the turtle move more smoothly

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)  # Curious? It's the turtle window
# size.
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

# Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

# Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

# Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

# Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the
#snake(i.e.START_LENGTH)
for snke in range (START_LENGTH):
    x_pos = snake.pos()[0]# Get x-position with snake.pos()[0]
    y_pos = snake.pos()[1]

    # Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    # You're RIGHT!
    x_pos +=SQUARE_SIZE
    my_pos = (x_pos, y_pos)  # Store position variables in a tuple
    snake.goto(x_pos,y_pos)  # Move snake to new (x,y)

    # Append the new position tuple to pos_list
    pos_list.append(my_pos)

    # Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)

###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up"  # Make sure you pay attention to upper and lower
# case
LEFT_ARROW = "Left"  # Pay attention to upper and lower case
DOWN_ARROW = "Down"  # Pay attention to upper and lower case
RIGHT_ARROW = "Right"  # Pay attention to upper and lower case
TIME_STEP = 50  # Update snake position after this many
# milliseconds
SPACEBAR = "space"  # Careful, it's not supposed to be capitalized!
RIGHT = 2
DOWN = 1
UP = 0
LEFT = 3
# 1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    global direction  # snake direction is global (same everywhere)
    direction = UP  # Change direction to up
   # Update the snake drawing <- remember me later
    print("You pressed the up key!")

def down():
    global direction  # snake direction is global (same everywhere)
    direction = DOWN  # Change direction to up
     # Update the snake drawing <- remember me later
    print("You pressed the up key!")

def Left():
    global direction  # snake direction is global (same everywhere)
    direction = LEFT  # Change direction to up
      # Update the snake drawing <- remember me later
    print("You pressed the Left key!")

def Right():
    global direction  # snake direction is global (same everywhere)
    direction = RIGHT # Change direction to up
    # Update the snake drawing <- remember me later
    print("You pressed the Right key!")

# 2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW)  # Create listener for up key
turtle.onkeypress(Left, LEFT_ARROW)
turtle.onkeypress(Right,RIGHT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)

# 3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction== UP:
        snake.goto (x_pos,y_pos+SQUARE_SIZE)
    elif direction == DOWN:
        snake.goto (x_pos,y_pos-SQUARE_SIZE)


      
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    #HINT: This if statement may be useful for Part 8

  
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of functio


    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    
    # pop zeroth element in pos_list to get rid of last the last
    # piece of the tail
    print(snake.pos())
    print(pos_list)
    if snake.pos() in pos_list[0:-1]:
            print ("game over j")
            quit()  

    #Add new lines to the end of the function
    #Grab position of snake


    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the
    
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the edge! you stupid ass hole Game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the edge! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the edge! Game over!")
        quit()
    
    elif new_y_pos <= DOWN_EDGE:

        print("You hit the edge! Game over!")
        quit()
    if len(food_stamps) <= 6 :
                make_food()
    # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    stampid=food.stamp()
    food_stamps.append(stampid) 







   


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
        ##                        position 
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
move_snake()

