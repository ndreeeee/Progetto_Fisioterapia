from tkinter import messagebox
from controller.gestore_dati import GestoreDati
from model.utente import Utente
from model.paziente import Paziente
from model.esercizio import Esercizio
from model.cartella_clinica import CartellaClinica
from model.esercizio_assegnato import EsercizioAssegnato



class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.id = -1 
        self.lista_pazienti = []
        self.lista_esercizi = []
        self.lista_prenotazioni = []
        
        
        
    def set_id(self,id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_lista_esercizi(self, lista_esercizi):
        self.lista_esercizi = lista_esercizi
    
    def set_lista_pazienti (self, lista_pazienti):
        self.lista_pazienti = lista_pazienti
    
    
    def get_lista_pazienti(self):
        return self.lista_pazienti
    
            
    def ottieni_paziente(self, nome, email):
        for paziente in self.lista_pazienti:
            if nome == paziente.nome and email == paziente.email:
                return paziente
    
            
    def cerca_pazienti(self, query):
        
        risultati = [
            paziente for paziente in self.lista_pazienti
            if query.lower() in paziente.nome.lower() or query.lower() in paziente.email.lower()
        ]
        return risultati
    
    
    def cerca_esercizio (self, query):
        
        risultati = [
            esercizio for esercizio in self.lista_esercizi
            if query.lower() in esercizio.titolo.lower()
        ]
        
        return risultati
    
    def elimina_esercizio(self, titolo):
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                self.lista_esercizi.remove(esercizio)
                
                break
            
    def ottieni_esercizio(self, titolo):
        for esercizio in self.lista_esercizi:
            if titolo == esercizio.titolo:
                return esercizio
            
    def modifica_esercizio(self, titolo, descrizione, video, esercizio):
        
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                self.lista_esercizi.remove(esercizio)
            
        esercizio.titolo = titolo
        esercizio.descrizione = descrizione
        esercizio.video = video
        
        self.lista_esercizi.append(Esercizio(titolo, descrizione, video))
        
                
    
    def aggiungi_nuovo_esercizio(self, titolo, descrizione, video_url):
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                messagebox.showerror("Errore", "Questo esercizio è stato già inserito")
                return      
        exercise = Esercizio(titolo, descrizione, video_url)
        self.lista_esercizi.append(exercise)
          # Save after adding exercise
        messagebox.showinfo("Successo", "Esercizio inserito con successo!")
        
    def aggiungi_cartella_clinica (self, paziente, descrizione):
        cartella_clinica = CartellaClinica(descrizione)
        
        for paziente1 in self.lista_pazienti:
            if paziente == paziente1:
                paziente1.set_cartella_clinica(cartella_clinica)
                messagebox.showinfo("Successo", "Cartella Clinica aggiunta con successo!")
                
                
    def modifica_cartella_clinica(self, cartella, descrizione):
        cartella.set_descrizione(descrizione)
        

        

            
    def get_esercizi(self):
        return self.lista_esercizi
            
    def aggiungi_esercizio_paziente(self, paziente1, esercizio):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                esercizio_assegnato = EsercizioAssegnato(esercizio.titolo, esercizio.descrizione, esercizio.video)
                paziente.add_esercizio(esercizio_assegnato)
                
                
    def rimuovi_esercizio_paziente (self, paziente1, titolo):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                for esercizio in self.lista_esercizi:
                    if titolo == esercizio.titolo:
                        paziente.remove_esercizio(esercizio)
                        
                        
    
            
    def __repr__(self):
        return f"Fisioterapista (nome={self.nome}, email={self.email}, password = {self.password})"
            

        
            
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    