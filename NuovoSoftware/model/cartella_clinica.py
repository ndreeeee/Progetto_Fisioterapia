from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from views.fisioterapista_view import FisioterapistaView


class CartellaClinica:
    
     

    def __init__(self, descrizione):
        
        self.id = -1
        self.descrizione = descrizione
    
    def get_id(self):
        return self.id
    
    def set_id(self,id):
        self.id = id
    
    def set_descrizione(self,descrizione):
        self.descrizione = descrizione
        
    def get_descrizione(self):
        return self.descrizione