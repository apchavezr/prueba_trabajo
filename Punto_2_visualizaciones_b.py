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
print(admin_2014)

# Crear una figura de Plotly
fig1 = go.Figure()
# Figura 1 semestre versus administrativos
fig1.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Auxiliar'], name='Auxiliar'))
fig1.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Servicios'], name='Servicios'))
fig1.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Profesional'], name='Profesional'))
fig1.add_trace(go.Bar(x=admin_2014['Semestre'], y=admin_2014['Directivo'], name='Directivo'))
# Personalizar el diseño del gráfico
fig1.update_layout(title='Datos por semestre y administrativos',
                  xaxis_title='Semestre',
                  yaxis_title='Cantidad',
                  barmode='group')
# Mostrar el gráfico
fig1.show()

# Figura 2 administrativos año 2016
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Auxiliar'], name='Auxiliar'))
fig2.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Servicios'], name='Servicios'))
fig2.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Profesional'], name='Profesional'))
fig2.add_trace(go.Bar(x=admin_2014['Sector_IES'], y=admin_2014['Directivo'], name='Directivo'))
# Personalizar el diseño del gráfico
fig2.update_layout(title='',
                  xaxis_title='Institución de Educación Superior (IES)',
                  yaxis_title='Cantidad',
                  barmode='group')
# Mostrar el gráfico
fig2.show()

#Grafica 3 administrativo por caracter IES
fig3 = go.Figure()
fig3 = make_subplots(2, 2, specs=[[{'type':'pie'}, {'type':'pie'}],[{'type':'pie'}, {'type':'pie'}]],
                    subplot_titles=['Auxiliar', 'Servicios', 'Profesional', 'Directivo'])
fig3.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Auxiliar'], name="Auxiliar",
               scalegroup='one'), 1, 1)
fig3.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Servicios'], name="Servicios", 
                     scalegroup='one'), 1, 2)
fig3.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Profesional'], name="Profesional", 
                     scalegroup='one'), 2, 1)
fig3.add_trace(go.Pie(labels=admin_2014['Caracter_IES'], values=admin_2014['Directivo'], name="Directivo", 
                     scalegroup='one'), 2, 2)
fig3.update_layout(title_text='Administrativo por caracter IES',uniformtext_minsize=8, uniformtext_mode='hide')
fig3.show()
 
# figura 4 total de administrativos por Municipio_domicilio_IES
fig4 = go.Figure()
admin_2014.loc[admin_2014['Total'] > 0.50, 'Municipio_domicilio_IES'] # Represent only large countries
fig4 = px.pie(admin_2014, values='Total', names='Municipio_domicilio_IES', title='Total de administrativos por Municipio de domicilio IES')
fig4.update_traces(textposition='inside', textinfo='percent')
fig4.show()
 

