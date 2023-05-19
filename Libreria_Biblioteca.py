import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Libro:
    def __init__(self, id_libro, titulo, autor, isbn, paginas, edicion, editorial, lugar, disponible, precio):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.disponible = disponible
        self.precio = precio

class BibliotecaApp:
    def __init__(self):
        self.libros = []

        self.window = tk.Tk()
        self.window.title("Biblioteca")

        # Crear etiquetas y campos de entrada
        label_id = tk.Label(self.window, text="ID:")
        label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(self.window)
        self.entry_id.grid(row=0, column=1)

        label_titulo = tk.Label(self.window, text="Título:")
        label_titulo.grid(row=1, column=0)
        self.entry_titulo = tk.Entry(self.window)
        self.entry_titulo.grid(row=1, column=1)

        label_autor = tk.Label(self.window, text="Autor:")
        label_autor.grid(row=2, column=0)
        self.entry_autor = tk.Entry(self.window)
        self.entry_autor.grid(row=2, column=1)

        label_isbn = tk.Label(self.window, text="ISBN:")
        label_isbn.grid(row=3, column=0)
        self.entry_isbn = tk.Entry(self.window)
        self.entry_isbn.grid(row=3, column=1)

        label_paginas = tk.Label(self.window, text="Páginas:")
        label_paginas.grid(row=4, column=0)
        self.entry_paginas = tk.Entry(self.window)
        self.entry_paginas.grid(row=4, column=1)

        label_edicion = tk.Label(self.window, text="Edición:")
        label_edicion.grid(row=5, column=0)
        self.entry_edicion = tk.Entry(self.window)
        self.entry_edicion.grid(row=5, column=1)

        label_editorial = tk.Label(self.window, text="Editorial:")
        label_editorial.grid(row=6, column=0)
        self.entry_editorial = tk.Entry(self.window)
        self.entry_editorial.grid(row=6, column=1)

        label_lugar = tk.Label(self.window, text="Lugar:")
        label_lugar.grid(row=7, column=0)
        self.entry_lugar = tk.Entry(self.window)
        self.entry_lugar.grid(row=7, column=1)

        label_disponible = tk.Label(self.window, text="Disponible:")
        label_disponible.grid(row=8, column=0)
        self.entry_disponible = tk.Entry(self.window)
        self.entry_disponible.grid(row=8, column=1)

        label_precio = tk.Label(self.window, text="Precio:")
        label_precio.grid(row=9, column=0)
        self.entry_precio = tk.Entry(self.window)
        self.entry_precio.grid(row=9, column=1)

        # Botones
        button_insertar = tk.Button(self.window, text="Insertar", command=self.insertar_libro)
        button_insertar.grid(row=10, column=0)

        button_modificar = tk.Button(self.window, text="Modificar", command=self.modificar_libro)
        button_modificar.grid(row=10, column=1)

        button_listar = tk.Button(self.window, text="Listar", command=self.listar_libros)
        button_listar.grid(row=10, column=2)

        button_borrar = tk.Button(self.window, text="Borrar", command=self.borrar_libro)
        button_borrar.grid(row=10, column=3)

        # Tabla
        self.tree = ttk.Treeview(self.window)
        self.tree["columns"] = ("id", "titulo", "autor", "isbn", "paginas", "edicion", "editorial", "lugar", "disponible", "precio")
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=50)
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=100)
        self.tree.heading("titulo", text="Título")
        self.tree.column("titulo", width=200)
        self.tree.heading("autor", text="Autor")
        self.tree.column("autor", width=150)
        self.tree.heading("isbn", text="ISBN")
        self.tree.column("isbn", width=100)
        self.tree.heading("paginas", text="Páginas")
        self.tree.column("paginas", width=100)
        self.tree.heading("edicion", text="Edición")
        self.tree.column("edicion", width=100)
        self.tree.heading("editorial", text="Editorial")
        self.tree.column("editorial", width=150)
        self.tree.heading("lugar", text="Lugar")
        self.tree.column("lugar", width=100)
        self.tree.heading("disponible", text="Disponible")
        self.tree.column("disponible", width=100)
        self.tree.heading("precio", text="Precio")
        self.tree.column("precio", width=100)
        self.tree.grid(row=11, columnspan=4, padx=10, pady=10)

        self.window.mainloop()

    def insertar_libro(self):
        id_libro = self.entry_id.get()
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        isbn = self.entry_isbn.get()
        paginas = self.entry_paginas.get()
        edicion = self.entry_edicion.get()
        editorial = self.entry_editorial.get()
        lugar = self.entry_lugar.get()
        disponible = self.entry_disponible.get()
        precio = self.entry_precio.get()

        if id_libro and titulo and autor and isbn and paginas and edicion and editorial and lugar and disponible and precio:
            libro = Libro(id_libro, titulo, autor, isbn, paginas, edicion, editorial, lugar, disponible, precio)
            self.libros.append(libro)
            messagebox.showinfo("Éxito", "Libro insertado correctamente.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def modificar_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_libro = self.entry_id.get()
            titulo = self.entry_titulo.get()
            autor = self.entry_autor.get()
            isbn = self.entry_isbn.get()
            paginas = self.entry_paginas.get()
            edicion = self.entry_edicion.get()
            editorial = self.entry_editorial.get()
            lugar = self.entry_lugar.get()
            disponible = self.entry_disponible.get()
            precio = self.entry_precio.get()

            if id_libro and titulo and autor and isbn and paginas and edicion and editorial and lugar and disponible and precio:
                libro = Libro(id_libro, titulo, autor, isbn, paginas, edicion, editorial, lugar, disponible, precio)
                index = int(self.tree.index(selected_item))
                self.libros[index] = libro
                messagebox.showinfo("Éxito", "Libro modificado correctamente.")
                self.clear_entries()
                self.listar_libros()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un libro de la lista.")

    def listar_libros(self):
        self.tree.delete(*self.tree.get_children())
        for libro in self.libros:
            self.tree.insert("", "end", text=libro.id_libro, values=(libro.id_libro, libro.titulo, libro.autor,
                                                                     libro.isbn, libro.paginas, libro.edicion,
                                                                     libro.editorial, libro.lugar, libro.disponible,
                                                                     libro.precio))

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_isbn.delete(0, tk.END)
        self.entry_paginas.delete(0, tk.END)
        self.entry_edicion.delete(0, tk.END)
        self.entry_editorial.delete(0, tk.END)
        self.entry_lugar.delete(0, tk.END)
        self.entry_disponible.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

    def borrar_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(self.tree.index(selected_item))
            del self.libros[index]
            messagebox.showinfo("Éxito", "Libro borrado correctamente.")
            self.clear_entries()
            self.listar_libros()
        else:
            messagebox.showerror("Error", "Por favor, seleccione un libro de la lista.")

if __name__ == "__main__":
    app = BibliotecaApp()
