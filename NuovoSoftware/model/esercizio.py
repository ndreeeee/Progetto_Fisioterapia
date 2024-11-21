from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from model.paziente import Paziente
from views.fisioterapista_view import FisioterapistaView



class Esercizio:
    def __init__(self, titolo, descrizione, video):
        
        self.codice = -1
        self.descrizione = descrizione
        self.titolo = titolo
        self.video = video
