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
                                descrizione TEXT,
                                FOREIGN KEY (id_paziente) REFERENCES utenti (id) ON DELETE CASCADE
                              )''')
        
        self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS esercizio_assegnato (
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
                                mittente_id INTEGER, -- ID del fisioterapista o del paziente
                                destinatario_id INTEGER, -- ID del destinatario (fisioterapista o paziente)
                                messaggio TEXT, -- Il contenuto del messaggio
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Quando è stato inviato il messaggio
                                FOREIGN KEY (mittente_id) REFERENCES utenti(id),
                                FOREIGN KEY (destinatario_id) REFERENCES utenti(id));
                            ''')
        
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS prenotazioni (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_paziente INTEGER,
                                data_ora DATETIME NOT NULL,
                                stato TEXT DEFAULT 'disponibile' CHECK(stato IN ('disponibile', 'prenotato')),
                                FOREIGN KEY (id_paziente) REFERENCES utenti(id) ON DELETE SET NULL
                        )''')
        
        self.conn.commit()
        
        
        
    def aggiungi_utente(self, nome, email, password, tipo):
        self.cursor.execute("INSERT INTO utenti (nome, email, password, tipo) VALUES (?, ?, ?, ?)", 
                            (nome, email, password, tipo))
        self.conn.commit()


    



        
        
    
    
    
      
    
  
  

        
    