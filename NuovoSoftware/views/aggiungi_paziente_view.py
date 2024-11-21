import tkinter as tk
from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog



class AggiungiPazienteView:
    def __init__(self, root, fisioterapista):
        
                
        form_window = tk.Toplevel(root)
        form_window.title("Aggiungi Nuovo Paziente")

        self.main_frame = ttk.Frame(form_window, width=900, height=700)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(pady=20, padx=20)

        self.spazio = ttk.Label(self.main_frame)
        self.spazio.pack(expand=True)

        # Campo per inserire il nome del paziente
        ttk.Label(self.main_frame, text="Nome Paziente", font=("Arial", 16)).pack(pady=5)
        nome_entry = ttk.Entry(self.main_frame, font=("Arial", 14), width=70)
        nome_entry.pack(pady=10)

        # Campo per inserire l'email del paziente
        ttk.Label(self.main_frame, text="Email Paziente", font=("Arial", 16)).pack(pady=5)
        email_entry = ttk.Entry(self.main_frame, font=("Arial", 14), width=70)
        email_entry.pack(pady=10)

        # Campo per inserire la password del paziente
        ttk.Label(self.main_frame, text="Password Paziente", font=("Arial", 16)).pack(pady=5)
        password_entry = ttk.Entry(self.main_frame, show="*", font=("Arial", 14), width=70)
        password_entry.pack(pady=10)

        # Pulsante per aggiungere il paziente
        submit_button = ttk.Button(self.main_frame, text="Aggiungi", 
                                command=lambda: fisioterapista.aggiungi_paziente(nome_entry.get(), email_entry.get(), password_entry.get(), form_window),
                                style="TButton")
        submit_button.pack(pady=15, ipadx=10, ipady=5)

        # Pulsante per tornare indietro
        back_button = ttk.Button(self.main_frame, text="Torna Indietro", command=lambda: form_window.destroy, style="TButton")
        back_button.pack(pady=10, ipadx=10, ipady=5)

        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        
        