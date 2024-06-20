import streamlit as st
def calculate_bmi(weight, height):
    bmi = weight / (height/100)**2
    return bmi
st.title("BMI Calculator")
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your weight (cm):", min_value=1.0, step=0.1)
if st.button("Calculate"):
    bmi = calculate_bmi(weight, height)
    st.writer(f"Your BMI is: {bmi:.2f}")

if st.button("Calculate"):
    bmi = calculate_bmi(weight, height)
    st.writer(f"Ypur BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.writer("Your are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.writer("You have a normal weight")
    elif 25 <= bmi < 29.9:
        st.writer("You are overweight.")
    else:
        st.writer("Your are obese.")
