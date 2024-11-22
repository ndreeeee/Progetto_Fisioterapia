from tkinter import messagebox
import tkinter as tk



class Utente:
    
    _id_counter = 1 

    
    def __init__(self, nome, email, password):
        
        self.codice = Utente._id_counter
        Utente._id_counter += 1
        
        self.nome = nome
        self.email = email
        self.password = password
        
        
      


  
    
            
    

   
