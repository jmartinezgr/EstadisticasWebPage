from django.shortcuts import render,redirect
from django.http import Http404
import pandas as pd

# Create your views here.

def home(request):
    
    return render(request,'general_pages/home.html')

def drop(request, actividad=''):
    if request.method == 'POST':
        file = request.FILES.get('hidden_file_input')
        if file:
            print('YES')
            df = pd.read_excel(file)
            column_number = request.POST.get('manual_data', [0])
            if column_number:
                column_number = int(column_number[0])
                print('Número de Columna seleccionada:', column_number)
                # Ahora puedes usar el número de columna en tus operaciones
                if column_number < len(df.columns):
                    selected_column = df.iloc[:, column_number]
                    print(selected_column.head())
                    # Realiza tus operaciones con la columna seleccionada
        else:
            manual_data = request.POST.get('manual_data').split(',')
            print(manual_data)
        #return redirect('services_without_section')
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