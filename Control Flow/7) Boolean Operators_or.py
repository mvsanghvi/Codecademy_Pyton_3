#1. Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
#2. The registrar’s office at Calvin Coolidge’s Cool College has another request. 
# They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA). 
# Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints: "You have met at least one of the requirements."
credits = 118
gpa = 2.0

if credits >=120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
