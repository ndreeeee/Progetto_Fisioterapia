import unittest
from model.utente import Utente
from controller.gestore_esercizi import GestoreEsercizi
import tkinter as tkk

class TestGestioneEsercizi(unittest.TestCase):
    def setUp(self):
        self.fisioterapista = Utente("Dott. Rossi", "dottor.rossi@email.com", "password123")
        self.controller = GestoreEsercizi()
        self.root = tkk.Tk()

    def test_inserisci_modifica_elimina_esercizio(self):
        titolo = "Mobilizzazione della Spalla per la Rigidità Articolare"
        descrizione = ("Questo esercizio è pensato per migliorare la mobilità della spalla e "
                       "alleviare la rigidità articolare. Seduti o in piedi, il paziente solleva lentamente "
                       "il braccio affetto, eseguendo movimenti circolari controllati e in tutte le direzioni "
                       "per 5 minuti, senza superare il punto di dolore. Ripetere 3 volte al giorno per favorire "
                       "l’aumento della flessibilità e della circolazione nella zona articolare")
        nuovo_titolo = "Rafforzamento dei Muscoli del Core con la Plank Modificata"
        nuova_descrizione = ("L’esercizio della plank modificata mira a rafforzare i muscoli del core, "
                             "fondamentali per la stabilità e l’equilibrio")
        
        self.controller.aggiungi_esercizio(titolo, descrizione, "", self.root)
    
        esercizio = self.controller.ottieni_esercizio(titolo)
        self.assertEqual((esercizio.get_titolo(), esercizio.get_descrizione(), esercizio.get_video()), (titolo, descrizione, ""))
        
        self.controller.modifica_esercizio(nuovo_titolo, nuova_descrizione, "https://www.youtube.com/watch?v=lesaJhWyZzA", esercizio)
        self.assertNotEqual((titolo, descrizione), (nuovo_titolo, nuova_descrizione))
        
        self.controller.elimina_esercizio(esercizio.get_titolo())
        self.assertIsNone(self.controller.ottieni_esercizio(esercizio.get_titolo()))

        
        
        
        