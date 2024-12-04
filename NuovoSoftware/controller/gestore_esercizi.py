from controller.gestore_dati import GestoreDati
from model.esercizio import Esercizio
from tkinter import messagebox


class GestoreEsercizi:
    def __init__(self):
        self.lista_esercizi = []
        
        
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
            
                esercizio.set_titolo(titolo)
                esercizio.set_descrizione(descrizione)
                esercizio.set_video(video)
                GestoreDati().modifica_esercizio(esercizio)
                
        messagebox.showinfo("Successo", "Esercizio modificato con successo!!")

                
    def ottieni_esercizio(self, titolo):
        for esercizio in self.lista_esercizi:
            if titolo == esercizio.get_titolo():
                return esercizio
        
        
        
        
        