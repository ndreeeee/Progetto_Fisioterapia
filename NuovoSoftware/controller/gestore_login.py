from controller.gestore_dati import GestoreDati
from controller.gestore_fisioterapista import GestoreFisioterapista
from controller.gestore_esercizi import GestoreEsercizi
from tkinter import messagebox
import tkinter as tk

class GestoreLogin:
    def __init__(self):
        self.lista_utenti = GestoreDati().carica_utenti()
        
        print (self.lista_utenti)
    
    
    def login(self, root, email, password):
        from model.fisioterapista import Fisioterapista
        from model.paziente import Paziente
        
        for utente in self.lista_utenti:
            if utente.email == email and utente.password == password:
                root.destroy()  
                root = tk.Tk()  
                
                
                if isinstance(utente, Fisioterapista):
                    from views.fisioterapista_view import FisioterapistaView
                    utente.set_lista_pazienti(GestoreDati().carica_pazienti())
                    utente.set_lista_esercizi(GestoreEsercizi().get_esercizi())
                    FisioterapistaView(root, utente)  

                elif isinstance(utente, Paziente):
                    from views.paziente_view import PazienteView
                    PazienteView(root, utente)  
                return
        messagebox.showerror("Errore", "Credenziali errate. Riprova.")