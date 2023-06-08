# instalar el paquetes 
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from lib2to3.pgen2.pgen import DFAState
from spellchecker import SpellChecker
from unidecode import unidecode
from plotly.subplots import make_subplots


# leer archivo Inscritos_2016
admin_2014 = pd.read_excel('Administrativos_2014.xlsx',skiprows=7, usecols="A:S")

# explorar datos
print(admin_2014.head())  # muestra las primeras filas del DataFrame
print(admin_2014.info())  # proporciona información sobre las columnas y los tipos de datos

# Redefinir los nombres de las columnas
# Obtener una lista de los nombres de las columnas
nombres_actuales = list(admin_2014.columns)
print(nombres_actuales)
# Definir los nombres nuevos
nombres_nuevos = ['Código_Institución', 'IES_PADRE', 'IES', 'Principal_Seccional', 'Id_Sector_IES', 'Sector_IES', 'Id_Caracter_IES', 'Caracter_IES', 'Código_dpto_(IES)', 'Dpto_domicilio_IES', 'Código_Municipio_(IES)', 'Municipio_domicilio_IES', 'Año', 'Semestre', 'Auxiliar', 'Servicios', 'Profesional', 'Directivo', 'Total']
print(nombres_nuevos)

# Renombrar las columnas utilizando df.rename()
admin_2014 = admin_2014.rename(columns=dict(zip(nombres_actuales, nombres_nuevos)))

# Identificar valores faltantes
print(admin_2014.isnull().sum())
# Eliminar filas con valores faltantes
admin_2014 = admin_2014.dropna()

# Encontrar filas duplicadas basadas en todas las columnas
filas_duplicadas = admin_2014[admin_2014.duplicated(keep=False)]
# Imprimir las filas duplicadas
print(filas_duplicadas)


# Crear una figura de Plotly
fig = go.Figure()
# Grafica semestre versus administrativos
fig.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Auxiliar'], name='Auxiliar'))
fig.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Servicios'], name='Servicios'))
fig.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Profesional'], name='Profesional'))
fig.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Directivo'], name='Directivo'))
# Personalizar el diseño del gráfico
fig.update_layout(title='Datos por semestre y administrativos',
                  xaxis_title='Semestre',
                  yaxis_title='Cantidad',
                  barmode='group')
# Mostrar el gráfico
fig.show()

# Grafica administrativos año 2016
fig = go.Figure()
fig.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Auxiliar'], name='Auxiliar'))
fig.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Servicios'], name='Servicios'))
fig.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Profesional'], name='Profesional'))
fig.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Directivo'], name='Directivo'))
# Personalizar el diseño del gráfico
fig.update_layout(title='',
                  xaxis_title='Institución de Educación Superior (IES)',
                  yaxis_title='Cantidad',
                  barmode='group')
# Mostrar el gráfico
fig.show()

#Grafica 3
fig = go.Figure()
fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['1980', '2007'])
fig.add_trace(go.Pie(labels=labels, values=[4, 7, 1, 7, 0.5], scalegroup='one',
                     name="World GDP 1980"), 1, 1)
fig.add_trace(go.Pie(labels=labels, values=[21, 15, 3, 19, 1], scalegroup='one',
                     name="World GDP 2007"), 1, 2)

fig.update_layout(title_text='World GDP')
fig.show()
 
# Create subplots: use 'domain' type for Pie subplot

fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}],
                                              [{'type': 'pie'}, {'type': 'pie'}]])
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Auxiliar'], name="Auxiliar"),
              1, 1)
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Servicios'], name="Servicios"),
              1, 2)
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Profesional'], name="Profesional"),
              2, 1)
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Directivo'], name="Directivo"),
              2, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="percent+name")

fig.update_layout(
    title_text="Global Emissions 1990-2011",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Auxiliar', x=0.18, y=0.5, font_size=8, showarrow=False),
                 dict(text='Servicios', x=0.82, y=0.5, font_size=8, showarrow=False),
                 dict(text='Profesional', x=0.18, y=0.5, font_size=8, showarrow=False),
                 dict(text='Directivo', x=0.82, y=0.5, font_size=8, showarrow=False)])
fig.show()

fig = px.pie(admin_2014, values='Auxiliar', names='Dpto_domicilio_IES',
             title='Population of American continent',
             hover_data=['Auxiliar'], labels={'lifeExp':'life expectancy'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

print(admin_2014)