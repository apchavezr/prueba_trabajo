# instalar el paquetes 
import pandas as pd
import numpy as np
from lib2to3.pgen2.pgen import DFAState
from spellchecker import SpellChecker
from unidecode import unidecode

# leer archivo Inscritos_2016
data = pd.read_excel('articles-391559_recurso.xlsx',skiprows=6, usecols="A:AG")

# explorar datos
print(data.head())  # muestra las primeras filas del DataFrame
print(data.info())  # proporciona información sobre las columnas y los tipos de datos

# Redefinir los nombres de las columnas
# Obtener una lista de los nombres de las columnas
nombres_actuales = list(data.columns)
print(nombres_actuales)
# Definir los nombres nuevos
nombres_nuevos = ['codigo_Inst', 'IES_PADRE', 'IES', 'Principal_Seccional', 'ID_Sector-IES', 'Sector_IES', 'ID_Caracter', 'Caracter_IES', 'Codigo_departamento', 'Dpto_domicilio_IES', 'codigo_Municipio_IES', 'Municipio_domicilio_IES', 'Codigo_SNIES_programa', 'Programa_Academico', 'ID_Nivel_Academico', 'Nivel_Academico', 'ID_Nivel_Formacion', 'Nivel_Formacion', 'ID_Metodologia', 'Metodologia', 'ID_area', 'Area_conocimiento', 'Id_nucleo', 'Nucleo_basico_conoci', 'Codigo_Departamento_(Programa)', 'Dpto_oferta_programa', 'Codigo_municipio_(programa)', 'Municipio_oferta_programa', 'ID_sexo', 'Sexo', 'Ano', 'Semestre', 'Inscritos']
print(nombres_nuevos)

# Renombrar las columnas utilizando df.rename()
data = data.rename(columns=dict(zip(nombres_actuales, nombres_nuevos)))
print(data)

# Identificar valores faltantes
print(data.isnull().sum())
# Eliminar filas con valores faltantes
data = data.dropna()

# Identificar registos duplicados
print(data.duplicated().sum())
# Eliminar registros duplicados en todas las columnas
data = data.drop_duplicates()

# Estandarizar el formato de los datos
# Funciones para pasar texto de minúscula a mayúscula
# Aplicar la función upper() a las columnas
data[['Sector_IES', 'Caracter_IES', 'Dpto_domicilio_IES', 
      'Municipio_domicilio_IES','Area_conocimiento', 'Nucleo_basico_conoci','Dpto_oferta_programa','Municipio_oferta_programa','Nivel_Academico','Nivel_Formacion','Metodologia']] = data[['Sector_IES', 'Caracter_IES', 
                                            'Dpto_domicilio_IES', 'Municipio_domicilio_IES',
                                            'Area_conocimiento', 'Nucleo_basico_conoci',
                                           'Dpto_oferta_programa',
                                        'Municipio_oferta_programa','Nivel_Academico','Nivel_Formacion','Metodologia']].applymap(str.upper)
 
# Corregir texto de las columnas  
data['Dpto_domicilio_IES'] = data['Dpto_domicilio_IES'].str.replace('Bogotá D.C', 'BOGOTA D.C.')
data['Dpto_oferta_programa'] = data['Dpto_oferta_programa'].str.replace('Bogotá D.C', 'BOGOTA D.C.')
data['Municipio_oferta_programa'] = data['Municipio_oferta_programa'].str.replace('Bogota', 'BOGOTA D.C.')
data['Programa_Academico'] = data['Programa_Academico'].str.replace('ADMINISTRACI¿N DE EMPRESAS', 'ADMINISTRACIÓN DE EMPRESAS')

#Manejo de tildes en el texto
# Aplicar la función unidecode()
data[['Sector_IES', 'Caracter_IES', 'Dpto_domicilio_IES', 
      'Municipio_domicilio_IES','Area_conocimiento', 'Nucleo_basico_conoci','Dpto_oferta_programa','Municipio_oferta_programa','Nivel_Academico','Nivel_Formacion','Metodologia']] = data[['Sector_IES', 'Caracter_IES', 
                                            'Dpto_domicilio_IES', 'Municipio_domicilio_IES',
                                            'Area_conocimiento', 'Nucleo_basico_conoci',
                                           'Dpto_oferta_programa',
                                        'Municipio_oferta_programa','Nivel_Academico','Nivel_Formacion','Metodologia']].applymap(unidecode)
 
# Encontrar filas duplicadas basadas en todas las columnas
filas_duplicadas = data[data.duplicated(keep=False)]
# Imprimir las filas duplicadas
print(filas_duplicadas)

# En caso de que existan filas duplicadas se utiliza el método groupby()
# en combinación con alguna función de agregación, como sum(), mean(), count(), entre otras.

#En caso de que se requiera transformar dato se pueden usar las funciones
# métodos astype() o to_numeric() para cambiar los tipos de datos de una o varias columnas. 



# Exportar el DataFrame a un archivo de Excel
data.to_excel('archivo.xlsx', index=False)

print(data)


