from controller.gestore_dati import GestoreDati


class GestoreEsercizi:
    def __init__(self):
        self.lista_esercizi = GestoreDati().get_esercizi()
        
        
    def get_esercizi(self):
        return self.lista_esercizi
        
    def aggiungi_esercizio (self, titolo, descrizione, video_url, window, fisioterapista):
        self.fisioterapista = fisioterapista
        if titolo and descrizione:
            if not video_url:
                video_url = ""
        self.fisioterapista.aggiungi_nuovo_esercizio(titolo, descrizione, video_url)  
        GestoreDati().inserisci_esercizio(titolo, descrizione, video_url)      
        window.destroy()
        
        
        
        