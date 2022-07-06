#! python3
#  stopwatch.py - A simple stopwatch program

import time

# Display the program's instructions
print("Press ENTER to begin, then press ENTER to record a lap or Ctrl-C to quit.")
input()

# start the stopwatch if user presses ENTER
start = time.time()
last_record = start
lap = 1

# TODO: Write a loop to track the lap times & handle keyboard interrupt error
