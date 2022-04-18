import streamlit as st
import model.fr24data  as fr24


st.write("")
st.title("Flightradar Analytics")
st.write(
    "Instant Access to Flightradar Raw Data in JSON"
)
st.write("COMING SOON - Runway predictions based on historical flight data")

st.write("Please enter a flightnumber for the desired flight. Please note - it has to be flying right now")
flightnumber = st.text_input("Flightnumber")

st.json(fr24.getflightdata_for_number(flightnumber))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Main function is currently disabled for streamlit functionality.
    print("Main function currently disabled. Please use streamlit run")


