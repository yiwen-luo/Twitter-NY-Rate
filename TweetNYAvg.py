#!/usr/bin/python
from sys import stdout
import json
import time
import redis

# Initialize Redis connection
conn = redis.Redis()

# Initialize "last_rate" for the first loop
last_rate = 0

# Initialize status
status_counter = 0
status = 'green'

while True:

    # Get data from Redis
    pipe = conn.pipeline()
    keys = conn.keys()
    values = conn.mget(keys)

    try:
        # Retrieve every tuples in Redis and convert to list in "deltas"
        deltas = [float(v) for v in values]
    except TypeError:
        print keys
        continue

    if len(deltas):

        # Calculate the rate of message in a given time windows (all data in Redis, here is 10 minutes)
        rate = sum(deltas) / float(len(deltas))
    else:
        rate = 0

    # If rate increases, increment the counter, vice versa
    if last_rate > 0:
        if rate > last_rate:
            status_counter += 1
        elif rate < last_rate:
            status_counter -= 1

    # Prevent counter to be negative, which has no meaning for the current, but may be utilized in future
    if status_counter < 0:
        status_counter = 0

    # Change status to different value depending on the counter
    if status_counter > 50:
            status = 'red'
    elif status_counter > 20:
            status = 'yellow'
    else:
            status = 'green'

    # Output data to be utilized by Websocketd
    print json.dumps({"rate": rate, 'status': status})
    stdout.flush()

    # Keep the current rate for next loop to evaluate the difference
    last_rate = rate
    time.sleep(1)
