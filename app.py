import streamlit as st
import numpy as np

st.title("Real Estate Price Prediction")

property_type = st.selectbox("Property Type", [
    "Land Sale",
    "House Sale",
    "Apartment Sale",
    "Land Rent",
    "House Rent",
    "Apartment Rent"
])

# ======================
# 📌 common inputs
# ======================
area = st.number_input("Area (sqm)", min_value=1.0)
area_log = np.log(area)

distance_to_sea = st.number_input("Distance to Sea", 0.0)
street_width = st.number_input("Street Width", 0.0)
street_direction = st.number_input("Street Direction", 0.0)

lat = st.number_input("Latitude", 0.0)
lng = st.number_input("Longitude", 0.0)

city_id = st.number_input("City ID", 0.0)

# ======================
# 🏡 LAND SALE
# ======================
if property_type == "Land Sale":

    price = (
        -190.854 +
        0.882 * area_log +
        -0.030 * distance_to_sea +
        0.010 * street_width +
        3.024 * lng +
        1.809 * lat +
        0.014 * street_direction
    )

# ======================
# 🏠 HOUSE SALE
# ======================
elif property_type == "House Sale":

    age = st.number_input("Age", 0)
    furnished = st.selectbox("Furnished", ["No", "Yes"])
    livings = st.number_input("Living Rooms", 0)
    wc = st.number_input("Bathrooms", 0)
    beds = st.number_input("Beds", 0)

    furnished_val = 1 if furnished == "Yes" else 0

    price = (
        -125.153 +
        0.814 * area_log +
        -0.007 * distance_to_sea +
        -0.015 * age +
        1.280 * lat +
        2.013 * lng +
        0.176 * furnished_val +
        0.010 * street_direction +
        0.018 * livings +
        0.013 * wc +
        0.006 * beds
    )

# ======================
# 🏢 APARTMENT SALE
# ======================
elif property_type == "Apartment Sale":

    age = st.number_input("Age", 0)
    livings = st.number_input("Living Rooms", 0)
    wc = st.number_input("Bathrooms", 0)
    beds = st.number_input("Beds", 0)

    price = (
        10.738 +
        0.473 * area_log +
        0.042 * wc +
        -0.003 * street_width +
        0.051 * livings +
        -0.007 * age +
        -0.006 * beds
    )

# ======================
# 🌱 LAND RENT
# ======================
elif property_type == "Land Rent":

    price = (
        7.132 +
        0.651 * area_log +
        -0.081 * distance_to_sea +
        0.011 * street_width +
        0.071 * street_direction +
        0.044 * city_id
    )

# ======================
# 🏠 HOUSE RENT
# ======================
elif property_type == "House Rent":

    furnished = st.selectbox("Furnished", ["No", "Yes"])
    livings = st.number_input("Living Rooms", 0)

    furnished_val = 1 if furnished == "Yes" else 0

    price = (
        8.080 +
        0.512 * area_log +
        0.338 * furnished_val +
        -0.023 * distance_to_sea +
        0.078 * livings
    )

# ======================
# 🏢 APARTMENT RENT
# ======================
elif property_type == "Apartment Rent":

    rent_period = st.number_input("Rent Period")
    wc = st.number_input("Bathrooms", 0)
    furnished = st.selectbox("Furnished", ["No", "Yes"])
    beds = st.number_input("Beds", 0)
    livings = st.number_input("Living Rooms", 0)
    kitchen = st.number_input("Kitchen", 0)

    furnished_val = 1 if furnished == "Yes" else 0

    price = (
        3.429 +
        1.796 * rent_period +
        0.360 * wc +
        0.274 * furnished_val +
        0.111 * beds +
        0.183 * livings +
        -0.246 * kitchen
    )

# ======================
# 🚀 OUTPUT
# ======================
if st.button("Predict Price"):
    st.success(f"Predicted Price: {price:,.2f} SAR")
