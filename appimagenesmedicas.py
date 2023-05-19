import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class IMAGENMEDICA:
    def __init__(self, Idimagen, tipo, especialidad, edadPac, seccionCur, lugar, diagnostico):
        self.Idimagen = Idimagen
        self.tipo = tipo
        self.especialidad = especialidad
        self.edadPac = edadPac
        self.seccionCur = seccionCur
        self.lugar = lugar
        self.diagnostico = diagnostico
        self.ruta_imagen = ""

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen")
        self.ruta_imagen = ruta_imagen

class Aplicacion:
    def __init__(self):
        self.imagenes = []

        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Imágenes Médicas")

        # Etiquetas y cajas de texto para ingresar los valores de las variables
        self.label_idimagen = tk.Label(self.ventana, text="ID Imagen")
        self.label_idimagen.pack()
        self.entry_idimagen = tk.Entry(self.ventana)
        self.entry_idimagen.pack()

        self.label_tipo = tk.Label(self.ventana, text="Tipo")
        self.label_tipo.pack()
        self.entry_tipo = tk.Entry(self.ventana)
        self.entry_tipo.pack()

        self.label_especialidad = tk.Label(self.ventana, text="Especialidad")
        self.label_especialidad.pack()
        self.entry_especialidad = tk.Entry(self.ventana)
        self.entry_especialidad.pack()

        self.label_edadPac = tk.Label(self.ventana, text="Edad Paciente")
        self.label_edadPac.pack()
        self.entry_edadPac = tk.Entry(self.ventana)
        self.entry_edadPac.pack()

        self.label_seccionCur = tk.Label(self.ventana, text="Sección Curada")
        self.label_seccionCur.pack()
        self.entry_seccionCur = tk.Entry(self.ventana)
        self.entry_seccionCur.pack()

        self.label_lugar = tk.Label(self.ventana, text="Lugar")
        self.label_lugar.pack()
        self.entry_lugar = tk.Entry(self.ventana)
        self.entry_lugar.pack()

        self.label_diagnostico = tk.Label(self.ventana, text="Diagnóstico")
        self.label_diagnostico.pack()
        self.entry_diagnostico = tk.Entry(self.ventana)
        self.entry_diagnostico.pack()

        # Crear Treeview
        self.treeview = ttk.Treeview(self.ventana)
        self.treeview["columns"] = ("Idimagen", "tipo", "especialidad", "edadPac", "seccionCur", "lugar", "diagnostico", "ruta_imagen")
        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0", width=50)
        self.treeview.heading("Idimagen", text="ID Imagen")
        self.treeview.column("Idimagen", width=100)
        self.treeview.heading("tipo", text="Tipo")
        self.treeview.column("tipo", width=100)
        self.treeview.heading("especialidad", text="Especialidad")
        self.treeview.column("especialidad", width=100)
        self.treeview.heading("edadPac", text="Edad Paciente")
        self.treeview.column("edadPac", width=100)
        self.treeview.heading("seccionCur", text="Sección Curada")
        self.treeview.column("seccionCur", width=100)
        self.treeview.heading("lugar", text="Lugar")
        self.treeview.column("lugar", width=100)
        self.treeview.heading("diagnostico", text="Diagnóstico")
        self.treeview.column("diagnostico", width=200)
        self.treeview.heading("ruta_imagen", text="Ruta Imagen")
        self.treeview.column("ruta_imagen", width=200)
        self.treeview.pack()

        # Botón para cargar imagen
        self.boton_cargar_imagen = tk.Button(self.ventana, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar_imagen.pack()

        # Botón para mostrar tabla
        self.boton_mostrar_tabla = tk.Button(self.ventana, text="Mostrar Tabla", command=self.mostrar_tabla)
        self.boton_mostrar_tabla.pack()

        self.ventana.mainloop()

    def cargar_imagen(self):
        Idimagen = self.entry_idimagen.get()
        tipo = self.entry_tipo.get()
        especialidad = self.entry_especialidad.get()
        edadPac = self.entry_edadPac.get()
        seccionCur = self.entry_seccionCur.get()
        lugar = self.entry_lugar.get()
        diagnostico = self.entry_diagnostico.get()

        imagen = IMAGENMEDICA(Idimagen, tipo, especialidad, edadPac, seccionCur, lugar, diagnostico)
        imagen.cargar_imagen()
        self.imagenes.append(imagen)

    def mostrar_tabla(self):
        # Limpiar la tabla
        self.treeview.delete(*self.treeview.get_children())

        # Insertar datos en la tabla
        for imagen in self.imagenes:
            self.treeview.insert("", "end", text=imagen.Idimagen,
                                 values=(imagen.Idimagen, imagen.tipo, imagen.especialidad, imagen.edadPac,
                                         imagen.seccionCur, imagen.lugar, imagen.diagnostico, imagen.ruta_imagen))

Aplicacion()
