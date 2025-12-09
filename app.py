import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
st.set_page_config(page_title='Análisis de Anuncios de Venta de Coches', layout='wide')

st.title('Análisis de Anuncios de Venta de Coches')
st.header('Dataframe:')
st.dataframe(car_data)

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histogramas
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')
if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_disp = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    ))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_disp.update_layout(title_text='Dispersión entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_disp, use_container_width=True)

show_plot = st.checkbox('Mostrar gráfico de líneas de precios promedio por tipo de vehiculo')
if show_plot:
    st.write('Creación de un gráfico de líneas para el precio promedio por tipo de vehiculo de los anuncios de venta de coches')

    

    # Agrupar los datos por año y calcular el precio promedio
    avg_price_per_year = car_data.groupby('type')['price'].mean().reset_index()

    # Crear un gráfico de líneas utilizando plotly.graph_objects
    fig_line = go.Figure(data=go.Scatter(
        x=avg_price_per_year['type'],
        y=avg_price_per_year['price'],
        mode='lines+markers'
    ))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_line.update_layout(title_text='Precio Promedio por tipo de vehiculo')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_line, use_container_width=True)