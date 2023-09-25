# plan:
# 1- we want the robot to move
# 
# 2- we want the robot to determine its own directions



# Pesudo code

# Import the necessary libraries or modules for API communication
# import RobotAPI as ra

# # Initialize the robot and establish a connection
# # robot = RobotAPI.initialize()

# Initialize starting postition

# Define movement commands
# forward_speed = 50  # Set forward speed (adjust as needed)
# backward_speed = -50  # Set backward speed (negative to reverse)

# Move the robot forward
# robot.move(forward_speed)

# Wait for a few seconds (or as needed)
# wait(2)

# # Stop the robot
# robot.stop()

# Move the robot backward
# robot.move(backward_speed)

# # Wait for a few seconds (or as needed)
# wait(2)

# Stop the robot
# robot.stop()

# Close the connection to the robot
# robot.close()

# ---------------------------------------------------------------------------------------------------------------------------
# training pseudo code

# 1 - get into position, a starting point 
#     (initilized position, not really up to the robot)

# 2 - define an enviroment, the robot will create a new enviroment if it does not already exist 
#     (some sort of graphical interface, a simulation if you will. x axis left and right,  y axis up and down, z axis (optional))

# 3 - it needs to look before it moves, get data on "what" is in its way, e.g. a bump in the pipe 
#     (define the obstacle the snake is facing)

# 4 - it needs to define its options
#     (options that depend on the obstacle, e.g. a dent, option: move left or move right, ?? explode ??)

# 5 - it needs to make a decion
#     (e.g. move right, and then take the option of moving right out of the list of options)

# 6 - if all decions have been made, and all failed, retreat. (pull the robot out the pipe) else:
#     (if there are no options in the "list", print a message to the user to pull out, e.g. print("help me world"))

# 7 - document whether if it failed or succeeded, such as 0 if fail 1 if success
#     (append to a dictionary or smthn, e.g. that option "moving right", failed in enviroment "dent")

# 8 - if it failed, back to step 5, if it succeeded document the success and the enviroment, 
#     so we know what succeeded in that enviroment (loop the training)

# 9 - reward the robot (some reward system, e.g. increase probability of a succeeding choice)

# 10 - back to step two, to test other enviroments, or try the same enviroment again, to be sure of an working option

# ---------------------------------------------------------------------------------------------------------------------------


# example of an enviroment checking code
real_enviroment = False
enviroments = ["Dent", "South Bump", "North Bump", "West Bump", "East Bump"]

while real_enviroment == False:
    enviroment = input("state an enviroment: ")
    if enviroment not in enviroments:
        print("Please enter an actaul enviroment")
    else:
        real_enviroment = True

print("thats a valid enviroment")





