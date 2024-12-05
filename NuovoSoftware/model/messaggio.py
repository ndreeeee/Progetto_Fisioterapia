from datetime import datetime

class Messaggio():
    
    
    def __init__(self, descrizione, destinatario, mittente, data_invio = None):
        
        self.id = -1
        self.data_invio = data_invio if data_invio else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.descrizione=descrizione
        self.destinatario=destinatario
        self.mittente=mittente
        
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def get_data_invio(self):
        return self.data_invio
    
    def set_data_invio(self, data_invio):
        self.data_invio = data_invio
        
    def get_mittente(self):
        return self.mittente
    
    def set_mittente(self, mittente):
        self.mià = mittente
    
    def get_destinatario(self):
        return self.destinatario
    
    def set_destinatario(self, destinatario):
        self.destinatario = destinatario
        
    def get_descrizione (self):
        return self.descrizione
    
    def set_descrizione (self, descrizione):
        self.descrizione = descrizione
