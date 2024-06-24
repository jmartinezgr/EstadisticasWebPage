from django.shortcuts import render,redirect
from django.http import Http404
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np

# Create your views here.

def home(request):
    
    return render(request,'general_pages/home.html')

def show_grafico(request, image_base64, data, pd):
    return render(request, 'general_pages/show_grafico.html', {'image_base64': image_base64, 'data': data, 'pd': pd})

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

                if manual_data:
                    data = df.iloc[:, int(manual_data)]
                    manual_data_array = np.array(data) 
        else:
            manual_data = request.POST.get('manual_data').split(',')
            # Convertir manual_data a un arreglo de NumPy
            manual_data_array = np.array(manual_data, dtype=int)

            if not manual_data_array.size:
                print('No se proporcionaron datos')
                return render(request, 'general_pages/drop.html')

        if actividad == 'Grafico de Barras':
            try:
                
                # Crear el objeto BytesIO antes de guardar la figura
                image_stream = BytesIO()

                ocurrencias = np.bincount(manual_data_array)
                valores = np.arange(len(ocurrencias))

                # Colores diferentes para cada barra
                colores = plt.cm.viridis(np.linspace(0, 1, len(ocurrencias)))

                plt.bar(valores, ocurrencias, width=0.8, align='center', color=colores)
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                plt.title('Histograma de ocurrencias')

                # Agregar labels
                for valor, frecuencia in zip(valores, ocurrencias):
                    plt.text(valor, frecuencia, str(frecuencia), ha='center', va='bottom')

                plt.savefig(image_stream, format='png')
                image_stream.seek(0)
                plt.close()

                image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

                return show_grafico(request, image_base64, manual_data_array, True if file else False)
            
            except RuntimeError:
                raise Http404("Sección no válida")

        elif actividad == 'Grafico de Pastel':
            try:
                # Crear el objeto BytesIO antes de guardar la figura
                image_stream = BytesIO()

                # Graficar el gráfico de pastel
                ocurrencias = np.bincount(manual_data_array)
                labels = np.arange(len(ocurrencias)).astype(str)
                plt.pie(ocurrencias, labels=labels, autopct='%1.1f%%', startangle=140)
                plt.title(f'Gráfico de Pastel - {manual_data}')
                # Puedes personalizar el gráfico según tus necesidades
                plt.axis('equal')  # Asegura que el gráfico de pastel se vea circular
                plt.title('Gráfico de Pastel de Ocurrencias')
                # Guardar la figura en un BytesIO para mostrarla en la plantilla
                plt.savefig(image_stream, format='png')
                image_stream.seek(0)
                plt.close()

                # Convertir la imagen a base64 para mostrarla en la plantilla
                image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

                return show_grafico(request, image_base64, ocurrencias, True if file else False)
            except RuntimeError:
                raise Http404("Sección no válida")
        elif actividad == 'Grafico de Caja 1 Variable':
            try:
                # Lógica para el gráfico de caja
                image_stream = BytesIO()

                # Crea el gráfico de caja
                plt.boxplot(manual_data_array, vert=False)
                plt.xlabel('Valores')
                plt.title('Gráfico de Caja de una Sola Variable')

                # Guarda la figura en un BytesIO para mostrarla en la plantilla
                plt.savefig(image_stream, format='png')
                image_stream.seek(0)
                plt.close()

                # Convierte la imagen a base64 para mostrarla en la plantilla
                image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

                return show_grafico(request, image_base64, [], True if file else False)
            except RuntimeError:
                raise Http404("Sección no válida")
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