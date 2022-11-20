import streamlit as st
import pandas as pd
import main
import imageio as iio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import locatiom
import json
from urllib.request import urlopen

import matplotlib.image as mpimg

st.title('Test')

tabs = st.tabs(['Intro', 'Get Started', 'Get Help'])

tab_intro = tabs[1]

with tab_intro:
    st.header("Upload Biometric Data")

    uf = st.file_uploader(label="Biometrics",
                          type=['img', 'png','bmp'])

    if uf is not None:
        print(uf)

    try:
        img = cv2.imread(uf)
    except Exception as e:
        print(e)

    health_Score = main.prediction(uf)
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    city = data.get('city')

    special_Doctors = (['General','General', 'Diabeties', 'Cadiovascular', 'Nueralogist', 'Pulmonology'])
    i = health_Score
    print(special_Doctors[3])
    find_loc = locatiom.getDocs(str(special_Doctors[i]) + ' Hospitals in ' + city)


    if (health_Score == 0 or health_Score == 1):
        st.write('You are Healthy')
        st.markdown('--------------------------------------------')
        st.write('Here are some General Physicians nearby')
        st.write(find_loc)
        st.map

    elif (health_Score == 2):
        st.write('Our model predicts that you might have Diabeties')
        st.markdown('--------------------------------------------')
        st.write('Here are some Doctors nearby that specialize in Diabeties')
        st.write(find_loc)
        st.map

    elif (health_Score == 3):
        st.write('Our model predicts that you might have Heart Diseases')
        st.markdown('--------------------------------------------')
        st.write('Here are some Doctors nearby that specialize in Cadiovascular Diseases')
        st.write(find_loc)
        st.map
    elif (health_Score == 4):
        st.write('Our model predicts that you might have Multiple Sclerosis')
        st.markdown('--------------------------------------------')
        st.write('Here are some Nueralogist in your area')
        st.write(find_loc)
        st.map
    elif (health_Score == 5):
        st.write('Our model predicts that you might have Asthma')
        st.markdown('--------------------------------------------')
        st.write('Here are some Pulmonologist in your area')
        st.write(find_loc)
        st.map




with tabs[2]:

    st.write('test')





