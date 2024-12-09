import unittest
from controller.gestore_fisioterapista import GestoreFisioterapista
from model.utente import Utente
import tkinter as Tkk

class TestGestionePazienti(unittest.TestCase):
    def setUp(self):
        self.fisioterapista = Utente("Dott. Rossi", "dottor.rossi@email.com", "password123")
        self.controller = GestoreFisioterapista()

    
    def test_inserisci_modifica_elimina_paziente(self):
        nome = "Mario Bianchi"
        email = "marioBi@gmail.com" 
        password = "pratofiorito"
    
        self.controller.aggiungi_paziente(nome,email, password, Tkk.Tk())
        paziente = self.controller.ottieni_paziente(nome, email)
        
        
        self.assertEqual((paziente.get_nome(), paziente.get_email(), paziente.get_password()), (nome, email, password))
        
        self.controller.modifica_paziente("Mario Neri", "mn@gmail.com", "prato", Tkk.Tk(), paziente)
        self.assertEqual((paziente.get_nome(), paziente.get_email(), paziente.get_password()), ("Mario Neri", "mn@gmail.com", "prato"))

        
        self.controller.elimina_paziente(paziente, Tkk.Tk())
        self.assertIsNone(self.controller.ottieni_paziente(paziente.get_nome(), paziente.get_email()))
        
        
        
        
        