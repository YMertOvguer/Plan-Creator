# adding libs
import numpy as np
import random

# setup
table = np.zeros((7, 7), dtype=str)
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

# getting lectures
while True:
    event = str(input("Enter lecture name: "))
    if event == "q":
        break
    else:
        listed_event.append(event)

# creating lecture plan

N = len(event)
while True:
    a = random.randint(0, N-1)
    plan.append(event[a])
    counter += 1
    if counter == 49:
        break
event_plan = np.array(plan)
event_plan = event_plan.reshape(7, 7)
print(event_plan)
