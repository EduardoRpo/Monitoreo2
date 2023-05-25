import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
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
    plt.bar(id, tamano)
    plt.xlabel('Id')
    plt.ylabel('Tamaño')
    plt.title('Tabla de Barras')

      # Crear la tabla
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title('Tabla de Datos')

    tabla = ttk.Treeview(ventana_tabla)
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

    # Mostrar el gráfico
    plt.show()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

def guardar_grafica():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', initialdir='C:/Users/erestrepo/Desktop/', filetypes=[('PNG Files', '*.png')])
    plt.savefig(file_path)
    plt.close()

# Crear la ventana de la aplicación
ventana = tk.Tk()

# Crear el botón para generar la gráfica
boton_generar = tk.Button(ventana, text='Positivo Aprobados', command=generar_grafica)
boton_generar.pack()

# Ejecutar la aplicación
ventana.mainloop()
