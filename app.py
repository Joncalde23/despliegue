import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')