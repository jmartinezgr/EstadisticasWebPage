from django.shortcuts import render,redirect
from django.http import Http404
import pandas as pd
import numpy as np

# Create your views here.

def home(request):
    
    return render(request,'general_pages/home.html')

import pandas as pd
from django.shortcuts import render, redirect

def drop(request, actividad=''):
    if request.method == 'POST':
        file = request.FILES.get('hidden_file_input')
        if file:
            # Verificar el tipo de archivo
            allowed_extensions = ['xlsx', 'csv']
            file_extension = file.name.split('.')[-1].lower()

            if file_extension in allowed_extensions:
                # Cargar el archivo con pandas
                if file_extension == 'xlsx':
                    df = pd.read_excel(file)
                elif file_extension == 'csv':
                    df = pd.read_csv(file)

                # Obtener las columnas especificadas en el textarea
                manual_data = request.POST.get('manual_data')
                selected_columns = []

                if manual_data:
                    # Dividir las columnas especificadas por comas y convertirlas a una lista
                    selected_columns = [int(col.strip()) for col in manual_data.split(',')]

                    # Filtrar el DataFrame por las columnas seleccionadas
                    df = df.iloc[:, selected_columns]

                    print('Columnas Seleccionadas:')
                    print(df.head())

                return redirect('services_without_section')
            else:
                print('Tipo de archivo no permitido')
        else:
            manual_data = request.POST.get('manual_data').split(',')

            # Convertir manual_data a un arreglo de NumPy
            manual_data_array = np.array(manual_data, dtype=float)

            # Realizar acciones según la solicitud
            action = request.POST.get('action')  # Asumiendo que hay un campo 'action' en tu formulario

            #if action == 'grafico_de_barras':
                # Lógica para grafico_de_barras
                # Puedes pasar manual_data_array a tu vista para generar el gráfico

                #return render(request, 'general_pages/grafico_de_barras.html', {'data': manual_data_array})

            #elif action == 'grafico_pastel':
                # Lógica para grafico_pastels
                #return render(request, 'general_pages/grafico_pastel.html', {'data': manual_data_array})

            #elif action == 'box_plot_1_variable':
                #return render(request, 'general_pages/box_plot_1_variable.html', {'data': manual_data_array})

    return render(request, 'general_pages/drop.html')

def services(request,seccion = ''):

    opciones_validas = ['graficos', 'resumenes', 'pruebas']
    if seccion and seccion not in opciones_validas:
        raise Http404("Sección no válida")

    servicios =[
        [
            {
                'name':'Grafico de Barras',
                'imagen' : 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/bar_diagram.jpg',
                'descripcion':'Este grafico sirve para verificar la frecuencia de valores en un conjunto de datos',
                'uso':'sin_registro'
            },
            {
                'name':'Grafico de Pastel',
                'imagen' : 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/cake_diagram.png',
                'descripcion':'Este grafico sirve para verificar los porcentajes de los valores frecuentes en un conjunto de datos',
                'uso':'sin_registro'
            },
            {
                'name': 'Grafico de Caja 1 Variable',
                'imagen' : 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/box_plot_diagram.jpg',
                'descripcion':'Este grafico sirve para verificar de que manera se',
                'uso':'sin_registro'
            },
            {
                'name': 'Grafico de Caja X Variables',
                'imagen' : 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/box_plot_diagram_1.jpg',
                'descripcion':'Este grafico sirve para verificar los porcentajes de los valores frecuentes en un conjunto de datos',
                'uso':'con_registro'
            },
            {
                'name': 'Histograma',
                'imagen' : 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/histograma_diagram.png',
                'descripcion':'Este grafico sirve para verificar los porcentajes de los valores frecuentes en un conjunto de datos',
                'uso':'con_registro'
            }
        ],
        [
            {
                'name':'Resumen General',
                'imagen': 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/summary_image.jpg',
                'descripcion' : 'Informacion general de un conjunto de datos, como su media, mediana, etc..',
                'uso':'sin_registro'
            },
            {
                'name':'Resumen Especifico',
                'imagen': 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/specific_summary.png',
                'descripcion' : 'Informacion general de un conjunto de datos, como su media, mediana, etc..',
                'uso':'con_registro'
            },
        ],
        [
            {
                'name':'Bondad de Ajuste',
                'imagen': 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/bondad_ajuste.jpg',
                'descripcion' : 'Informacion general de un conjunto de datos, como su media, mediana, etc..',
                'uso':'con_registro'
            },
            {
                'name':'Intervalos de Confianza',
                'imagen': 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/intervals.jpeg',
                'descripcion' : 'Informacion general de un conjunto de datos, como su media, mediana, etc..',
                'uso':'con_registro'
            },
            {
                'name':'Pruebas de Hipotesis',
                'imagen': 'https://raw.githubusercontent.com/jmartinezgr/FotosToMyWebs/main/TuPrimerAnalisis/services/hipotesis.jpeg',
                'descripcion' : 'Informacion general de un conjunto de datos, como su media, mediana, etc..',
                'uso':'con_registro'
            },
        ]
    ]

    if seccion == 'graficos':
        servicios_filtrados = servicios[0]
    elif seccion == 'resumenes':
        servicios_filtrados = servicios[1]
    elif seccion == 'pruebas':
        servicios_filtrados = servicios[2]
    else:
        servicios_filtrados = servicios

    return render(request,'general_pages/services.html',{'servicios':servicios_filtrados,'seccion': seccion})