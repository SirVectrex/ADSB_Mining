from opensky_api import OpenSkyApi
import time as t

User =
pw =

# api = OpenSkyApi(User, pw)


def test():
    api = OpenSkyApi(User, pw)
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    time = t.time()
    for n in range(7200):
        #states = api.get_states( bbox=(48.355026, 48.374598, 11.741354, 11.838376))
        states = api.get_states(time_secs=time, bbox=(48.355026, 48.374598, 11.741354, 11.838376))

        if states is not None:
                    print(states)b
        t.sleep(1)
        time = time - 5
    #for s in states.states:
    #    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
    return -1;


