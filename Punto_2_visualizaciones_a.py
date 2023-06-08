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
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Auxiliar'], name="Auxiliar",
               scalegroup='one'), 1, 1)
fig.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Servicios'], name="Servicios", 
                     scalegroup='one'), 1, 2)

fig.update_layout(title_text='World GDP')
fig.show()
 
# figura 4 total de administrativos por Municipio_domicilio_IES
fig = go.Figure()
fig = px.pie(admin_2014, values='Total', names='Municipio_domicilio_IES',
             title='Total de administrativos por Municipio de IES',
             hover_data=['Total'] )
fig.update_traces(textposition='inside', textinfo='percent')
fig.show()

print(admin_2014)