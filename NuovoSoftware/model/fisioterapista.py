from model.utente import Utente




class Fisioterapista(Utente):
    def __init__(self, nome, email, password):
        super().__init__(nome, email, password)
        
        
    def cerca_esercizio (self, query):
        
        risultati = [
            esercizio for esercizio in self.lista_esercizi
            if query.lower() in esercizio.titolo.lower()
        ]
        
        return risultati
    
    
    def __repr__(self):
        return f"Fisio (id = {self.id}, nome={self.nome}, email={self.email}, password= {self.password})"
    
    
            
    
            
    
        
                
    

                
                
    
                        
                        
    
            
  
            

        
            
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    