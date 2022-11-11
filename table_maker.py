# adding libs
import numpy as np
import random

# setup
listed_event = []
plan = []
counter = 0

# presentation
print("""
-------------------------------------------------

enter you event name
            at least whatever you want...

press 'q' and hit enter button to quit

-------------------------------------------------
""")
# getting event number per-day
event_num_perD = int(input("Enter lecture number per-day: "))

# getting off days
event_off_num = int(input("Enter your off days as number(in a week): "))

# getting lectures
while True:
    event = str(input("Enter lecture name: "))
    if event == "q":
        break
    else:
        listed_event.append(event)

# creating lecture plan
total_event = (7 - event_off_num) * event_num_perD
N = len(event)
while True:
    a = random.randint(0, N-1)
    plan.append(event[a])
    counter += 1
    if counter == total_event:
        break
event_plan = np.array(plan)
event_plan = event_plan.reshape(7 - event_off_num, event_num_perD)

# showing plan
print(event_plan)
