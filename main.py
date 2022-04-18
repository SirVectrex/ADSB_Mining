import streamlit as st
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

st.write("")
st.title("Flightradar Analytics")
st.write(
    "Instant Access to Flightradar Raw Data in JSON"
)
st.write("COMING SOON - Runway predictions based on historical flight data")

st.write("Please enter a flightnumber for the desired flight. Please note - it has to be flying right now")
flightnumber = st.text_input("Flightnumber")

st.json(getflightdata_for_number(flightnumber))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Main function is currently disabled for streamlit functionality.
    print("Main function currently disabled. Please use streamlit run")


