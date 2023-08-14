import time as t
import csv

from opensky_api import OpenSkyApi


# open the file in the write mode
f = open('26R.csv', 'a', newline='')  # northern runway
f = open('26L.csv', 'a', newline='')  # southern runway

# define bbox
northrunway = (48.355026, 48.374598, 11.741354, 11.838376)
southrunway = (48.332477, 48.351134, 11.705034, 11.832545)

api = OpenSkyApi()

def startcollecting(runway):
    # loop with user interrupt
    while True:
        try:
            if runway == "northern":
                # if time is between the 5am and 10pm time, get the data
                if t.localtime().tm_hour >= 5 and t.localtime().tm_hour <= 22:
                    get_north_runway_data()
            elif runway == "southern":
                # if time is between the 5am and 10pm time, get the data
                if t.localtime().tm_hour >= 5 and t.localtime().tm_hour <= 22:
                    get_south_runway_data()
        except KeyboardInterrupt:
            print("\nExiting...")
            break

# get runway data in a loop
def get_north_runway_data():
    while True:
        states = api.get_states(time_secs=t.time(), bbox=northrunway)
        if states is not None:
            print("north:    "+ str(len(states))+  " planes tracked" )
            write_northern_csv(states);
        t.sleep(5)

def get_north_runway_once():
    # print(api)
    states = api.get_states(bbox=northrunway)
    if states is not None and states.states != []:
        try:
            print("north:    " + str(len(states.states)) +  " planes tracked at " + str(t.localtime().tm_hour) + ":" + str(t.localtime().tm_min) + ":" + str(t.localtime().tm_sec))
            write_northern_csv(states);

        except:
            print("Currently no plane on northern runway")
            # print(states)
    return -1;

def get_south_runway_once():
    south_states = api.get_states(bbox=southrunway)
    if south_states is not None and south_states.states != []:
        try:
            print("south:    " + str(len(south_states.states)) +  " planes tracked at " + str(t.localtime().tm_hour) + ":" + str(t.localtime().tm_min) + ":" + str(t.localtime().tm_sec))
            write_southern_csv(south_states);
            print(south_states)
        except:
            print("Currently no plane on southern runway")
            print(south_states)
    return -1;


# get runway data in a loop
def get_south_runway_data():
    while True:
        states = api.get_states(time_secs=t.time(), bbox=southrunway)
        if states is not None:
            print(states)
            write_southern_csv(states);
        t.sleep(5)


def MUC_northernrunway_curr():
    time = t.time()
    for n in range(10):
        states = api.get_states(bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
            print(states)
        t.sleep(1)

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

# write northern runway data to file
def write_northern_csv(states):
    with open('./26R.csv', 'a', newline='') as csvfile:
        fieldnames = ['icao24', 'flightnumber', 'Country', 'Timestamp', 'latitude', 'longitude', 'baro_altitude', 'vertical_rate', 'on_ground', 'runway', 'state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        if states is not None:
            try:
                for s in states.states:
                    # append row to csv
                    if(s.callsign != None):
                        if(s.vertical_rate > 0 and s.on_ground == False):
                            pos = "Takeoff"
                        elif(s.vertical_rate < 0 and s.on_ground == False):
                            pos = "Landing"
                        else:
                            pos = "Ground"
                        writer.writerow({'icao24': s.icao24, 'flightnumber': s.callsign, 'Country': s.origin_country,
                                     'Timestamp': unix_to_timestamp(s.last_contact), 'latitude': s.latitude,
                                     'longitude': s.longitude, 'baro_altitude': s.baro_altitude,
                                     'vertical_rate': s.vertical_rate, 'on_ground': s.on_ground, 'runway': '26R','state': pos})
            except:
                print("Error writing one plane.")
    return -1;


# write southern runway data to file
def write_southern_csv(states):
    with open('./26L.csv', 'a', newline='') as csvfile:
        fieldnames = ['icao24', 'flightnumber', 'Country', 'Timestamp', 'latitude', 'longitude', 'baro_altitude',
                      'vertical_rate', 'on_ground', 'runway', 'state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        for s in states.states:
            try:
            # append row to csv
                if(s.callsign != None and s.callsign != ""):
                    if(s.vertical_rate != None and s.on_ground != None):
                        if(s.vertical_rate > 0 and s.on_ground == False):
                            pos = "Takeoff"
                        elif(s.vertical_rate < 0 and s.on_ground == False):
                            pos = "Landing"
                        else:
                            pos = "Ground"

                    else:
                        pos = "Not Avail."
                    if(pos != "Not Avail." and pos != "Ground"):
                        writer.writerow({'icao24': s.icao24, 'flightnumber': s.callsign, 'Country': s.origin_country,
                                 'Timestamp': unix_to_timestamp(s.last_contact), 'latitude': s.latitude,
                                 'longitude': s.longitude, 'baro_altitude': s.baro_altitude,
                                 'vertical_rate': s.vertical_rate, 'on_ground': s.on_ground, 'runway': '26L','state': pos})
            except:
                print("Error writing one plane.")
                print(s)
    return -1;


def test():
    api = OpenSkyApi()
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    time = t.time()
    for n in range(10):
        # states = api.get_states( bbox=(48.355026, 48.374598, 11.741354, 11.838376))
        states = api.get_states(time_secs=time, bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
            print(states.states[0])
        t.sleep(1)
        time = time - 5
    # for s in states.states:
    #    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
    return -1;

def unix_to_timestamp(unix_time):
    return t.strftime("%Y-%m-%d %H:%M:%S", t.localtime(unix_time))