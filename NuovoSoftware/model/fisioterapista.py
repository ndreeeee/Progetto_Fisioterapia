from tkinter import messagebox
import tkinter as tk
import pickle
import os
from model.utente import Utente
from model.paziente import Paziente
from model.esercizio import Esercizio
from model.cartella_clinica import CartellaClinica



class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
               
        self.lista_pazienti = []
        self.lista_esercizi = []
        self.lista_prenotazioni = []
        
        self.load_data()
        
    
        
    def save_data(self):
        """Salva i dati dei pazienti, esercizi e prenotazioni su file"""
        try:
            # Ensure data directory exists
            os.makedirs('data', exist_ok=True)

            # Salvataggio dei pazienti
            with open('data/pazienti.pkl', 'wb') as pazienti_file:
                pickle.dump(self.lista_pazienti, pazienti_file, protocol=pickle.HIGHEST_PROTOCOL)

            # Salvataggio degli esercizi
            with open('data/esercizi.pkl', 'wb') as esercizi_file:
                pickle.dump(self.lista_esercizi, esercizi_file, protocol=pickle.HIGHEST_PROTOCOL)

            # Salvataggio delle prenotazioni
            with open('data/prenotazioni.pkl', 'wb') as prenotazioni_file:
                pickle.dump(self.lista_prenotazioni, prenotazioni_file, protocol=pickle.HIGHEST_PROTOCOL)

            print("Dati salvati correttamente.")

        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
            messagebox.showerror("Errore", f"Impossibile salvare i dati: {e}")

    def load_data(self):
        """Carica i dati dei pazienti, esercizi e prenotazioni dal file"""
        try:
            # Caricamento dei pazienti
            if os.path.exists('data/pazienti.pkl'):
                with open('data/pazienti.pkl', 'rb') as pazienti_file:
                    self.lista_pazienti = pickle.load(pazienti_file)
                print(f"Pazienti caricati: {len(self.lista_pazienti)}")

            # Caricamento degli esercizi
            if os.path.exists('data/esercizi.pkl'):
                with open('data/esercizi.pkl', 'rb') as esercizi_file:
                    self.lista_esercizi = pickle.load(esercizi_file)
                print(f"Esercizi caricati: {len(self.lista_esercizi)}")

            # Caricamento delle prenotazioni
            if os.path.exists('data/prenotazioni.pkl'):
                with open('data/prenotazioni.pkl', 'rb') as prenotazioni_file:
                    self.lista_prenotazioni = pickle.load(prenotazioni_file)
                print(f"Prenotazioni caricate: {len(self.lista_prenotazioni)}")

        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
            # Se i file non esistono, inizializza le liste vuote
            self.lista_pazienti = []
            self.lista_esercizi = []
            self.lista_prenotazioni = []
        
   

    def aggiungi_paziente(self, nome, email, password, window):
        if nome and email and password:
            paziente = Paziente(nome, email, password)      
            self.lista_pazienti.append(paziente)
            with open('paziente.pkl', 'wb') as file:
                pickle.dump(paziente, file, pickle.HIGHEST_PROTOCOL)
            self.save_data()  # Save after adding patient
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
                self.save_data()
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
        self.save_data()
                
    
    def aggiungi_nuovo_esercizio(self, titolo, descrizione, video_url):
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                messagebox.showerror("Errore", "Questo esercizio è stato già inserito")
                return      
        exercise = Esercizio(titolo, descrizione, video_url)
        self.lista_esercizi.append(exercise)
        self.save_data()  # Save after adding exercise
        messagebox.showinfo("Successo", "Esercizio inserito con successo!")
        
    def aggiungi_cartella_clinica (self, paziente, descrizione):
        cartella_clinica = CartellaClinica(descrizione)
        
        for paziente1 in self.lista_pazienti:
            if paziente == paziente1:
                paziente1.set_cartella_clinica(cartella_clinica)
                messagebox.showinfo("Successo", "Cartella Clinica aggiunta con successo!")
                self.save_data()
                
    def modifica_cartella_clinica(self, cartella, descrizione):
        cartella.set_descrizione(descrizione)
        self.save_data()

        
    def modifica_paziente(self, nome, email, password, window, paziente1):   
        if nome and email and password:
            for paziente in self.lista_pazienti:
                if paziente == paziente1:
                    paziente.set_credenziali(nome, email, password)
                    window.destroy() 
                    messagebox.showinfo("Successo", "Modifiche salvate con successo!")
                    self.save_data()
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
            
    def get_esercizi(self):
        return self.lista_esercizi
            
    def aggiungi_esercizio_paziente(self, paziente1, esercizio):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                paziente.add_esercizio(esercizio)
                self.save_data()
                
    def rimuovi_esercizio_paziente (self, paziente1, titolo):
        for paziente in self.lista_pazienti:
            if paziente1 == paziente:
                for esercizio in self.lista_esercizi:
                    if titolo == esercizio.titolo:
                        paziente.remove_esercizio(esercizio)
                        self.save_data()
                        
    def elimina_paziente(self, paziente1, finestra_profilo):
        risposta = messagebox.askyesno("Conferma Eliminazione", "Sei sicuro di voler eliminare questo paziente?")
        
        if risposta:
            for paziente in self.lista_pazienti:
                if paziente1 == paziente:
                    self.lista_pazienti.remove(paziente)
                    self.save_data()  # Save after deleting patient
                    finestra_profilo.destroy()
            
            messagebox.showinfo("Successo", "Paziente eliminato con successo.")
            
    def __repr__(self):
        return f"Paziente(nome={self.nome}, email={self.email})"
            

        
            
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    