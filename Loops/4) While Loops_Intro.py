# 1. Examine the while loop from the narrative in your code editor. 
# There are additional print() statements to help visualize the iterations.
# Run the code to see what happens on each iteration of the loop. 
# When you are finished, comment out the example to make space for the rest of the checkpoints.
# To quickly comment out the code, use your cursor or mouse to highlight all the code and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.
# If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop! If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else. To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# 2. Let’s write a while loop that counts down from 10 to 0(inclusive). 
# Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".
# As we saw in the narrative, our key components will be:
#     A variable to keep track of the count, and also help our loop eventually stop.
#     A condition that our while loop will check on each iteration.
#     Several code statements to execute on each iteration of the loop.
# Let’s tackle the first component!
# Create a variable named countdown and set the value to 10.
countdown = 10

# 3. Now let’s tackle the actual while loop. 
# Define a while loop that will run while our countdown variable is greater than or equal to zero.
# On each iteration:
#     We should print() the value of the countdown variable.
#     We should decrease the value of the countdown variable by 1
# Make sure to only print the value of countdown.
print("Count initiating")
while countdown >0:
  print(countdown)
  countdown -= 1

# 4. Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.

print("We have liftoff!")



