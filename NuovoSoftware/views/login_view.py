import tkinter as tk
from tkinter import ttk
from model.fisioterapista import Fisioterapista
from model.paziente import Paziente
from tkinter import messagebox
from model.prenotazione import GestorePrenotazioni
import pickle
import os



class LoginView:
    def __init__(self, root, lista_utenti):
        self.root = root
        self.root.title("Login")
        self.lista_utenti = lista_utenti

        self.root.configure(bg="#f4f4f4")
        
        gestore = GestorePrenotazioni()
        
        gestore.aggiorna_prenotazioni_future()
        self.posti_disponibili = gestore.get_prenotazioni_disponibili()
        self.posti_prenotati = gestore.get_posti_prenotati()
        
        font_label = ("Helvetica", 14, "bold")
        font_entry = ("Helvetica", 14)
        btn_style = ttk.Style()
        
        btn_style.configure("TButton", 
                            padding=10, 
                            relief="flat", 
                            background="#007bff", 
                            foreground="black",
                            font=("Helvetica", 12, "bold"))

        btn_style.map("TButton", 
                      background=[('active', '#0056b3')], 
                      foreground=[('active', 'white')])

        
        self.spazio = tk.Label(self.root, bg="#f4f4f4")
        self.spazio.pack(expand=True)
        
        label = tk.Label(self.root, text="Inserisci le tue credenziali per accedere all'Area Riservata", font=("Arial", 14, "bold"))
        label.pack(pady=20)
        
        
        self.email_label = tk.Label(self.root, text="Email", bg="#f4f4f4", font=font_label)
        self.email_label.pack(pady=(20, 20))
        self.email_entry = ttk.Entry(self.root, font=font_entry)
        self.email_entry.pack(pady=10, ipadx=5, ipady=5, fill="x", padx=200)

        
        self.password_label = tk.Label(self.root, text="Password", bg="#f4f4f4", font=font_label)
        self.password_label.pack(pady=(10, 5))

        # Frame per password e icona
        password_frame = tk.Frame(self.root, bg="#f4f4f4")
        password_frame.pack(pady=10, fill="x", padx=200)
        
        self.password_entry = ttk.Entry(password_frame, show="*", font=font_entry)
        self.password_entry.pack(side="left", fill="x", expand=True, ipadx=5, ipady=5)

        self.show_password = False
        self.eye_button = tk.Button(password_frame, text="👁️", command=self.toggle_password, bg="#f4f4f4", bd=0, font=("Arial", 14))
        self.eye_button.pack(side="right", padx=(5, 0))

        self.login_button = ttk.Button(self.root, text="Login", style="TButton", command=self.login)
        self.login_button.pack(pady=20)

        self.spazio2 = tk.Label(self.root, bg="#f4f4f4")
        self.spazio2.pack(expand=True)

    def toggle_password(self):
        """Alterna la visualizzazione della password."""
        if self.show_password:
            self.password_entry.config(show="*")
            self.eye_button.config(text="👁️")  
        else:
            self.password_entry.config(show="")
            self.eye_button.config(text="🔒")  
        self.show_password = not self.show_password

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        lista_pazienti = []
        
        for utente in self.lista_utenti:
            if (isinstance(utente, Fisioterapista)):
                fisioterapista = utente
                continue
                
            lista_pazienti.append(utente)
            fisioterapista.lista_pazienti = lista_pazienti
            fisioterapista.lista_prenotazioni = self.posti_prenotati
        
        
        for utente in self.lista_utenti:
            if utente.email == email and utente.password == password:
                self.root.destroy()  
                root = tk.Tk()  
                
                
                if isinstance(utente, Fisioterapista):
                    from views.fisioterapista_view import FisioterapistaView
                    FisioterapistaView(root, utente)  

                elif isinstance(utente, Paziente):
                    from views.paziente_view import PazienteView
                    PazienteView(root, utente, fisioterapista, self.posti_disponibili)  
                return
        messagebox.showerror("Errore", "Credenziali errate. Riprova.")
            

