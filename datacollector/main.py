import Collection as coll
import time

if __name__ == '__main__':
    # Main function will serve for data collection only.
    # It will only run the data collection.
    # Please start ./app.py to run the web app.


    # check if current time is between 5am and 10pm time
    if 5 <= time.localtime().tm_hour <= 22:
        print("Starting collection...")
        print("Press Ctrl+C to stop collection.")
        coll.mixedrun()
        # Wait for Ctrl+C
