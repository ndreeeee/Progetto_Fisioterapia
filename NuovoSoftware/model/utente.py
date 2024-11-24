from tkinter import messagebox
import tkinter as tk
from model.messaggio import Messaggio
from database import Database




class Utente:
    
    _id_counter = 1 

    
    def __init__(self, nome, email, password):
        
        self.codice = Utente._id_counter
        Utente._id_counter += 1
        
        self.nome = nome
        self.email = email
        self.password = password
        
    def invia_messaggio(self, mittente, destinatario, testo):
        Messaggio(testo, destinatario, mittente)
        db = Database()
        db.salva_messaggio(mittente.codice, destinatario.codice, testo)
        

        

      


  
    
            
    

   
