from tkinter import messagebox
import tkinter as tk
from model.utente import Utente
from model.paziente import Paziente
from views.fisioterapista_view import FisioterapistaView
from model.esercizio import Esercizio
from model.cartella_clinica import CartellaClinica



class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        self.lista_pazienti = []
        self.lista_esercizi = []
        self.lista_prenotazioni = []
        
        esempio = Paziente ("Marco Bianchi", "marco@email.com", "password123")
        
        esercizio1 = Esercizio ("salti con la corda", "descrizione", "")
        es2 = Esercizio ("Panca piana", "description", "")
        
        self.lista_esercizi.append(es2)
        self.lista_esercizi.append(esercizio1)

        self.lista_pazienti.append(esempio)
        
    def aggiungi_paziente(self, nome, email, password, window):
        if nome and email and password:
            paziente = Paziente(nome, email, password)      
            self.lista_pazienti.append(paziente)
            window.destroy() 
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
            
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
                
    
    def aggiungi_nuovo_esercizio (self, titolo, descrizione, video_url):
        
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                messagebox.showerror("Errore", "Questo esercizio è stato già inserito")
                return      
        self.lista_esercizi.append(Esercizio(titolo, descrizione,video_url))
        messagebox.showinfo("Successo", "Esercizio inserito con successo!")
        
    def aggiungi_cartella_clinica (self, paziente, descrizione):
        cartella_clinica = CartellaClinica(descrizione)
        
        for paziente1 in self.lista_pazienti:
            if paziente == paziente1:
                paziente1.set_cartella_clinica(cartella_clinica)
                messagebox.showinfo("Successo", "Cartella Clinica aggiunta con successo!")
                
    def modifica_cartella_clinica(self, cartella, descrizione):
        cartella.set_descrizione(descrizione)

        
    def modifica_paziente(self, nome, email, password, window, paziente1):   
        if nome and email and password:
            for paziente in self.lista_pazienti:
                if paziente == paziente1:
                    paziente.set_credenziali(nome, email, password)
                    window.destroy() 
                    messagebox.showinfo("Successo", "Modifiche salvate con successo!")
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
            
    def get_esercizi(self):
        return self.lista_esercizi
            
    def aggiungi_esercizio_paziente(self, paziente1, esercizio):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                paziente.add_esercizio(esercizio)
                
    def rimuovi_esercizio_paziente (self, paziente1, titolo):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                for esercizio in self.lista_esercizi:
                    if titolo == esercizio.titolo:
                        paziente.remove_esercizio(esercizio)
                        
    def elimina_paziente(self, paziente1, finestra_profilo):
        risposta = messagebox.askyesno("Conferma Eliminazione", "Sei sicuro di voler eliminare questo paziente?")
        
        if risposta:
            for paziente in self.lista_pazienti:
                if paziente1 == paziente:
                    self.lista_pazienti.remove(paziente)
                    finestra_profilo.destroy()
            
            messagebox.showinfo("Successo", "Paziente eliminato con successo.")
        
            
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    