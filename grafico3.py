import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector

# Función para generar la gráfica de barras
def generar_grafica():
    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='batch_record'
    )

    # Obtener los datos de la base de datos
    cursor = conn.cursor()
    cursor.execute('SELECT id_batch, unidad_lote FROM `batch` where id_batch > 2770')
    resultados = cursor.fetchall()

    # Extraer los valores de las categorías y cantidades
    id = [resultado[0] for resultado in resultados]
    tamano = [resultado[1] for resultado in resultados]

    # Crear el gráfico de barras
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(id, tamano)
    ax.set_xlabel('Id')
    ax.set_ylabel('Tamaño')
    ax.set_title('Tabla de Barras')

    # Crear el widget FigureCanvasTkAgg para mostrar la gráfica en la ventana
    canvas = FigureCanvasTkAgg(fig, master=pane)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Crear la tabla
    tabla = ttk.Treeview(pane)
    tabla['columns'] = ('Id', 'Tamaño')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('Id', anchor=tk.CENTER, width=100)
    tabla.column('Tamaño', anchor=tk.CENTER, width=100)

    tabla.heading('#0', text='', anchor=tk.CENTER)
    tabla.heading('Id', text='Id', anchor=tk.CENTER)
    tabla.heading('Tamaño', text='Tamaño', anchor=tk.CENTER)

    for i in range(len(id)):
        tabla.insert(parent='', index='end', iid=i, values=(id[i], tamano[i]))

    tabla.pack()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

def guardar_grafica():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', initialdir='C:/Users/erestrepo/Desktop/', filetypes=[('PNG Files', '*.png')])
    plt.savefig(file_path)
    plt.close()

# Crear la ventana de la aplicación
ventana = tk.Tk()

# Crear el widget PanedWindow para dividir la ventana
pane = tk.PanedWindow(ventana, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)

# División 1: Gráfico y tabla
frame1 = tk.Frame(pane)
pane.add(frame1)

# División 2: Vacía
frame2 = tk.Frame(pane)
pane.add(frame2)

# División 3: Vacía
frame3 = tk.Frame(pane)
pane.add(frame3)

# División 4: Vacía
frame4 = tk.Frame(pane)
pane.add(frame4)

# Crear el botón para generar la gráfica
boton_generar = tk.Button(frame1, text='Positivo Aprobados', command=generar_grafica)
boton_generar.pack()

# Ejecutar la aplicación
ventana.mainloop()
