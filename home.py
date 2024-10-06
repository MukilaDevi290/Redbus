import streamlit as st
import pandas as pd
import numpy as np

# set page configuration
st.set_page_config(layout="wide")

st.title("RED BUS")
st.image("https://shop.signimus.com/wp-content/uploads/2024/05/TICKET-BOOKING.png",width=900)
st.header("BUS ROUTES AND DETAILS")


# Create a dictionary of DataFrames
df_list = {
    "HRTC BUSES": pd.read_csv("hrtc_bus_details.csv"),
    "JKSRTC BUSES": pd.read_csv("jksrtc_bus_details.csv"),
    "ASTC BUSES": pd.read_csv("astc_bus_details.csv"),
    "BSRTC BUSES": pd.read_csv("bsrtc_bus_details.csv"),
    "KSRTC BUSES": pd.read_csv("ksrtc_bus_details.csv"),
    "KTCL BUSES": pd.read_csv("ktcl_bus_details.csv"),
    "NBSTC BUSES": pd.read_csv("nbstc_bus_details.csv"),  
    "PEPSU BUSES": pd.read_csv("pepsu_bus_details.csv"),
    "RSRTC BUSES": pd.read_csv('rsrtc_bus_details.csv'),
    "UPSRTC BUSES": pd.read_csv("upsrtc_bus_details.csv")
}

st.sidebar.title("Select Bus states")
selected_bus = st.sidebar.radio("Choose a bus states:", list(df_list.keys()))
st.subheader(f"DETAILS OF {selected_bus} ")
st.dataframe(df_list[selected_bus],width=1000) 
st.button("Bus Booking")
st.write("Click [here](https://www.redbus.in/) to book your bus!")
st.write("ADVERTISEMENT FOR BUS BOOKING")
st.video("https://youtu.be/eyAAUGhvZu8?si=EM34RkHyVovBoRUr")








