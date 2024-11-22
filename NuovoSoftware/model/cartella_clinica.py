from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from views.fisioterapista_view import FisioterapistaView


class CartellaClinica:
    
    _id_counter = 1 

    def __init__(self, descrizione):
        
        self.codice = CartellaClinica._id_counter
        CartellaClinica._id_counter += 1
        
        self.descrizione = descrizione
    
    def set_descrizione(self,descrizione):
        self.descrizione = descrizione