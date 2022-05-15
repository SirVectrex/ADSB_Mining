import streamlit as st
#import model.fr24data as fr24
import pandas as pd

st.write("")
st.title("ADSB Analytics")
st.write(
    "Instant Access to collected Data in CSV format.\n"
    "Fligtradar Datagathering is currently disabled.\n"
)


col1, col2, col3 = st.columns(3)
with col1:
    south = st.button("Show South")
with col2:
    north = st.button("Show North")
with col3:
    both = st.button("Show Both")
if south:
    df = pd.read_csv("./datacollector/26L.csv")
    # visulize data in streamlit
    st.write(df)
if north:
    df = pd.read_csv("./datacollector/26R.csv")
    # visulize data in streamlit
    st.write(df)
if both :
    st.write("26L - Southern Runway")
    df = pd.read_csv("./datacollector/26L.csv")
    # visulize data in streamlit
    st.write(df)
    st.write("26R - Northern Runway")
    df2 = pd.read_csv("./datacollector/26R.csv")
    # visulize data in streamlit
    st.write(df2)



#if st.button("Get Flightradar Data"):
#    st.write("Please enter a flightnumber for the desired flight. Please note - it has to be flying right now")
#    flightnumber = st.text_input("Flightnumber")

#    st.json(fr24.getflightdata_for_number(flightnumber))
