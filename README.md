# ResearchTrackAssignment1_2023

# Robot Token Collection Algorithm

This Python code controls a robot to collect tokens placed in a space. It utilizes a series of functions to locate, grab, and organize the tokens.

## Functions

- **`find_token()`**
  - Finds the closest available token.
  - Returns the distance and orientation of the token relative to the robot.

- **`find_reference_token()`**
  - Identifies the initial reference token, commencing the token collection process.

- **`Token_grabber(rot_y, dist, code_of_token)`**
  - Uses distance and orientation data to navigate and grab tokens.
  - Updates token information and adds the code to the list of collected tokens.

- **`find_previous_token()`**
  - Locates the token previously grabbed by the robot.
  - Returns the distance and orientation of the identified token.

- **`go_to_previous_and_release(rot_y, dist, code_of_token)`**
  - Navigates to the previously collected token and releases it in a specific location.

- **`drive(speed, seconds)`** & **`turn(speed, seconds)`**
  - Functions for controlling the robot's linear and angular velocity.

- **`sign(a)`**
  - Returns the sign of a value (`-1` for negative values, `1` otherwise).

## Execution

The `main()` function orchestrates the token collection process:
- Initiates by finding the first reference token.
- Continuously searches and collects tokens until the desired number of tokens is obtained.
- Moves back to previously collected tokens and releases them in designated positions.
- Completes the token collection mission upon reaching the set token count.

This code is intended for educational purposes and can be used to understand the basics of robot control and token collection algorithms.

Please refer to the source code for detailed implementation and usage instructions.
