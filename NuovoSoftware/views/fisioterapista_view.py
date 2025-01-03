import tkinter as tk
import tkinter.ttk as ttk
from views.cerca_paziente_view import CercaPazienteView
from views.aggiungi_paziente_view import AggiungiPazienteView
from views.mostra_lista_esercizi_view import MostraListaEsercizi
from views.prenotazioni_fisio_view import PrenotazioniFisio
from backup import backup_database



# width=700, height=600
class FisioterapistaView(tk.Frame):
    def __init__(self, root, fisioterapista, gestore, gestoreEsercizi):
        self.root = root
        self.file_video_path = ""
        self.fisioterapista = fisioterapista
        self.gestore = gestore
        self.gestoreEsercizi = gestoreEsercizi

        self.main_frame = tk.Frame(self.root, width=900, height=700)
        self.main_frame.pack_propagate(False)  
        self.main_frame.pack()
        
        self.spazio = tk.Label(self.main_frame)
        self.spazio.pack(expand=True)

        self.label = ttk.Label(self.main_frame, text=f"Benvenuto, {self.fisioterapista.get_nome()}", font=("Arial", 18, "bold"))
        self.label.pack(pady=20)
        
        button_font = ("Arial", 14, "bold") 

        self.cerca_pazienti_button = ttk.Button(self.main_frame, text="Cerca Paziente", command=lambda: CercaPazienteView(0, self.root, self.fisioterapista, self.gestore, self.gestoreEsercizi), 
                                                width=20, style='TButton')
        self.cerca_pazienti_button.pack(pady=20, ipadx=20, ipady=10)

        self.aggiungi_paziente_button = ttk.Button(self.main_frame, text="Aggiungi Paziente", command=lambda: AggiungiPazienteView(self.root, self.fisioterapista, self.gestore), width=20, style='TButton')
        self.aggiungi_paziente_button.pack(pady=20, ipadx=20, ipady=10)
        
        self.mostra_esercizi_button = ttk.Button(self.main_frame, text="Lista Esercizi", command=lambda: MostraListaEsercizi(self.root, self.fisioterapista, self.gestoreEsercizi), width=20, style='TButton')
        self.mostra_esercizi_button.pack(pady=20, ipadx=20, ipady=10)
        
        self.messaggia_paziente_button = ttk.Button(self.main_frame, text="Messaggia Paziente", command=lambda: CercaPazienteView(1, self.root, self.fisioterapista, self.gestore, self.gestoreEsercizi), width=20, style='TButton')
        self.messaggia_paziente_button.pack(pady=20, ipadx=20, ipady=10)

        self.prenotazione_button = ttk.Button(self.main_frame, text="Prenotazioni", command=lambda: PrenotazioniFisio(self.root, self.fisioterapista, self.gestore), width=20, style='TButton')
        self.prenotazione_button.pack(pady=20, ipadx=20, ipady=10)
        

        
        self.esegui_backup_ = ttk.Button(self.main_frame, text="Esegui Backup", command=lambda: backup_database(), width=20, style='TButton')
        self.esegui_backup_.pack(pady=20, ipadx=20, ipady=10)

     
        style = ttk.Style()
        style.configure('TButton', font=button_font)  
        
        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
      
        

   
        
        
        
        
        
        