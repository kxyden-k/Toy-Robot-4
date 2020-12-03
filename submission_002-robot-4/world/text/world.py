from world import obstacles

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def print_obstacles():
    """
    prints the positions of obstacles
    """
    #lst = obstacles.obstacle_lst
    if obstacles.create_obstacles() == []:
        return None
    elif obstacles.create_obstacles() != []:
        print("There are some obstacles:")
        for i in range(len(obstacles.obstacle_lst)):
            tup = obstacles.obstacle_lst[i]
            x = tup[0]
            y = tup[1]
            print("- At position "+str(x)+","+str(y)+" (to "+str(x+4)+","+str(y+4)+")")


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
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

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
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
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