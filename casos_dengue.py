import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#Cargando base de datos previamente descargada
data = pd.read_csv('dengue_data.csv')

#Seleccionando los datos de interes
dataset = data[['EDAD_ANOS','ESTATUS_CASO','FECHA_SIGN_SINTOMAS']]

#Eliminando estatus 1 y 3, y quedandonos con el 2(Confirmado)
dataset = dataset.loc[dataset["ESTATUS_CASO"] == 2]

#Definiendo funcion de clasificacion
def class_age(age):
    classification = ''
    if age < 12:
        classification = 'Infante'
    elif age < 27:
        classification = 'Joven'
    elif age < 60:
        classification = 'Adulto'
    else:
        classification = 'Anciano'
    return classification

#Generando columna de clasificacion segun edad
dataset.insert(1, "CLASIFICACION", [class_age(age) for age in dataset.EDAD_ANOS])

#Preparando los datos para graficar
dataset_class = dataset.groupby(['CLASIFICACION']).count().iloc[:,0]
dataset_date = dataset.groupby(['FECHA_SIGN_SINTOMAS']).count().iloc[:,0]

#Graficando
fig = make_subplots(rows=1, cols=2,column_widths=[0.55, 0.45])

fig.add_trace(#Casos por Fecha
    go.Scatter(x=dataset_date.index, y=dataset_date.values,name='Casos confirmados'),
    row=1, col=1
)

fig.add_trace(#Casos por clasificacion de edad
    go.Bar(x=dataset_class.index, y=dataset_class.values,name='Casos confirmados'),
    row=1, col=2
)

fig.update_layout(height=400, width=800, title_text="Casos de Dengue Confirmados en Mexico",showlegend=False)
fig.show()
fig.write_html("./fig.html")