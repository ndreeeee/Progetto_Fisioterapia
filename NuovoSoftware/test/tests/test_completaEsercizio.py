import unittest
from model.esercizio_assegnato import EsercizioAssegnato
from controller.gestore_esercizi import GestoreEsercizi
from controller.gestore_paziente import GestorePaziente
from model.utente import Utente
import tkinter as tk

class TestAggiornaStatoEsercizio(unittest.TestCase):
    def setUp(self):
        self.paziente = Utente("Mario Bianchi", "mario.bianchi@email.com", "password123")
        self.gestore = GestoreEsercizi()
        self.gestorePaz = GestorePaziente()
        self.root = tk.Tk()
        self.root.withdraw()  
        
        self.esercizio_assegnato = EsercizioAssegnato("Mobilizzazione Spalla","Descrizione dell'esercizio","video.mp4")
        self.esercizio_assegnato.set_paziente(self.paziente)
        self.gestore.lista_esercizi_assegnati = [self.esercizio_assegnato]
        self.gestorePaz.set_esercizi_assegnati([self.esercizio_assegnato])
        
        self.stato_var = tk.IntVar(master = self.root)

    def test_completa_esercizio(self):
        
        self.stato_var.set(1)  
        self.gestorePaz.aggiorna_stato_esercizio(self.paziente, self.esercizio_assegnato, self.stato_var)
        
        self.assertEqual(self.esercizio_assegnato.get_stato(), "completato")  
          
    def test_incompleto_esercizio(self):
        
        self.stato_var.set(0)  
        self.gestorePaz.aggiorna_stato_esercizio(self.paziente, self.esercizio_assegnato, self.stato_var)
        self.assertEqual(self.esercizio_assegnato.get_stato(), "incompleto")

if __name__ == "__main__":
    unittest.main()
    
    
    
