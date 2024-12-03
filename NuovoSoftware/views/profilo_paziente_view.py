import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
from views.cartella_clinica_fisio_view import CartellaClinicaFisio
from views.modifica_paziente_view import ModificaPaziente
from views.gestisci_esercizi_paziente_view import GestisciEsercizi

class ProfiloPaziente:
    def __init__(self, root, paziente, gestore):
        self.root = root
        self.paziente = paziente
        self.gestore = gestore
        
        search_frame = tk.Toplevel(self.root)
        search_frame.title(f"Profilo di {paziente.nome}")

        profilo_paziente_window = ttk.Frame(search_frame, width=900, height=700)
        profilo_paziente_window.pack_propagate(False)
        profilo_paziente_window.pack(pady=20, padx=20)

        self.spazio = ttk.Label(profilo_paziente_window)
        self.spazio.pack(expand=True)
        
        button_font = ("Arial", 14, "bold")  


        # Mostra i dettagli del paziente
        ttk.Label(profilo_paziente_window, text=f"Nome: {self.paziente.nome}", font=("Arial", 12, 'bold')).pack(pady=10)
        ttk.Label(profilo_paziente_window, text=f"Email: {self.paziente.email}", font=("Arial", 12)).pack(pady=10)
        
        titolo_font = font.Font(family="Arial", size=14, weight="bold")
        testo_font = font.Font(family="Arial", size=12)
        """
        percentuale = self.fisioterapista.calcola_percentuale_completamento(id_paziente)
        
        percentuale_label = tk.Label(profilo_paziente_window, text=f"Completamento Terapia: {percentuale:.2f}%", font=titolo_font)
        percentuale_label.pack(pady=20)

        progressbar = ttk.Progressbar(profilo_paziente_window, orient="horizontal", length=300, mode="determinate")
        progressbar.pack(pady=20)

        progressbar['value'] = percentuale
        """
        # Pulsanti per gestire la cartella clinica e gli esercizi
        ttk.Button(profilo_paziente_window, text="Cartella Clinica", 
                command=lambda: CartellaClinicaFisio(self.root, self.paziente, self.gestore), style="TButton").pack(pady=20, ipadx=20, ipady=10)
        ttk.Button(profilo_paziente_window, text="Gestisci Esercizi", 
                command=lambda: GestisciEsercizi(self.root, self.paziente), style="TButton").pack(pady=20, ipadx=20, ipady=10)

        # Pulsante per modificare il paziente
        ttk.Button(profilo_paziente_window, text="Modifica Paziente", 
                command=lambda: ModificaPaziente(search_frame, self.paziente, self.gestore), style="TButton").pack(pady=20, ipadx=20, ipady=10)
        
                    # Pulsante per eliminare il paziente
        ttk.Button(profilo_paziente_window, text="Elimina Paziente", 
                command=lambda: self.gestore.elimina_paziente(self.paziente, search_frame), style="TButton").pack(pady=20, ipadx=20, ipady=10)

        # Pulsante per tornare indietro
        ttk.Button(profilo_paziente_window, text="Torna Indietro", 
                command=search_frame.destroy, style="TButton").pack(pady=20, ipadx=20, ipady=10)

        style = ttk.Style()
        style.configure('TButton', font=button_font) 
        self.spazio2 = ttk.Label(profilo_paziente_window)
        self.spazio2.pack(expand=True)
            

    
    


