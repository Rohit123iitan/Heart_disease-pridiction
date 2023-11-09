import streamlit as st
import util

st.title("Heart Disease Prediction :heart:")

util.load_saved_artifacts()
gender,height,weight,age = st.columns(4)

gender_ = gender.number_input("Gender",min_value=1,max_value=2,value=1,step=1)
height_ = height.number_input("Height",min_value=50,max_value=300,value=100,step=1)
weight_ = weight.number_input("Weight",min_value=10,max_value=250,value=10,step=1)
age_ = age.number_input("Age",min_value=0,max_value=100,value=1,step=1)

ap_hi,ap_lo = st.columns(2)

ap_hi = ap_hi.number_input("Maximum pressure",min_value=-150,max_value=16030,value=110,step=1)

ap_lo = ap_lo.number_input("Minimum pressure",min_value=-80,max_value=12000,value=80,step=1)



smoke,alco,active,cholesterol,glucose = st.columns(5)
cholesterol = cholesterol.slider("Cholesterol",min_value=1,max_value=5,value=1,step=1)
glucose = glucose.slider("Glucose",min_value=1,max_value=5,value=1,step=1)
smoke = smoke.slider("Smoke",min_value=0,max_value=1,value=0,step=1)
alco = alco.slider("Alcohol",min_value=0,max_value=1,value=0,step=1)
active = active.slider("Active status",min_value=0,max_value=1,value=0,step=1)
# age_ = age.number_input("Age",min_value=0,max_value=15000,value=1,step=1)

if st.button("Predict"):
    cardio = util.get_estimated_cardio(age_,gender_,height_,weight_,ap_hi,ap_lo,alco,active,smoke,glucose,cholesterol)
    if(cardio==0):
        st.write(f"No Heart Disease")
    else:
        st.write("Person with above details have Heart Disease")
