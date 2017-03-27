import os
import datetime
import time
import subprocess
import sys

def main():
    weekday = int(os.environ["WEEKDAY"])
    hour, minute = os.environ["TIME"].split(":")

    hour = int(hour)
    minute = int(minute)

    while True:
        today = datetime.date.today()
        next_weekday = today + datetime.timedelta((weekday - today.weekday()) % 7 )
        next_time = datetime.datetime.combine(next_weekday, datetime.time(hour, minute))

        wait_delta = next_time - datetime.datetime.now()
        if wait_delta.total_seconds() < 0.0:
            wait_delta += datetime.timedelta(days=7)

        print("Next run time is", datetime.datetime.now() + wait_delta)
        print("Waiting", wait_delta.total_seconds(), "seconds")

        time.sleep(wait_delta.total_seconds())

        print(sys.argv[1:])
        subprocess.run(sys.argv[1:])

if __name__ == "__main__":
    main()
