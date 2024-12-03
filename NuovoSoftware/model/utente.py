from tkinter import messagebox
import tkinter as tk
from model.messaggio import Messaggio




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
        
    def set_nome(self,nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    
    def set_email(self, email):
        self.email = email
    
    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = password
        
    def get_password(self):
        return self.password
        

        

      


  
    
            
    

   
