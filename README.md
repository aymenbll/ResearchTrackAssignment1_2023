# ResearchTrackAssignment1_2023

# Robot Token Collection Algorithm

This Python code controls a robot to collect tokens placed in a space. It utilizes a series of functions to locate, grab, and organize the tokens.

## Functions

- **`find_token()`**
  - Finds the closest available token.
  - Returns the distance and orientation of the token relative to the robot.
 
    ```
    SET dist to a large value
    FOR EACH token IN Robot's vision:
        IF token distance < dist AND token code NOT in TokenList:
            UPDATE dist, rot_y, code_of_token with token values
    IF no token found:
        RETURN -1, -1, -1
    ELSE:
        RETURN dist, rot_y, code_of_token 

- **`find_reference_token()`**
  - Identifies the initial reference token, commencing the token collection process.
    ```
    SET dist to a large value
      FOR EACH token IN Robot's vision:
          IF token distance < dist AND token code NOT in TokenList:
              UPDATE dist, rot_y, code_of_token with token values
      IF no token found:
          RETURN -1, -1, -1
      ELSE:
          ADD code_of_token to TokenList

- **`Token_grabber(rot_y, dist, code_of_token)`**
  - Uses distance and orientation data to navigate and grab tokens.
  - Updates token information and adds the code to the list of collected tokens.
    ```
    WHILE dist < 0:
          Turn robot to find a token
      WHILE rot_y > a_th OR rot_y < -a_th:
          Turn robot to align with the token
      WHILE dist >= d_th:
          Move robot towards the token
      ADD code_of_token to TokenList
      Grab the token
      Display message indicating the grabbed box number
      Turn robot


- **`find_previous_token()`**
  - Locates the token previously grabbed by the robot.
  - Returns the distance and orientation of the identified token.
     ```
    SET dist to a large value
        FOR EACH token IN Robot's vision:
            IF token distance < dist AND token code matches second last token in TokenList:
                UPDATE dist, rot_y, code_of_token with token values
        IF no token found:
            RETURN -1, -1, -1
        ELSE:
            RETURN dist, rot_y, code_of_token

- **`go_to_previous_and_release(rot_y, dist, code_of_token)`**
  - Navigates to the previously collected token and releases it in a specific location.
    ```
    WHILE dist < 0:
            Turn robot to find the previous token
        WHILE rot_y > a_th OR rot_y < -a_th:
            Turn robot to align with the previous token
        WHILE dist >= 1.5 * d_th:
            Move robot towards the previous token
        Release the token
        Display message indicating the place box number
        Move the robot back

- **`drive(speed, seconds)`** & **`turn(speed, seconds)`**
  - Functions for controlling the robot's linear and angular velocity.
    ```
    FUNCTION drive(speed, seconds):
      SET power of motors to given speed
      WAIT for given seconds
      STOP motors

    FUNCTION turn(speed, seconds):
        SET power of motors to turn at given speed
        WAIT for given seconds
        STOP motors
## Execution

The `main()` function orchestrates the token collection process:
- Initiates by finding the first reference token.
- Continuously searches and collects tokens until the desired number of tokens is obtained.
- Moves back to previously collected tokens and releases them in designated positions.
- Completes the token collection mission upon reaching the set token count.

This code is intended for educational purposes and can be used to understand the basics of robot control and token collection algorithms.
```
Find the first nearest box
    WHILE length of TokenList < 6:
        Find the next closest token
        IF no token found:
            Turn the robot
            Continue to next iteration
        Grab the token and group it with others
        Find the previously grouped token
        Go to the previous token and release the box
    Move the robot back
    Turn the robot
    Display completion message

CALL main()

