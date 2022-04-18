from FlightRadar24.api import FlightRadar24API

def getflightdata_for_number(nr):
    fr_api = FlightRadar24API()
    if nr == "":
        res = {
            "status" : "No flightnumber provided"
        }
        return res
    flight = fr_api.search_flight_by((nr))[0]
    print("The ID for this flight is:", flight.id)  # The ID for this flight is: 2af43d19
    details = fr_api.get_flight_details(flight_id=flight.id)
    flight.set_flight_details(details)
    return details
