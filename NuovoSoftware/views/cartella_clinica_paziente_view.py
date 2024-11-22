import tkinter as tk
from tkinter import scrolledtext

import tkinter.ttk as ttk
from tkinter import font, messagebox, filedialog as fd

class CartellaClinicaPaziente:
    def __init__(self, root, paziente):
        self.root = root
        self.paziente = paziente
        
        print("Mostra cartella clinica chiamato")  
        
        cartella_window = tk.Toplevel(self.root)
        cartella_window.title("Cartella Clinica")
        cartella_window.geometry("900x700")

        cartella_clinica = self.paziente.cartella_clinica

        if cartella_clinica:
            cartella_info = f"{cartella_clinica.descrizione}"
            informazioni_label = ttk.Label(cartella_window, text="Cartella Clinica", font=("Arial", 14))
            informazioni_label.pack(pady=10)
        else:
            cartella_info = "Non hai ancora una cartella clinica."
            informazioni_label = ttk.Label(cartella_window, text="Cartella Clinica", font=("Arial", 14))
            informazioni_label.pack(pady=10)

        descrizione_label = ttk.Label(cartella_window, text="Descrizione", font=("Arial", 14))
        descrizione_label.pack(pady=2)

        info_text = tk.Text(cartella_window, wrap='word', height=20, width=70, font=("Arial", 12))
        info_text.pack(pady=10)

        info_text.insert(tk.END, cartella_info)

        # Imposta la text box come non modificabile
        info_text.config(state=tk.DISABLED)
        
        indietro_button = ttk.Button(cartella_window, text="Torna indietro", command=cartella_window.destroy, style='TButton')
        indietro_button.pack(pady=20, ipadx=20, ipady=10)