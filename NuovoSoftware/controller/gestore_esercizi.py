from controller.gestore_dati import GestoreDati
from model.esercizio import Esercizio
from tkinter import messagebox


class GestoreEsercizi:
    def __init__(self):
        self.lista_esercizi = []
        self.lista_esercizi_assegnati =  []
        
        
    def set_lista_esercizi(self, esercizi):
        self.lista_esercizi = esercizi
        
    def get_esercizi(self):
        return self.lista_esercizi
        
    def aggiungi_esercizio (self, titolo, descrizione, video_url, window):
        if titolo and descrizione:
            if not video_url:
                video_url = ""
            esercizio = Esercizio(titolo, descrizione, video_url)
            self.lista_esercizi.append(esercizio)
            GestoreDati().inserisci_esercizio(titolo, descrizione, video_url)      
            window.destroy()
            messagebox.showinfo("Success", "Esercizio aggiunto con successo!!!")
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori!")
            
    def elimina_esercizio(self, titolo):
        for esercizio in self.lista_esercizi:
            if esercizio.titolo == titolo:
                self.lista_esercizi.remove(esercizio)
                GestoreDati().elimina_esercizio(esercizio.get_id())
        
        messagebox.showinfo("Successo", "Esercizio eliminato con successo!!")
        
        
    def modifica_esercizio(self, titolo, descrizione, video, esercizio1):
        
        for esercizio in self.lista_esercizi:
            if esercizio.get_titolo() == esercizio1.titolo:
                esercizio.set_modifica_esercizio(titolo, descrizione, video)
                
                GestoreDati().modifica_esercizio(esercizio)
                
        messagebox.showinfo("Successo", "Esercizio modificato con successo!!")

                
    def ottieni_esercizio(self, titolo):
        for esercizio in self.lista_esercizi:
            if titolo == esercizio.get_titolo():
                return esercizio
            
    def set_esercizi_assegnati(self, lista_esercizi_assegnati):
        self.lista_esercizi_assegnati = lista_esercizi_assegnati
        
    def get_esercizi_assegnati(self):
        return self.lista_esercizi_assegnati
    
    def get_esercizi_assegnati_per_paziente(self, paziente):
        esercizi_filtrati = [
            esercizio for esercizio in self.lista_esercizi_assegnati
            if esercizio.get_paziente()
                if esercizio.get_paziente().get_id() == paziente.get_id()  # Confronta gli ID
        ]
        return esercizi_filtrati
    
    def cerca_esercizio (self, query):
        
        risultati = [
            esercizio for esercizio in self.lista_esercizi
            if query.lower() in esercizio.titolo.lower()
        ]
        
        return risultati
    
    
    
    def aggiungi_esercizio_assegnato(self, paziente, esercizio):
        from model.esercizio_assegnato import EsercizioAssegnato
        from controller.gestore_dati import GestoreDati

        esercizio_assegnato = EsercizioAssegnato(
            esercizio.get_titolo(),
            esercizio.get_descrizione(),
            esercizio.get_video()
        )
        esercizio_assegnato.set_paziente(paziente)
        esercizio_assegnato.set_stato("incompleto")  # Stato iniziale

        self.lista_esercizi_assegnati.append(esercizio_assegnato)
        GestoreDati().aggiungi_esercizio_assegnato(paziente.get_id(), esercizio.get_id())
        
    
    def rimuovi_esercizio_assegnato(self, titolo):
        for esercizio in self.lista_esercizi_assegnati:
           if esercizio.get_titolo() == titolo:
               self.lista_esercizi_assegnati.remove(esercizio)
               print("Gestore", esercizio)
               GestoreDati().rimuovi_esercizio_assegnato(esercizio.get_id())
               
    def get_esercizio(self, titolo):
        for esercizio in self.lista_esercizi_assegnati:
            if esercizio.get_titolo() == titolo:
                return esercizio



        
        
        
        