import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector

# Función para ejecutar la consulta y mostrar la gráfica de barras y la tabla
def mostrar_grafica_barras_y_tabla():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='batch_record'
    )

    # Ejecutar la consulta para obtener los datos
    cursor = conn.cursor()
    cursor.execute('SELECT id_batch, unidad_lote FROM `batch` where id_batch > 2770')
    resultados = cursor.fetchall()

    # Extraer los valores de las categorías y cantidades
    id = [resultado[0] for resultado in resultados]
    tamano = [resultado[1] for resultado in resultados]

    # Crear la figura y el eje para la gráfica de barras
    fig = plt.Figure(figsize=(4, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(id, tamano)
    ax.set_xlabel('Id')
    ax.set_ylabel('Tamaño')
    ax.set_title('Gráfica de Barras')

    # Crear el widget FigureCanvasTkAgg para mostrar la gráfica en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

    # Crear la tabla
    tabla = ttk.Treeview(ventana)
    tabla['columns'] = ('Id', 'Tamaño')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('Id', anchor=tk.CENTER, width=100)
    tabla.column('Tamaño', anchor=tk.CENTER, width=100)

    tabla.heading('#0', text='', anchor=tk.CENTER)
    tabla.heading('Id', text='Id', anchor=tk.CENTER)
    tabla.heading('Tamaño', text='Tamaño', anchor=tk.CENTER)

    for i in range(len(id)):
        tabla.insert(parent='', index='end', iid=i, values=(id[i], tamano[i]))

    tabla.grid(row=0, column=1, padx=10, pady=10)

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

# Función para ejecutar la consulta y mostrar la gráfica de línea y la tabla
def mostrar_grafica_linea_y_tabla():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='batch_record'
    )

    # Ejecutar la consulta para obtener los datos
    cursor = conn.cursor()
    cursor.execute('SELECT id_batch, unidad_lote FROM `batch` where id_batch > 1500')
    resultados = cursor.fetchall()

    # Extraer los valores de las categorías y cantidades
    id = [resultado[0] for resultado in resultados]
    tamano = [resultado[1] for resultado in resultados]

    # Crear la figura y el eje para la gráfica de línea
    fig = plt.Figure(figsize=(3, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(id, tamano)
    ax.set_xlabel('Id')
    ax.set_ylabel('Tamaño')
    ax.set_title('Gráfica de Línea')

    # Crear el widget FigureCanvasTkAgg para mostrar la gráfica en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=2, padx=10, pady=10)

    # Crear la tabla
    tabla = ttk.Treeview(ventana)
    tabla['columns'] = ('Id', 'Tamaño')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('Id', anchor=tk.CENTER, width=100)
    tabla.column('Tamaño', anchor=tk.CENTER, width=100)

    tabla.heading('#0', text='', anchor=tk.CENTER)
    tabla.heading('Id', text='Id', anchor=tk.CENTER)
    tabla.heading('Tamaño', text='Tamaño', anchor=tk.CENTER)

    for i in range(len(id)):
        tabla.insert(parent='', index='end', iid=i, values=(id[i], tamano[i]))

    tabla.grid(row=0, column=3, padx=10, pady=10)

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

# Crear la ventana de la aplicación
ventana = tk.Tk()

# Configurar el tamaño y posición de la ventana
ventana.geometry("800x400")
ventana.title("Consulta de Datos")

# Centrar la ventana en la pantalla
window_width = ventana.winfo_reqwidth()
window_height = ventana.winfo_reqheight()
position_right = int(ventana.winfo_screenwidth()/2 - window_width/2)
position_down = int(ventana.winfo_screenheight()/2 - window_height/2)
ventana.geometry("+{}+{}".format(position_right, position_down))

# Llamar a la función mostrar_grafica_barras_y_tabla cuando se presione el botón "Consulta 1"
boton_consulta1 = tk.Button(ventana, text='Consulta 1', command=mostrar_grafica_barras_y_tabla)
boton_consulta1.grid(row=1, column=0, padx=10, pady=10)

# Llamar a la función mostrar_grafica_linea_y_tabla cuando se presione el botón "Consulta 2"
boton_consulta2 = tk.Button(ventana, text='Consulta 2', command=mostrar_grafica_linea_y_tabla)
boton_consulta2.grid(row=1, column=1, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
