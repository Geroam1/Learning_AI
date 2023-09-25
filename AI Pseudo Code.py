
# Import the necessary libraries or modules for API communication
import RobotAPI as ra

# Initialize the robot and establish a connection
robot = RobotAPI.initialize()

# Define movement commands
forward_speed = 50  # Set forward speed (adjust as needed)
backward_speed = -50  # Set backward speed (negative to reverse)

# Move the robot forward
robot.move(forward_speed)

# Wait for a few seconds (or as needed)
wait(2)

# Stop the robot
robot.stop()

# Move the robot backward
robot.move(backward_speed)

# Wait for a few seconds (or as needed)
wait(2)

# Stop the robot
robot.stop()

# Close the connection to the robot
robot.close()
