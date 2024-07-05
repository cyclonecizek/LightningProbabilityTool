import streamlit as st
import numpy as np
import pandas as pd
from prediction import predict

def main():

  st.title('Cape Canaveral Lightning Probability Tool')
  st.markdown('Input parameters from 10Z KXMR sounding')

  st.header('Sounding Parameters')
  col1, col2 = st.columns(2)
  with col1:
    Thompson_Index = st.number_input('Thompson Index (KI - LI)', 0.0, 60.0, step = 0.1, format= "%.1f"%)
    RH = st.number_input('700-500mb Average RH', 0, 100, step=1)
  with col2:
    #wind_average = st.slider('1000-700mb Average U-Wind Component', -40.0, 40.0, 0.5)
    wind_speed = st.number_input('1000-700mb Average Wind Speed', 0.0, 100.0, step= 0.1, format= "%.1f"%)
    wind_direction = st.number_input('1000-700mb Average Wind Direction', 0, 360, step = 1)

  if st.button('Probability of Lightning'):
    #result = predict(np.array([[Thompson_Index, wind_average]]))

    wind_average = wind_speed * np.cos(np.deg2rad(270-wind_direction))

    result = predict(np.array([[Thompson_Index, wind_average, RH]]))
    #result_str = str(int(result[0])) + '%'
    st.header(str(int(result[0])) + '%')

if __name__=='__main__': 
    main()
  



