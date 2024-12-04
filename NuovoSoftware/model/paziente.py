from model.utente import Utente
from model.cartella_clinica import CartellaClinica





class Paziente(Utente):

    def __init__(self, nome, email, password):
        
        super().__init__(nome, email, password)
        self.esercizi_assegnati = []
        self.prenotazioni = []
        self.cartella_clinica = None
      
    
  
    def set_cartella_clinica(self,cartella):
        self.cartella_clinica = cartella
        
    def get_cartella_clinica(self):
        if self.cartella_clinica:
            return self.cartella_clinica
        else:
            return False
        
    def aggiorna_cartella(self, descrizione):
        self.cartella_clinica.set_descrizione(descrizione)


       
    
    def set_credenziali(self, nome, email, password):
        self.nome = nome
        self.password = password
        self.email = email
        
    def get_esercizi(self):
        return self.esercizi_assegnati
    
    def add_esercizio(self, esercizio):
        self.esercizi_assegnati.append(esercizio)
    
    def remove_esercizio(self, esercizio):
        self.esercizi_assegnati.remove(esercizio)

        
    def prenota (self, prenotazione):
        prenotazione.stato = "prenotato"
        self.prenotazioni.append(prenotazione)

    
    def elimina_prenotazione (self, prenotazione):
        if prenotazione in self.prenotazioni:
            prenotazione.stato = "disponibile"
            self.prenotazioni.remove(prenotazione)
    
    def get_prenotazioni(self):
        return self.prenotazioni
    
    
        
    def __del__(self):
        print(f"Paziente {self.nome} eliminato, id = {self.id}")
        
    def __repr__(self):
        return f"Paziente (id = {self.id}, nome={self.nome}, email={self.email}, password= {self.password})"