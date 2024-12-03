from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from model.paziente import Paziente
from views.fisioterapista_view import FisioterapistaView



class Esercizio:
    
    _id_counter = 1 

    
    def __init__(self, titolo, descrizione, video):
        
        self.codice = Esercizio._id_counter
        Esercizio._id_counter += 1
        self.descrizione = descrizione
        self.titolo = titolo
        self.video = video
 
    def get_video (self):
        return self.video
    
    def get_titolo(self):
        return self.titolo
    
    def get_descrizione(self):
        return self.descrizione
    
    def set_descrizione(self, descrizione):
        self.descrizione = descrizione
    
    def set_titolo (self, titolo):
        self.titolo = titolo
        
    def set_video(self, video):
        self.video = video