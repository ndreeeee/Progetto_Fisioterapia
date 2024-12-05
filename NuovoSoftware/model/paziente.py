from model.utente import Utente
from model.cartella_clinica import CartellaClinica





class Paziente(Utente):

    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
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
        

    
    def __repr__(self):
        return f"Paziente (id = {self.id}, nome={self.nome}, email={self.email}, password= {self.password})"