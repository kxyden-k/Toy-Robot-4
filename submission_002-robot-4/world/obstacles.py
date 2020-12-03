import random

obstacle_lst = []
obst_check = False
def create_obstacles():
    """
    Randomizes the amount and position of obstacles
    """
    global obstacle_lst
    
    obstacle_lst = [(random.randint(-99,99), random.randint(-199, 199)) for i in range(random.randint(1,10))]
    return obstacle_lst


def is_position_blocked(x,y):
    """
    Makes sure robot cannot occupy the same space as the robot
    """
    global obst_check
    for i in range(len(obstacle_lst)):
        x_check = obstacle_lst[i][0]
        y_check = obstacle_lst[i][1]
        if y_check <= y <= (y_check + 4) and x_check <= x <= (x_check + 4):
            obst_check = True
            return True
    obst_check = False
    return False

def is_path_blocked(x1, y1, x2, y2):
    """
    -Blocks the robot from skipping the obstacles
    -Returns true if there is an obstacles
    """
    global obstacle_lst
    global obst_check
    obst_check = True
    for i in obstacle_lst:
        obs_x = i[0]
        obs_y = i[1]
        if x1 == x2 and (obs_x <= x1 and x1 <= obs_x + 4):
            if y2 < obs_y:
                return y1 >= obs_y
            elif y2 > obs_y + 4:
                return y1 <= obs_y + 4
        elif y1 == y2 and (obs_y <= y1 and y1 <= obs_y + 4):
            if x2 < obs_x:
                return x1 >= obs_x
            elif x2 > obs_x + 4:
                return x1 <= obs_x + 4
    obst_check = False
    return False
