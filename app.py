import tkinter as tk
from tkinter import filedialog
from shutil import move


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.placemarks = []
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_file_button = tk.Button(self, text="Selecione um arquivo KMZ", command=self.select_file)
        self.select_file_button.pack()

        self.previous_button = tk.Button(self, text="Anterior", command=self.previous_placemark)
        self.previous_button.pack(side="left")

        self.next_button = tk.Button(self, text="Próximo", command=self.next_placemark)
        self.next_button.pack(side="left")

        self.aprovar_button = tk.Button(self, text="Aprovar", command=lambda: self.move_placemark("aprovados"))
        self.aprovar_button.pack(side="right")

        self.reprovar_button = tk.Button(self, text="Reprovar", command=lambda: self.move_placemark("reprovados"))
        self.reprovar_button.pack(side="right")






root = tk.Tk()
app = Application(master=root)
app.mainloop()
