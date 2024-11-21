from model.utente import Utente
from views.paziente_view import PazienteView
import tkinter as tk





class Paziente(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.esercizi_assegnati = []
        
    