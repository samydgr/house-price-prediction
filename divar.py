import streamlit as st
import numpy as np
import pandas as pd
import joblib

from model import predict_house, Addresses
html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Forecasting the price of divar houses in 1400 by Samyar dagigi Rad </h1>
    </div>
    """

st.markdown(html_temp, unsafe_allow_html=True)
st.title('please give us your info so we can predict this question :ship:')
address = st.selectbox("Choose class", Addresses)
area = st.number_input("Input Fare Price", 0,1000)
elevator = st.select_slider("Choose elevator", [0,1])
warehouse = st.select_slider("Choose Warehouse", [0,1])
parking = st.select_slider("Choose parking", [0,1])
room = st.slider("how many room",0,10)

def predict(): 
    result = predict_house(area,int(room),int(parking),int(warehouse), int(elevator),address)
    decimal_value = float(result)
    print(room)

    result = '{:,.0f}'.format(decimal_value)
    st.success(f'your house {result} :thumbsup:')
st.write(f"See your result in top of the page")

trigger = st.button('Predict', on_click=predict)

