import streamlit as st
import numpy as np

st.title("Real Estate Price Prediction (Clean SPSS Model)")

# المدن
city_geo = {
    "الدمام":   {"lat": 26.3927, "lng": 49.9777, "city_id": 1},
    "الخبر":    {"lat": 26.2172, "lng": 50.1971, "city_id": 2},
    "الظهران":  {"lat": 26.2361, "lng": 50.0393, "city_id": 3},
    "القطيف":   {"lat": 26.5593, "lng": 49.9961, "city_id": 4},
    "الجبيل":   {"lat": 27.0046, "lng": 49.6460, "city_id": 5}
}

# اتجاه الشارع (اختيار فقط)
direction_map = {
    "شمالي": 1.0,
    "جنوبي": 0.9,
    "شرقي": 0.8,
    "غربي": 0.7
}

property_type = st.selectbox("Property Type", [
    "Land Sale",
    "House Sale",
    "Land Rent"
])

city = st.selectbox("City", list(city_geo.keys()))

lat = city_geo[city]["lat"]
lng = city_geo[city]["lng"]
city_id = city_geo[city]["city_id"]

area = st.number_input("Area", min_value=1.0)
area_log = np.log(area)

# ❌ العميل لا يدخل أي شيء عن البحر أو الشارع
distance_to_sea = {
    "الدمام": 2,
    "الخبر": 1,
    "الظهران": 3,
    "القطيف": 1.5,
    "الجبيل": 5
}[city]

street_width = {
    "الدمام": 20,
    "الخبر": 18,
    "الظهران": 25,
    "القطيف": 12,
    "الجبيل": 15
}[city]

street_direction = direction_map[
    st.selectbox("Street Direction", ["شمالي", "جنوبي", "شرقي", "غربي"])
]

# ================= LAND SALE =================
if property_type == "Land Sale":

    price_log = (-190.854 +
                 0.882 * area_log -
                 0.030 * distance_to_sea +
                 0.010 * street_width +
                 3.024 * lng +
                 1.809 * lat +
                 0.014 * street_direction)

    price = np.exp(price_log)

# ================= HOUSE SALE =================
elif property_type == "House Sale":

    age = st.number_input("Age", 0)
    furnished = st.selectbox("Furnished", ["No", "Yes"])
    livings = st.number_input("Livings", 0)
    wc = st.number_input("WC", 0)
    beds = st.number_input("Beds", 0)

    f = 1 if furnished == "Yes" else 0

    price_log = (-125.153 +
                 0.814 * area_log -
                 0.007 * distance_to_sea -
                 0.015 * age +
                 1.280 * lat +
                 2.013 * lng +
                 0.176 * f +
                 0.018 * livings +
                 0.013 * wc +
                 0.006 * beds)

    price = np.exp(price_log)

# ================= LAND RENT =================
elif property_type == "Land Rent":

    price_log = (7.132 +
                 0.651 * area_log -
                 0.081 * distance_to_sea +
                 0.011 * street_width +
                 0.071 * street_direction +
                 0.044 * city_id)

    price = np.exp(price_log)

# OUTPUT
if st.button("Predict Price"):
    st.success(f"Price: {price:,.2f} SAR")
