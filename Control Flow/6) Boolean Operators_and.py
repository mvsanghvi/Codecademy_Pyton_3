#1. Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
#2. Let’s return to Calvin Coolidge’s Cool College. 
# 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher.
# Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement. 
# If they do, print the string:
credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")