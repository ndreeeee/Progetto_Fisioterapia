from controller.gestore_dati import GestoreDati
from model.messaggio import Messaggio

class GestoreMessaggi():
    def __init__(self):
        self.messaggi = []
        
    
    def get_messaggi (self):
        return self.messaggi
    
    def set_messaggi(self, messaggi):
        self.messaggi = messaggi
        
    def invia_messaggio(self, mittente, destinatario, testo):
        messaggio = Messaggio(testo, destinatario, mittente)
        self.messaggi.append(messaggio)
        GestoreDati().salva_messaggio(messaggio, mittente.get_id(), destinatario.get_id())
    
    def ottieni_messaggi(self, paziente, fisioterapista):
        
        if not self.messaggi:
            print("Nessun messaggio trovato nella lista.")
            return []
        messaggi_filtrati = []
        
        for messaggio in self.messaggi:  # Assume che self.lista_messaggi contenga tutti i messaggi
            mittente = messaggio.get_mittente()
            destinatario = messaggio.get_destinatario()

        # Verifica se i mittente e destinatario corrispondono agli utenti specificati
        if ((mittente.get_email() == fisioterapista.get_email() and destinatario.get_email() == paziente.get_email()) or
            (mittente.get_email() == paziente.get_email() and destinatario.get_email() == fisioterapista.get_email())):
            messaggi_filtrati.append(messaggio)
        print ("gestore", messaggi_filtrati)
        print ("gestore", self.messaggi)
        return messaggi_filtrati
        
