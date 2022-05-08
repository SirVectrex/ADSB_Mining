import openskydata
from threading import Thread
import time

# loop until keyboard interrupt
def mixedrun():

    while True:
        try:

    # check if time is between 5am and 22pm
             if (5 <= int(time.strftime("%H")) <= 22):
                # start collecting data
                openskydata.get_north_runway_once();
                time.sleep(2)
                openskydata.get_south_runway_once()
                time.sleep(2)
        except KeyboardInterrupt:
            print("Exiting...")
            break

def easyrun():
    openskydata.startcollecting("northern")
    northern = Thread(target=openskydata.startcollecting("northern"))
    southern = Thread(target=openskydata.startcollecting("southern"))

    try:
        southern.run()
        northern.run()

    except KeyboardInterrupt:
        northern.terminate()
        southern.terminate()
        northern.join()
        southern.join()
        print("Exiting...")
        exit(0)


def run():


    northern = Thread(target=NorthernCollection)
    southern = Thread(target=SouthernCollection)
    northern.run()
    southern.run()
    try:
        while True:
            print("waiting...")
            pass
    except KeyboardInterrupt:
        northern.terminate()
        southern.terminate()
        northern.join()
        southern.join()
        print("Exiting...")
        exit(0)




def NorthernCollection():
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def start(self):
        while self._running:
            # get data from opensky
            openskydata.startcollecting("northern")


def SouthernCollection():
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            # get data from opensky
            openskydata.startcollecting("southern")

