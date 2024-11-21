from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from model.paziente import Paziente
from views.fisioterapista_view import FisioterapistaView



class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.lista_pazienti = []
        self.lista_esercizi = []
        self.lista_prenotazioni = []
        
    def aggiungi_paziente(self, nome, email, password, window):
        if nome and email and password:
            paziente = Paziente(nome, email, password)      
            self.lista_pazienti.append(paziente)
            window.destroy() 
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
            
    def cerca_pazienti(self, query):
        # Ricerca pazienti per nome o email
        risultati = [
            paziente for paziente in self.lista_pazienti
            if query.lower() in paziente.nome.lower() or query.lower() in paziente.email.lower()
        ]
        return risultati
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    