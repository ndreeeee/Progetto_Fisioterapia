
class Esercizio:
    

    
    def __init__(self, titolo, descrizione, video):
        
        self.id = -1
        self.descrizione = descrizione
        self.titolo = titolo
        self.video = video
        
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
 
    def get_video (self):
        return self.video
    
    def get_titolo(self):
        return self.titolo
    
    def get_descrizione(self):
        return self.descrizione
    
    def set_descrizione(self, descrizione):
        self.descrizione = descrizione
    
    def set_titolo (self, titolo):
        self.titolo = titolo
        
    def set_video(self, video):
        self.video = video