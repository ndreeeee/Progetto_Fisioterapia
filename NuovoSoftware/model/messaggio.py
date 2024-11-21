from model.utente import Utente
from datetime import date
import sqlite3

class Messaggio():
    def __init__(self, codice, data_invio, descrizione, destinatario, mittente):
        self.codice=codice
        self.data_invio=data_invio
        self.descrizione=descrizione
        self.destinatario=destinatario
        self.mittente=mittente
    
    def to_dict(self):
        return {
            "codice": self.codice,
            "data_invio": self.data_invio.isoformat(),
            "descrizione": self.descrizione,
            "destinatario": self.destinatario.nome,
            "mittente": self.mittente.nome
        }
    
    def invia_messaggio(self, mittente, destinatario, testo):
        if not testo:
            raise ValueError("Il messaggio non può essere vuoto.")
        codice = self.genera_codice_unico()
        nuovo_messaggio = self(
            codice=codice,
            data_invio=date.today(),
            descrizione=testo,
            destinatario=destinatario,
            mittente=mittente
        )
        self.salva_su_database(nuovo_messaggio)
        
    
    def genera_codice_unico():
        from random import randint
        return randint(1000, 9999)
    
    def salva_su_database(messaggio):
        conn = sqlite3.connect('messaggi.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messaggi (
                codice INTEGER PRIMARY KEY,
                data_invio TEXT,
                descrizione TEXT,
                destinatario_nome TEXT,
                mittente_nome TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO messaggi (codice, data_invio, descrizione, destinatario_nome, mittente_nome)
            VALUES (?, ?, ?, ?, ?)
        ''', (messaggio.codice, messaggio.data_invio.isoformat(), messaggio.descrizione, 
              messaggio.destinatario.nome, messaggio.mittente.nome))
        
        conn.commit()
        conn.close()

    def visualizza_messaggi(mittente, destinatario):
        conn = sqlite3.connect('messaggi.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT codice, data_invio, descrizione, destinatario_nome, mittente_nome
            FROM messaggi
            WHERE (mittente_nome = ? AND destinatario_nome = ?)
               OR (mittente_nome = ? AND destinatario_nome = ?)
            ORDER BY data_invio
        ''', (mittente.nome, destinatario.nome, destinatario.nome, mittente.nome))
        messaggi = cursor.fetchall()
        conn.close()
        lista_messaggi = []
        for codice, data_invio, descrizione, destinatario_nome, mittente_nome in messaggi:
            lista_messaggi.append({
                "codice": codice,
                "data_invio": data_invio,
                "descrizione": descrizione,
                "mittente": mittente_nome,
                "destinatario": destinatario_nome
            })
        
        return lista_messaggi
    