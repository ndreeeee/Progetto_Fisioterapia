from controller.gestore_dati import GestoreDati
from model.paziente import Paziente
from model.cartella_clinica import CartellaClinica
from datetime import datetime, timedelta
from tkinter import messagebox

class GestoreFisioterapista:
    def __init__(self):
        self.lista_pazienti = []
        self.cartelle_cliniche = []
        self.prenotazioni = GestoreDati().get_prenotazioni_effettuate()
        self.elimina_prenotazioni_scadute()
        
        
    def get_prenotazioni (self):
        return self.prenotazioni
    
    def set_lista_pazienti(self, lista_pazienti):
        self.lista_pazienti = lista_pazienti
    
    def get_pazienti(self):
        return self.lista_pazienti      
    
    
    def cerca_pazienti(self, query):
        
        risultati = [
            paziente for paziente in self.lista_pazienti
            if query.lower() in paziente.get_nome().lower() or query.lower() in paziente.get_email().lower()
        ]
        return risultati  
    
    def ottieni_paziente(self, nome, email):
        for paziente in self.lista_pazienti:
            if nome == paziente.get_nome() and email == paziente.get_email():
                print(f"{paziente.get_nome()} - {paziente.get_email()}")
                return paziente
    
    
    def aggiungi_paziente(self, nome, email, password, window):
        if nome and email and password:
            paziente = Paziente(nome, email, password)      
            self.lista_pazienti.append(paziente)
            GestoreDati().aggiungi_utente(nome, email, password, "paziente")
            window.destroy() 
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
    
        
    def modifica_paziente(self, nome, email, password, window, paziente1):   
        if nome and email and password:
            for paziente in self.lista_pazienti:
                if paziente == paziente1:
                    paziente.set_credenziali(nome, email, password)
                    GestoreDati().modifica_paziente(paziente.get_id(), nome, email, password)
                    window.destroy() 
                    messagebox.showinfo("Successo", "Modifiche salvate con successo!")
                    
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
                    
    def elimina_paziente(self, paziente1, finestra_profilo):
        risposta = messagebox.askyesno("Conferma Eliminazione", "Sei sicuro di voler eliminare questo paziente?")
        
        if risposta:
            for paziente in self.lista_pazienti:
                if paziente == paziente1:
                    self.lista_pazienti.remove(paziente)
                    GestoreDati().elimina_paziente(paziente.get_id())
                    finestra_profilo.destroy()
            
            messagebox.showinfo("Successo", "Paziente eliminato con successo.")
            
            
            
    def aggiungi_cartella_clinica (self, paziente, descrizione):
        cartella_clinica = CartellaClinica(descrizione)
        
        for paziente1 in self.lista_pazienti:
            if paziente.get_email() == paziente1.get_email():
                paziente1.set_cartella_clinica(cartella_clinica)
                GestoreDati().aggiungi_cartella(descrizione, paziente.get_id())
                
                
    def modifica_cartella_clinica(self, paziente, descrizione):
        cartella = paziente.get_cartella_clinica()
        paziente.aggiorna_cartella(descrizione)
        GestoreDati().modifica_cartella(paziente.get_id(), descrizione)
        
        
    def elimina_prenotazioni_scadute(self):
     
        ora_attuale = datetime.now()
        prenotazioni_da_rimuovere = [
                p for p in self.prenotazioni
                if datetime.strptime(p.data_e_ora, '%Y-%m-%d %H:%M') < ora_attuale
            ]
        
        for p in prenotazioni_da_rimuovere:
            self.prenotazioni.remove(p)
        
        
        
    

                
                