# Run code block 1 and examine the error message.
# Fix the syntax error then run the code again to check your work.

# Code block 1:
launch_ready = False
fuel_level = 27000

if fuel_level >= 20000:
   print('Fuel level cleared.')
   launch_ready = True
else:
   print('WARNING: Insufficient fuel!')
   launch_ready = False

# Code block 2 hides two syntax errors.
# Un-comment lines 18 - 34. Run the code and find the mistakes. Only ONE error will be flagged at a time. 

crew_status = True
computer_status = 'green'

if crew_status and computer_status == 'green':
  print('Crew & computer cleared.')
  launch_ready = True
else:
  print('WARNING: Crew or computer not ready!')
  launch_ready = False

if (launch_ready):
  print("10, 9, 8, 7, 6, 5, 4, 3, 2, 1...")
  print("Fed parrot...")
  print("Ignition...")
  print("Liftoff!")
else:
  print("Launch scrubbed.")

# Run this code block 3 and examine the error message.
# Pay close attention to any line numbers mentioned in the message - these will help locate and repair the mistake in the code.

# Code block 3:
launch_ready = False
fuel_level = 27000

if fuel_level >= 20000:
   print('Fuel level cleared.')
   launch_ready = True
else:
   print('WARNING: Insufficient fuel!')
   launch_ready = False

# Code block 4:
# Un-comment lines 18 - 26, run the program, and fix the error.

if launch_ready:
   print("10, 9, 8...")
   print("Fed parrot...")
   print("6, 5, 4...")
   print("Ignition...")
   print("3, 2, 1...")
   print("Liftoff!")
else:
   print("Launch scrubbed.")

# Let’s break the code down into smaller chunks to help fix the logic errors.
# Follow the instructions here to complete the task: https://education.launchcode.org/data-analysis/chapters/errors-and-debugging/studio.html#solve-logic-errors-last

fuel_ready = False
crew_ready=False
fuel_level = 17000
crew_status = True
computer_status = 'green'

if fuel_level >= 20000:
  print('Fuel level cleared.')
  fuel_ready = True
else:
  print('WARNING: Insufficient fuel!')
  fuel_ready = False

if crew_status and computer_status == 'green':
  print('Crew & computer cleared.')
  crew_ready = True
else:
  print('WARNING: Crew or computer not ready!')
  crew_ready = False

if fuel_ready and crew_ready:
  print('10, 9, 8, 7, 6, 5, 4, 3, 2, 1...')
  print('Liftoff!')
else:
  print('Launch scrubbed.')
