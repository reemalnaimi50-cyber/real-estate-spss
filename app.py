import streamlit as st
import numpy as np
import pandas as pd

# 🏫 الشعار + العنوان بشكل احترافي
col1, col2 = st.columns([1, 5])

with col1:
    st.image("IMG_9045.png", width=180)

with col2:
    st.title("Real Estate Price Prediction")

# 🌍 Cities
city_geo = {
    "الدمام":   {"lat": 26.3927, "lng": 49.9777, "city_id": 1},
    "الخبر":    {"lat": 26.2172, "lng": 50.1971, "city_id": 2},
    "الظهران":  {"lat": 26.2361, "lng": 50.0393, "city_id": 3},
    "القطيف":   {"lat": 26.5593, "lng": 49.9961, "city_id": 4},
    "الجبيل":   {"lat": 27.0046, "lng": 49.6460, "city_id": 5}
}

# 🧭 اتجاه الشارع (فقط 3 نماذج تستخدمه)
direction_map = {
    "شمالي": 1.0,
    "جنوبي": 0.9,
    "شرقي": 0.8,
    "غربي": 0.7
}

property_type = st.selectbox("Property Type", [
    "Land Sale",
    "House Sale",
    "Apartment Sale",
    "Land Rent",
    "House Rent",
    "Apartment Rent"
])

city = st.selectbox("City", list(city_geo.keys()))

lat = city_geo[city]["lat"]
lng = city_geo[city]["lng"]
city_id = city_geo[city]["city_id"]

# 🗺️ خريطة حسب المدينة المختارة
map_data = pd.DataFrame({
    "lat": [lat],
    "lon": [lng]
})

st.map(map_data)

area = st.number_input("Area", min_value=1.0)
area_log = np.log(area)

# 🚫 لا يوجد إدخال للمسافة أو عرض الشارع نهائياً

# 🧭 الاتجاه (يستخدم فقط في 3 نماذج)
direction = st.selectbox("Street Direction", ["شمالي", "جنوبي", "شرقي", "غربي"])
street_direction = direction_map[direction]

# ================= LAND SALE =================
if property_type == "Land Sale":

    price_log = (-190.854 +
                 0.882 * area_log +
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
                 0.015 * age +
                 1.280 * lat +
                 2.013 * lng +
                 0.176 * f +
                 0.010 * street_direction +
                 0.018 * livings +
                 0.013 * wc +
                 0.006 * beds)

    price = np.exp(price_log)

# ================= APARTMENT SALE =================
elif property_type == "Apartment Sale":

    age = st.number_input("Age", 0)
    livings = st.number_input("Livings", 0)
    wc = st.number_input("WC", 0)
    beds = st.number_input("Beds", 0)

    price_log = (10.738 +
                 0.473 * area_log +
                 0.042 * wc +
                 0.051 * livings -
                 0.007 * age -
                 0.006 * beds)

    price = np.exp(price_log)

# ================= LAND RENT =================
elif property_type == "Land Rent":

    price_log = (7.132 +
                 0.651 * area_log +
                 0.071 * street_direction +
                 0.044 * city_id)

    price = np.exp(price_log)

# ================= HOUSE RENT =================
elif property_type == "House Rent":

    furnished = st.selectbox("Furnished", ["No", "Yes"])
    livings = st.number_input("Livings", 0)

    f = 1 if furnished == "Yes" else 0

    price_log = (8.080 +
                 0.512 * area_log +
                 0.338 * f +
                 0.078 * livings)

    price = np.exp(price_log)

# ================= APARTMENT RENT =================
elif property_type == "Apartment Rent":

    rent_period = st.number_input("Rent Period", 1)
    wc = st.number_input("WC", 0)
    furnished = st.selectbox("Furnished", ["No", "Yes"])
    beds = st.number_input("Beds", 0)
    livings = st.number_input("Livings", 0)
    kitchen = st.number_input("Kitchen", 0)

    f = 1 if furnished == "Yes" else 0

    price_log = (3.429 +
                 1.796 * rent_period +
                 0.360 * wc +
                 0.274 * f +
                 0.111 * beds +
                 0.183 * livings -
                 0.246 * kitchen)

    price = np.exp(price_log)

# 🚀 OUTPUT
if st.button("Predict Price"):
    st.success(f"Predicted Price: {price:,.2f} SAR")
