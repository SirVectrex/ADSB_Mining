from unittest import case

from opensky_api import OpenSkyApi
import time as t
import csv

# open the file in the write mode
f = open('26R.csv', 'w')  # northern runway
f = open('26L.csv', 'w')  # southern runway

# define bbox
northrunway = (48.355026, 48.374598, 11.741354, 11.838376)
southrunway = (48.332477, 48.354276, 11.705034, 11.833045)

User =
pw =

api = OpenSkyApi(User, pw)


# get runway data in a loop
def get_north_runway_data():
    while True:
        states = api.get_states(time_secs=t.time(), bbox=(48.355026, 48.374598, 11.741354, 11.838376))
        if states is not None:
            print(states)
            write_northern_csv(states);
        t.sleep(1)


def startcollecting(runway):
    # loop with user interrupt
    while True:
        try:
            if runway == "northern":
                get_north_runway_data()
            elif runway == "southern":
                get_south_runway_data()
        except KeyboardInterrupt:
            print("\nExiting...")
            break


# get runway data in a loop
def get_south_runway_data():
    while True:
        states = api.get_states(time_secs=t.time(), bbox=(48.332477, 48.354276, 11.705034, 11.833045))
        if states is not None:
            print(states)
            write_southern_csv(states);
        t.sleep(1)


def MUC_northernrunway_curr():
    time = t.time()
    for n in range(10):
        states = api.get_states(bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
            print(states)
        t.sleep(1)
        time = time - 5

    return -1;


def MUC_northernrunway_hist(begin, end, step):
    range = (end - begin) / step
    time = begin
    for n in range(10):
        states = api.get_states(time_secs=time, bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
            print(states)
        t.sleep(1)
        time = time - 5
    return -1;


def MUC_southernrunway():
    time = t.time()
    for n in range(10):
        # coordinates include the full southern runway
        states = api.get_states(bbox=(48.332477, 48.354276, 11.705034, 11.833045))

        if states is not None:
            print(states)
        t.sleep(1)
        time = time - 5

    return -1;

    return -1;


# write northern runway data to file
def write_northern_csv(states):
    with open('26R.csv', 'w') as csvfile:
        fieldnames = ['latitude', 'longitude', 'baro_altitude', 'velocity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in states.states:
            writer.writerow({'latitude': s.latitude, 'longitude': s.longitude, 'baro_altitude': s.baro_altitude,
                             'velocity': s.velocity})
    return -1;


# write southern runway data to file
def write_southern_csv(states):
    with open('26L.csv', 'w') as csvfile:
        fieldnames = ['latitude', 'longitude', 'baro_altitude', 'velocity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in states.states:
            writer.writerow({'latitude': s.latitude, 'longitude': s.longitude, 'baro_altitude': s.baro_altitude,
                             'velocity': s.velocity})
    return -1;


def test():
    api = OpenSkyApi(User, pw)
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    time = t.time()
    for n in range(10):
        # states = api.get_states( bbox=(48.355026, 48.374598, 11.741354, 11.838376))
        states = api.get_states(time_secs=time, bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
            print(states)
        t.sleep(1)
        time = time - 5
    # for s in states.states:
    #    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
    return -1;
