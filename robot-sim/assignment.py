from __future__ import print_function

import time
from sr.robot import *

R = Robot()



    
a_th = 2.0 # The threshold for controlling the linear distance
d_th = 0.4 # The threshold for controlling the orientation

TokenList = [] # a list to count the number of tokens grabbed and save their codes.


def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    
def sign(a):
	if a < 0:
		return -1
	else:
		return 1
    
    
def find_token():
    """
    Function to find the closest token

    Returns:
	dist (float): distance of the closest token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    dist=100
    for token in R.see():  
        if token.dist < dist and token.info.code not in TokenList:  # if the robot can see the token, it checks if it is not already grabbed (not in list of Tokens)
            dist=token.dist
	    rot_y=token.rot_y
	    code_of_token=token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code_of_token
   	
def find_reference_token():
    """
    Function to find the first token where we will group other tokens

    register the token.info.code in the TokenList
    """
    dist=100
    for token in R.see():  # if the robot can see the token, it checks if it is not already grabbed (not in list of Tokens)
        if token.dist < dist and token.info.code not in TokenList:
	    dist=token.dist
	    rot_y=token.rot_y
	    code_of_token=token.info.code
    if dist==100:
	return -1, -1, -1
    else:
    	TokenList.append(code_of_token)
   	
   	
   	
   	
def Token_grabber(rot_y,dist,code_of_token):

    """This function works using the distance and orientation returned by the 
    function 'find_token' and it tends to update the distatnce and the orientation of the 
    token each time using the functions turn and drive to reach the box. and also it is used to grab
    the token and append the list of tokens"""

    while(dist<0):   #This loop works if the boxes are too far from the robot, so the loop makes the robot turn untill it finds a token.
        turn(-5,0.01)
        dist, rot_y, code_of_token = find_token()
    while (rot_y >= a_th or rot_y<=-a_th) : #This loop tries to find the exact orientation of the box
        turn(sign(rot_y-a_th) * 10,0.001) #I used the sign to make the robot turn with the right orientation
        dist, rot_y,code_of_token = find_token()
    while (dist >= d_th) : #This loop drives the robot to the token.
        drive(30,0.01)
        dist, rot_y, code_of_token = find_token()
    TokenList.append(code_of_token)
    R.grab()
    print("Got you box number:",len(TokenList))
    turn(20,0.1)
    
    
def find_previous_token():
    """
    Function to find the previous token

    Returns:
	dist (float): distance of the previous token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    dist=100
    for token in R.see():  # if the robot can see the token, it checks if it is the previously grabbed token
        if token.dist < dist and token.info.code==TokenList[-2]:
            dist=token.dist
	    rot_y=token.rot_y
	    code_of_token=token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code_of_token
    
    
   
def go_to_previous_and_release(rot_y,dist,code_of_token):
    """This function works with the same principle of the function token grabber, except 
    that instead of grab it releases """
    while(dist<0):
        turn(-5,0.01)
        dist, rot_y, code_of_token = find_previous_token()
    while (rot_y >= a_th or rot_y<=-a_th) :
        turn(sign(rot_y-a_th) * 10,0.001)
        dist, rot_y, code_of_token= find_previous_token()
    while (dist >= 1.5*d_th) :
        drive(40,0.01)
        dist, rot_y, code_of_token= find_previous_token()
    R.release()
    print("this is your place box number:",len(TokenList))
    drive(-30,0.8)
   	
   	
   	
   	
   	
def main():
	
    """Let's start our task by finding the first nearest box using the following function, without going to its direction"""	
    find_reference_token()
    
    
    while (len(TokenList)<6):
    	
        """Now we for the next box using the following function"""
        dist, rot_y, code_of_token = find_token()
        """This if statement to make the robot turn until it found a box"""
        if dist==-1:
            turn(10,0.1)
            continue
        """Now we have the orientation and the distance of the closest box so we ask
        the robot to go and grab it"""
        Token_grabber(rot_y,dist,code_of_token)
        print("Lets group you with the other boxes arround")
        """Now let's go back to the previous box"""
        dist, rot_y, code_of_token = find_previous_token()
        """Now we have the orientation and the distance of the previously grouped box so we ask
        the robot to go and drop the box close to it"""
        go_to_previous_and_release(rot_y,dist,code_of_token)
        print("")		
    drive(-30,2)
    turn(20,0.5)
    print("Mission completed")
            
            
main()          
