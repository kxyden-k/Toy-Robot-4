import turtle
from world import obstacles

def create_screen():
    wn = turtle.Screen()
    wn.bgcolor("white")
    sc = turtle.Screen() 
    wn.mode('world') 
    wn.setworldcoordinates(-300,-300,300,300)
    wn.setup(500, 700)

def create_outline():
    outline = turtle.Turtle()
    outline.speed(20)
    outline.hideturtle()
    outline.penup()
    outline.setposition(100,200)
    outline.pendown()
    outline.color("red")
    outline.pensize(3)
    outline.right(90)
    outline.forward(400)
    outline.right(90)
    outline.forward(200)
    outline.right(90)
    outline.forward(400)
    outline.right(90)
    outline.forward(200)
    outline.penup()

dave = 0

def create_turtle():
    global dave
    dave = turtle.Turtle()
    dave.penup()
    dave.left(90)
    dave.setposition(0,0)

def create_obstacles():
    place_obstacles = turtle.Turtle()
    place_obstacles.hideturtle()
    place_obstacles.speed(20)
    place_obstacles.color("red")
    place_obstacles.penup()
    lst = obstacles.create_obstacles()
    for i in range(len(lst)):
        tup = lst[i]
        place_obstacles.setposition(tup[0],tup[1])
        place_obstacles.pendown()
        place_obstacles.begin_fill()
        for i in range(4):
            place_obstacles.forward(4)
            place_obstacles.left(90)
        place_obstacles.end_fill()
        place_obstacles.penup()



# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100



def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_position_blocked(new_x, new_y) or obstacles.is_path_blocked(position_x,position_y,new_x,new_y):
        return False
    elif is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def show_position(robot_name):
    # print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    pass

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        dave.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        if obstacles.obst_check == False:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
        elif obstacles.obst_check == True:
            return True, ''+robot_name+': Sorry, there is an obstacle in the way.'

def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        dave.backward(steps)
        return True,  ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        if obstacles.obst_check == False:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
        elif obstacles.obst_check == True:
            return True, ''+robot_name+': Sorry, there is an obstacle in the way.'

def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    dave.right(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    dave.left(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def reset_globals():
    """resets global variables for test cases"""
    global current_direction_index,position_x,position_y
    current_direction_index = 0
    position_x = 0
    position_y = 0
    obstacles.obstacle_lst = []

