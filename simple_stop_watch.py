# This script helps to build a simple stopwatch application
# using Python's time module.

import time

print('Press ENTER to begin, Press Ctrl + C to stop')
while True:
    input()
    print('Started')
    start_time = time.time()
    try:
        while True:
            print('Stoppedapsed: ', round(time.time() - start_time, 0),
                  'secs', end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopped')
        end_time = time.time()
        print('Total Time:', round(end_time - start_time, 2), "secs")
        break
