from controller.gestore_dati import GestoreDati
from controller.gestore_fisioterapista import GestoreFisioterapista
from controller.gestore_esercizi import GestoreEsercizi
from controller.gestore_paziente import GestorePaziente
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
            if isinstance(utente, Fisioterapista):
                self.fisioterapista = utente
        
        for utente in self.lista_utenti:
            if utente.email == email and utente.password == password:
                root.destroy()  
                root = tk.Tk()  
                
                
                if isinstance(utente, Fisioterapista):
                    gestore = GestoreFisioterapista()
                    gestore.set_lista_pazienti(GestoreDati().carica_pazienti())
                    gestoreEsercizi = GestoreEsercizi()
                    gestoreEsercizi.set_lista_esercizi(GestoreDati().carica_esercizi())
                    gestoreEsercizi.set_esercizi_assegnati(GestoreDati().get_esercizi_assegnati())
                    from views.fisioterapista_view import FisioterapistaView
                    FisioterapistaView(root, utente, gestore, gestoreEsercizi)  

                elif isinstance(utente, Paziente):
                    gestore = GestorePaziente()
                    gestore.set_esercizi_assegnati(GestoreDati().get_esercizi_assegnati())
                    gestore.set_cartella(GestoreDati().get_cartella_clinica_utente(utente.get_id()))
                    from views.paziente_view import PazienteView
                    PazienteView(root, utente, gestore, self.fisioterapista)  
                return
        messagebox.showerror("Errore", "Credenziali errate. Riprova.")