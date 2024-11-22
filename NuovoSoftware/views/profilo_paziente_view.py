import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog
from views.cartella_clinica_fisio_view import CartellaClinicaFisio
from views.modifica_paziente_view import ModificaPaziente
from views.gestisci_esercizi_paziente_view import GestisciEsercizi

class ProfiloPaziente:
    def __init__(self, root, paziente, fisioterapista):
        self.root = root
        self.paziente = paziente
        self.fisioterapista = fisioterapista
       
        
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
                command=lambda: CartellaClinicaFisio(self.root, self.paziente, self.fisioterapista), style="TButton").pack(pady=20, ipadx=20, ipady=10)
        ttk.Button(profilo_paziente_window, text="Gestisci Esercizi", 
                command=lambda: GestisciEsercizi(self.root, self.paziente, self.fisioterapista), style="TButton").pack(pady=20, ipadx=20, ipady=10)

        # Pulsante per modificare il paziente
        ttk.Button(profilo_paziente_window, text="Modifica Paziente", 
                command=lambda: ModificaPaziente(search_frame, paziente, fisioterapista), style="TButton").pack(pady=20, ipadx=20, ipady=10)
        
                    # Pulsante per eliminare il paziente
        ttk.Button(profilo_paziente_window, text="Elimina Paziente", 
                command=lambda: self.elimina_paziente(id_paziente, search_frame), style="TButton").pack(pady=20, ipadx=20, ipady=10)

        # Pulsante per tornare indietro
        ttk.Button(profilo_paziente_window, text="Torna Indietro", 
                command=search_frame.destroy, style="TButton").pack(pady=20, ipadx=20, ipady=10)

        style = ttk.Style()
        style.configure('TButton', font=button_font) 
        self.spazio2 = ttk.Label(profilo_paziente_window)
        self.spazio2.pack(expand=True)
            
    def elimina_paziente(self, id_paziente, finestra_profilo):
        risposta = messagebox.askyesno("Conferma Eliminazione", "Sei sicuro di voler eliminare questo paziente?")
        
        if risposta:
            # Rimuove il paziente dal database
            self.controller.elimina_paziente(id_paziente)
            self.visualizza_tutti_pazienti()  # Ricarica la lista dei pazienti

            
            # Chiude la finestra del profilo
            finestra_profilo.destroy()

            
            # Rimuove il paziente dalla listbox principale (aggiorna l'interfaccia)
            
            messagebox.showinfo("Successo", "Paziente eliminato con successo.")
    
    def aggiorna_ricerca(self, event):
    # Funzione per aggiornare i risultati della ricerca dinamica
        query = self.search_entry.get().strip()  # Rimuove spazi bianchi iniziali e finali
        if query:
            # Esegue la ricerca solo se ci sono caratteri nella query
            risultati = self.controller.cerca_pazienti(query)
            self.results_listbox.delete(0, tk.END)  # Pulisce la Listbox

            if risultati:
                for paziente in risultati:
                    try:
                        # Correggi l'accesso ai dati del paziente
                        self.results_listbox.insert(tk.END, f"ID: {paziente['id']}, Nome: {paziente['nome']}, Email: {paziente['email']}")
                    except KeyError:
                        self.results_listbox.insert(tk.END, "Dati paziente non validi.")
            else:
                self.results_listbox.insert(tk.END, "Nessun paziente trovato.")
        else:
            # Se la query è vuota, mostra tutti i pazienti
            self.visualizza_tutti_pazienti()  # Chiamata al metodo per visualizzare tutti i pazienti


