import streamlit as st
import requests
import datetime

st.title("🚕 Taxi Fare Prediction")

date = st.date_input("Pickup date", value=datetime.date.today())
time = st.time_input("Pickup time", value=datetime.datetime.now().time())
pickup_datetime = f"{date} {time}"

pickup_long = st.number_input("Pickup Longitude", value=-73.985428)
pickup_lat = st.number_input("Pickup Latitude", value=40.748817)
dropoff_long = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_lat = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.slider("Passenger Count", min_value=1, max_value=8, value=1)

# زر التوقع
if st.button("Predict Fare"):
    url = "https://taxifare.lewagon.ai/predict"
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_long,
        "pickup_latitude": pickup_lat,
        "dropoff_longitude": dropoff_long,
        "dropoff_latitude": dropoff_lat,
        "passenger_count": passenger_count
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"Estimated Fare: ${prediction:.2f}")
    else:
        st.error("Something went wrong 😢")
