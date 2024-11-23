import tkinter as tk
from tkinter import scrolledtext

import tkinter.ttk as ttk
from tkinter import font, messagebox, filedialog as fd
from views.cartella_clinica_paziente_view import CartellaClinicaPaziente
from views.prenotazione_view import PrenotazioniView
from views.messaggi_view import MessaggiView
from database import Database




class PazienteView(tk.Frame):
    def __init__(self, root, paziente, fisioterapista, posti_disponibili):  
        self.root = root
        self.paziente = paziente
        self.posti_disponibili = posti_disponibili  
        self.fisioterapista = fisioterapista
        
        self.main_frame = tk.Frame(self.root, width=900, height=700)
        self.main_frame.pack_propagate(False) 
        self.main_frame.pack()
        
        button_font = ("Arial", 14, "bold")  

        
        self.spazio = ttk.Label(self.main_frame)
        self.spazio.pack(expand=True)
        
        self.label = ttk.Label(self.main_frame, text=f"Benvenuto, {self.paziente.nome}", font=("Arial", 18, "bold"))
        self.label.pack()
        
        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        titolo_font = font.Font(family="Arial", size=14, weight="bold")
        
        """
        percentuale = self.controller.db.calcola_percentuale_completamento(id_paziente)
        
        percentuale_label = tk.Label(self.main_frame, text=f"Completamento Terapia: {percentuale:.2f}%", font=titolo_font)
        percentuale_label.pack(pady=20)

        progressbar = ttk.Progressbar(self.main_frame, orient="horizontal", length=300, mode="determinate")
        progressbar.pack(pady=20)

        progressbar['value'] = percentuale
        """
        self.cartella_clinica_btn = ttk.Button(self.main_frame, text="Cartella Clinica", command= lambda: CartellaClinicaPaziente(self.root, self.paziente), width=20, style='TButton')
        self.cartella_clinica_btn.pack(pady=20, ipadx=20, ipady=10)
        
        self.messaggi_btn = ttk.Button(self.main_frame, text="Prenotazione", command=lambda: PrenotazioniView(self.root, self.paziente, self.posti_disponibili), width=20, style='TButton')
        self.messaggi_btn.pack(pady=20, ipadx=20, ipady=10)
        
        self.messaggi_btn = ttk.Button(self.main_frame, text="Messaggi", command=lambda: MessaggiView(self.root, paziente, self.fisioterapista, 0), width=20, style='TButton')
        self.messaggi_btn.pack(pady=20, ipadx=20, ipady=10)

        #self.esercizi_btn = ttk.Button(self.main_frame, text="Esercizi", command=self.mostra_esercizi, width=20, style='TButton')
        #self.esercizi_btn.pack(pady=20, ipadx=20, ipady=10)

        
        
        
        
        style = ttk.Style()
        style.configure('TButton', font=button_font)  
        
        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        

        print("Interfaccia creata con successo")  # Debug per vedere se la GUI è stata creata correttamente

    