import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Eliminar filas en archivo XYZ")
        self.master.geometry("400x200")
        
        self.file_path = ""
        self.skip_rate = 0
        
        self.file_label = tk.Label(master, text="Seleccione archivo XYZ:")
        self.file_label.pack(pady=(20,10))
        
        self.file_button = tk.Button(master, text="Seleccionar archivo", command=self.open_file)
        self.file_button.pack(pady=(0,20))
        
        self.skip_label = tk.Label(master, text="Ingrese número de filas a saltar de cada 100:")
        self.skip_label.pack(pady=(0,10))
        
        self.skip_entry = tk.Entry(master)
        self.skip_entry.pack()
        
        self.run_button = tk.Button(master, text="Ejecutar", command=self.process_file)
        self.run_button.pack(pady=(20,0))
        
    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".xyz", filetypes=[("XYZ files", "*.xyz")])
        
    def process_file(self):
        if self.file_path == "":
            tk.messagebox.showerror("Error", "Seleccione un archivo XYZ")
        else:
            try:
                self.skip_rate = int(self.skip_entry.get())
                with open(self.file_path, 'r') as input_file:
                    with open("output.xyz", 'w') as output_file:
                        line_count = 0
                        skip_count = 0
                        for line in input_file:
                            if line_count % 100 >= self.skip_rate:
                                output_file.write(line)
                            else:
                                skip_count += 1
                            line_count += 1
                        tk.messagebox.showinfo("Completado", f"Se eliminaron {skip_count} filas de cada 100 seleccionadas.")
            except ValueError:
                tk.messagebox.showerror("Error", "Ingrese un número entero válido para el salto de filas.")
        

root = tk.Tk()
app = App(root)
root.mainloop()