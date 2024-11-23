import sqlite3


class Database:
    
    
    def __init__(self, db_name="gestione_fisioterapia.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Tabella utenti (fisioterapisti e pazienti)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS utenti (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL,
                                tipo TEXT NOT NULL CHECK(tipo IN ('fisioterapista', 'paziente'))
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS esercizi (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titolo TEXT NOT NULL UNIQUE,
                                descrizione TEXT NOT NULL,
                                video_url VARCHAR(255)
                                )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cartella_clinica (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paziente INTEGER NOT NULL,
                                data_creazione DATE DEFAULT CURRENT_DATE,
                                data_modifica DATE DEFAULT CURRENT_DATE,
                                descrizione TEXT,
                                FOREIGN KEY (id_paziente) REFERENCES utenti (id) ON DELETE CASCADE
                              )''')
        
        self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS pazienti_esercizi (
                                    id_paziente INTEGER,
                                    id_esercizio INTEGER,
                                    stato TEXT DEFAULT 'incompleto' CHECK(stato IN ('completato', 'incompleto')),
                                    FOREIGN KEY (id_paziente) REFERENCES utenti(id) ON DELETE CASCADE,
                                    FOREIGN KEY (id_esercizio) REFERENCES esercizi(id) ON DELETE CASCADE,
                                    PRIMARY KEY (id_paziente, id_esercizio)
                                );
                            ''')

      
        self.conn.commit()

        
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messaggi (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                mittente_id INTEGER, 
                                destinatario_id INTEGER, 
                                messaggio TEXT, -- Il contenuto del messaggio
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY (mittente_id) REFERENCES utenti(id),
                                FOREIGN KEY (destinatario_id) REFERENCES utenti(id));
                            ''')
        self.conn.commit()
        
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS prenotazioni (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paziente INTEGER,
                                id_fisioterapista INTEGER,
                                data_ora DATETIME NOT NULL,
                                stato TEXT DEFAULT 'disponibile' CHECK(stato IN ('disponibile', 'prenotato')),
                                FOREIGN KEY (id_paziente) REFERENCES utenti(id) ON DELETE SET NULL,
                                FOREIGN KEY (id_fisioterapista) REFERENCES utenti (id) ON DELETE SET NULL
                            )''')
        
        self.conn.commit()
        
    def ottieni_messaggi(self, fisioterapista, paziente):
        from model.messaggio import Messaggio
        
        
        # Recupera tutti i messaggi dal DB
        self.cursor.execute("SELECT * FROM messaggi")
        rows = self.cursor.fetchall()

        
        messaggi = []
        
        for row in rows:
            # Recupera il mittente
            self.cursor.execute('SELECT * FROM utenti WHERE id=?', (row[1],))  # mittente_id
            
            # Recupera il destinatario
            self.cursor.execute('SELECT * FROM utenti WHERE id=?', (row[2],))  # destinatario_id
            destinatario = self.cursor.fetchone()
             
            if destinatario[4] == 'fisioterapista':
                messaggio = Messaggio(row[3], fisioterapista, paziente, row[4])  
                messaggi.append(messaggio)            
            else:
                messaggio = Messaggio(row[3], paziente, fisioterapista, row[4])  
                messaggi.append(messaggio)            
            

        
            # Filtra i messaggi rilevanti tra fisioterapista e paziente
        messaggi_filtrati = [
            m for m in messaggi
            if (m.mittente == fisioterapista and m.destinatario == paziente) or
            (m.mittente == paziente and m.destinatario == fisioterapista)
        ]

        return messaggi_filtrati

        
    def salva_messaggio(self, mittente, destinatario, testo):
        self.cursor.execute('''
                INSERT INTO messaggi (mittente_id, destinatario_id, messaggio)
                VALUES (?, ?, ?)
            ''', (mittente, destinatario, testo))
        self.conn.commit()

        
    def aggiungi_utente(self, nome, email, password, tipo):
       
        try:
            # Controllo validità del tipo
            if tipo not in ('fisioterapista', 'paziente'):
                raise ValueError("Tipo utente non valido. Deve essere 'fisioterapista' o 'paziente'.")
            
            # Inserimento nel database
            self.cursor.execute('''
                INSERT INTO utenti (nome, email, password, tipo)
                VALUES (?, ?, ?, ?)
            ''', (nome, email, password, tipo))
            self.conn.commit()
            print(f"Utente {nome} aggiunto con successo come {tipo}.")
        except sqlite3.IntegrityError as e:
            print(f"Errore: L'email '{email}' è già utilizzata.")
        except ValueError as ve:
            print(f"Errore: {ve}")
        except sqlite3.Error as e:
            print(f"Errore durante l'aggiunta dell'utente: {e}")
            
    def carica_utenti(self):
        from model.fisioterapista import Fisioterapista
        from model.paziente import Paziente
        self.cursor.execute("SELECT * FROM utenti")
        rows = self.cursor.fetchall()
        utenti = []

        for row in rows:
            # Crea l'oggetto utente in base al tipo
            if row[4] == 'fisioterapista':
                utente = Fisioterapista(row[1], row[2], row[3])
            elif row[4] == 'paziente':
                utente = Paziente(row[1], row[2], row[3])

            utenti.append(utente)
        
        return utenti
    
        
            
    
        


        
        

            
        
    
        

