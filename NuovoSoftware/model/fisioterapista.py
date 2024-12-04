from tkinter import messagebox
from controller.gestore_dati import GestoreDati
from model.utente import Utente
from model.esercizio import Esercizio
from model.esercizio_assegnato import EsercizioAssegnato



class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        
        
        
        
  
    
    
    
            
   
    
            
   
    
    
    def cerca_esercizio (self, query):
        
        risultati = [
            esercizio for esercizio in self.lista_esercizi
            if query.lower() in esercizio.titolo.lower()
        ]
        
        return risultati
    
    
            
    
            
    
        
                
    
    def aggiungi_nuovo_esercizio(self, titolo, descrizione, video_url):
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                messagebox.showerror("Errore", "Questo esercizio è stato già inserito")
                return      
        exercise = Esercizio(titolo, descrizione, video_url)
        self.lista_esercizi.append(exercise)
          # Save after adding exercise
        messagebox.showinfo("Successo", "Esercizio inserito con successo!")
        
   
        

        

            
    
            
    def aggiungi_esercizio_paziente(self, paziente1, esercizio):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                esercizio_assegnato = EsercizioAssegnato(esercizio.titolo, esercizio.descrizione, esercizio.video)
                paziente.add_esercizio(esercizio_assegnato)
                
                
    
                        
                        
    
            
  
            

        
            
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    