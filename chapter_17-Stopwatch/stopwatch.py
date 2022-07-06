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

# Write a loop to track the lap times & handle keyboard interrupt error
try:
    while True:
        input()
        lap_time = round(time.time() - last_record, 2)
        total_time = round(time.time() - start, 2)
        print(f"LAP TIME: {lap_time} - TOTAL TIME: {total_time} - LAP: {lap}")
        lap += 1
        last_record = time.time()
except KeyboardInterrupt:
    print("\nDone!")
