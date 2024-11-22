from model.utente import Utente
from views.paziente_view import PazienteView
import tkinter as tk
from model.cartella_clinica import CartellaClinica





class Paziente(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.esercizi_assegnati = []
        self.cartella_clinica = ""
        
        
        
    def set_cartella_clinica(self,cartella):
        self.cartella_clinica = cartella
        
    def get_cartella_clinica(self):
        return self.cartella_clinica
    
    def set_credenziali(self, nome, email, password):
        self.nome = nome
        self.password = password
        self.email = email
        
    def get_esercizi(self):
        return self.esercizi_assegnati
    
    def add_esercizio(self, esercizio):
        self.esercizi_assegnati.append(esercizio)
    
    def remove_esercizio(self, esercizio):
        self.esercizi_assegnati.remove(esercizio)
        
    