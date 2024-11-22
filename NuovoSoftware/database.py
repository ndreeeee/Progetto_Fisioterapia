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
        from model.paziente import Paziente
        from model.fisioterapista import Fisioterapista
        self.cursor.execute("SELECT * FROM messaggi")
        rows=self.cursor.fetchall()
        messaggi = []
            
        for row in rows:
            self.cursor.execute('SELECT * FROM utenti WHERE id=?', (row[2],))  
            mittente = self.cursor.fetchone()
            
            self.cursor.execute('SELECT * FROM utenti WHERE id=?', (row[3],))  
            destinatario = self.cursor.fetchone()
            
        if mittente[3] == 'Fisioterapista':
            mittente_obj = Fisioterapista(mittente[0], mittente[1], mittente[2], mittente[4])
        else:
            mittente_obj = Paziente(mittente[0], mittente[1], mittente[2], mittente[5])
        
        if destinatario[3] == 'Fisioterapista':
            destinatario_obj = Fisioterapista(destinatario[0], destinatario[1], destinatario[2], destinatario[4])
        else:
            destinatario_obj = Paziente(destinatario[0], destinatario[1], destinatario[2], destinatario[5])
        
        messaggio = Messaggio(row[1], mittente_obj, destinatario_obj, row[4])
        
        messaggi_filtrati = []

        for messaggio in messaggi:
            # Controlla se il fisioterapista e il paziente sono mittente e destinatario (o viceversa)
            if (messaggio.mittente == fisioterapista and messaggio.destinatario == paziente) or \
            (messaggio.mittente == paziente and messaggio.destinatario == fisioterapista):
                messaggi_filtrati.append(messaggio)
        messaggi.append(messaggio)
        
        self.conn.close()
        pass
        return messaggi
        
        

            
        
    
        

