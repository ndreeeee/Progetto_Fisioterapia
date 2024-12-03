from controller.gestore_dati import GestoreDati
from model.paziente import Paziente
from tkinter import messagebox

class GestoreFisioterapista:
    def __init__(self):
        self.lista_pazienti = GestoreDati().carica_pazienti()
        
    
    def get_pazienti(self):
        return self.lista_pazienti
    
    def aggiungi_paziente(self, nome, email, password):
        paziente = Paziente (nome, email, password)
        self.lista_pazienti.append(paziente)
    
    
    def aggiungi_paziente(self, nome, email, password, window, fisioterapista):
        if nome and email and password:
            paziente = Paziente(nome, email, password)      
            self.lista_pazienti.append(paziente)
            fisioterapista.lista_pazienti.append(paziente)
            GestoreDati().aggiungi_utente(nome, email, password, "paziente")
            window.destroy() 
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
    
        
    def modifica_paziente(self, nome, email, password, window, paziente1, fisioterapista):   
        if nome and email and password:
            for paziente in self.lista_pazienti:
                if paziente == paziente1:
                    fisioterapista.lista_pazienti.remove(paziente)
                    paziente.set_credenziali(nome, email, password)
                    fisioterapista.lista_pazienti.append(paziente)
                    GestoreDati().modifica_paziente(paziente, nome, email, password)
                    window.destroy() 
                    messagebox.showinfo("Successo", "Modifiche salvate con successo!")
                    
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
                    
    def elimina_paziente(self, paziente1, finestra_profilo, fisioterapista):
        risposta = messagebox.askyesno("Conferma Eliminazione", "Sei sicuro di voler eliminare questo paziente?")
        
        if risposta:
            for paziente in self.lista_pazienti:
                if paziente1 == paziente:
                    self.lista_pazienti.remove(paziente)
                    fisioterapista.lista_pazienti.remove(paziente)
                    GestoreDati().elimina_paziente(paziente.get_id())
                      # Save after deleting patient
                    finestra_profilo.destroy()
            
            messagebox.showinfo("Successo", "Paziente eliminato con successo.")
                
                