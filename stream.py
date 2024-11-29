

import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(layout="wide")

st.title("RED BUS")
st.image("https://shop.signimus.com/wp-content/uploads/2024/05/TICKET-BOOKING.png", width=900)
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

# Sidebar for selecting bus states
st.sidebar.title("Select Bus States")
selected_bus = st.sidebar.radio("Choose a bus state:", list(df_list.keys()))
st.subheader(f"DETAILS OF {selected_bus}")

#create a variable bus_df
bus_df = df_list[selected_bus]
st.dataframe(bus_df)



# Dropdown for selecting routes within the selected bus state
selected_route = st.selectbox("SELECT A ROUTE:", bus_df['Route_Name'].unique())
route_df = bus_df[bus_df['Route_Name'] == selected_route]
st.dataframe(route_df)



# Filters
st.sidebar.header("Filters")

Departing_Time = st.sidebar.selectbox(
    "DEPARTING TIME",
    ["Before 6 am", "6 am to 12 pm", "12 pm to 6 pm", "After 6 pm"]
)

Bus_Type = st.sidebar.multiselect(
    "BUS TYPE",
    ["SEATER", "SLEEPER", "AC", "NONAC"]
)

Arrival_Time = st.sidebar.selectbox(
    "ARRIVAL TIME",
    ["Before 6 am", "6 am to 12 pm", "12 pm to 6 pm", "After 6 pm"]
)



# Apply filters to the route_df
filtered_df = route_df


# Filter by Departure Time
if Departing_Time == "Before 6 am":
    filtered_df = filtered_df[filtered_df['Departing_Time'] < "06:00"]
elif Departing_Time == "6 am to 12 pm":
    filtered_df = filtered_df[(filtered_df['Departing_Time'] >= "06:00") & (filtered_df['Departing_Time'] < "12:00")]
elif Departing_Time == "12 pm to 6 pm":
    filtered_df = filtered_df[(filtered_df['Departing_Time'] >= "12:00") & (filtered_df['Departing_Time'] < "18:00")]
elif Departing_Time == "After 6 pm":
    filtered_df = filtered_df[filtered_df['Departing_Time'] >= "18:00"]


if Bus_Type:
    # Use string contains for flexible matching
    filtered_df = filtered_df[filtered_df['Bus_Type'].str.upper().str.contains('|'.join([b.upper() for b in Bus_Type]))]
   
# Filter by Arrival Time
if Arrival_Time == "Before 6 am":
    filtered_df = filtered_df[filtered_df['Arrival_Time'] < "06:00"]
elif Arrival_Time == "6 am to 12 pm":
    filtered_df = filtered_df[(filtered_df['Arrival_Time'] >= "06:00") & (filtered_df['Arrival_Time'] < "12:00")]
elif Arrival_Time == "12 pm to 6 pm":
    filtered_df = filtered_df[(filtered_df['Arrival_Time'] >= "12:00") & (filtered_df['Arrival_Time'] < "18:00")]
elif Arrival_Time == "After 6 pm":
    filtered_df = filtered_df[filtered_df['Arrival_Time'] >= "18:00"]

# Display the filtered DataFrame
if not filtered_df.empty:
    st.write("Filtered DataFrame:")
    st.dataframe(filtered_df)

else:
    st.write("No results match your filters")
   
st.button("Bus Booking")
st.write("Click [here](https://www.redbus.in/) to book your bus!")
st.write("ADVERTISEMENT FOR BUS BOOKING")
st.video("https://youtu.be/eyAAUGhvZu8?si=EM34RkHyVovBoRUr")
