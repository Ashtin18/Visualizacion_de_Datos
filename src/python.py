from distutils.command.upload import upload
from importlib.resources import path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from PIL import Image

st.title('Proyecto Visualización de Datos')
path=("https://raw.githubusercontent.com/Ashtin18/Visualizacion_de_Datos/main/data/VentasTienda.csv")

def load_data(nrows):
    data = pd.read_csv(path, nrows=nrows,delimiter=";")
    return data

data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Mostar Datos'):
    st.text('Datos Crudos')
    st.write(data)

st.set_option('deprecation.showPyplotGlobalUse', False)

#####################################################################################################