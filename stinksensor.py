import time
from aq import AQ

aq = AQ()
aq.leds_automatic()

# Poll every x seconds
interval = 30
# Fire the action after AQ >= action_threshold
action_threshold = 1000

last_update = 0
t0 = int(time.monotonic())

def action():
    print("AQ too high, action fired!")

current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Process started at: " + current_time)

try:
    while True:
        now = time.monotonic()
        if (now > last_update + interval):
            last_update = now
            if int(aq.get_eco2()) >= action_threshold:
                action()
except:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Process ended at: " + current_time)
