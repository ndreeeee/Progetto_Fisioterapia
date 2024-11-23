from database import Database

if __name__ == "__main__":
    db = Database()
    
    """
    db.aggiungi_utente("Mario Rossi", "dottor.rossi@email.com", "password123", "fisioterapista")
    db.aggiungi_utente("Marco Bianchi", "marco@email.com", "password123", "paziente")
    print("Database inizializzato e popolato con utenti di esempio.")"""
    
    db.cursor.execute("DELETE FROM messaggi")
    db.conn.commit()  # Conferma la modifica nel database
    print("Tutti i messaggi sono stati cancellati.")
    db.conn.close()