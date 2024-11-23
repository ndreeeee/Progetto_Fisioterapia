from datetime import date
import sqlite3
from datetime import datetime

class Messaggio():
    
    _id_counter = 1
    
    def __init__(self, descrizione, destinatario, mittente, data_invio = None):
        
        self.codice=Messaggio._id_counter
        Messaggio._id_counter += 1
        
        self.data_invio = data_invio if data_invio else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.descrizione=descrizione
        self.destinatario=destinatario
        self.mittente=mittente
