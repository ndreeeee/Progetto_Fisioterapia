from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from views.fisioterapista_view import FisioterapistaView


class CartellaClinica:
    def __init__(self, descrizione):
        self.codice = -1
        self.descrizione = descrizione
    
    def set_descrizione(self,descrizione):
        self.descrizione = descrizione