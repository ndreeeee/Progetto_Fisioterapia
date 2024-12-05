import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


class PrenotazioniView(tk.Toplevel):
    
    
    
    
    def __init__(self, root, paziente, gestore, gestorePrenotazioni):
        super().__init__(root)
        self.root = root
        self.title("Prenotazioni disponibili")
        self.geometry("900x700")  
        self.gestorePrenotazioni = gestorePrenotazioni
        self.gestore = gestore
        self.paziente = paziente
        
        self.posti_disponibili = self.gestorePrenotazioni.get_prenotazioni_disponibili()
        
        self.posti_prenotati = self.gestore.get_prenotazioni(paziente.get_id())
        
        

        self.prenotazioni_effettuate_lista = ttk.Treeview(self, columns=("ID", "Data e Ora", "Stato"), show="headings")
        self.prenotazioni_effettuate_lista.heading("ID", text="ID")
        self.prenotazioni_effettuate_lista.heading("Data e Ora", text="Data e Ora")
        self.prenotazioni_effettuate_lista.heading("Stato", text="Stato")
        self.prenotazioni_effettuate_lista.column("ID", width=100)  
        self.prenotazioni_effettuate_lista.column("Data e Ora", width=200) 
        self.prenotazioni_effettuate_lista.column("Stato", width=100)  
        self.prenotazioni_effettuate_lista.pack(fill=tk.BOTH, expand=True, pady=10)

        self.cancella_prenotazione_effettuata_btn = ttk.Button(self, text="Cancella Prenotazione Effettuata", command = self.cancella_prenotazione_effettuata)
        self.cancella_prenotazione_effettuata_btn.pack(pady=10)

        self.prenotazioni_lista = ttk.Treeview(self, columns=("ID", "Data e Ora", "Stato"), show="headings")
        self.prenotazioni_lista.heading("ID", text="ID")
        self.prenotazioni_lista.heading("Data e Ora", text="Data e Ora")
        self.prenotazioni_lista.heading("Stato", text="Stato")
        self.prenotazioni_lista.column("ID", width=100) 
        self.prenotazioni_lista.column("Data e Ora", width=200)  
        self.prenotazioni_lista.column("Stato", width=100)  
        self.prenotazioni_lista.pack(fill=tk.BOTH, expand=True)

        self.prenota_btn = ttk.Button(self, text="Prenota", command=self.prenota)
        self.prenota_btn.pack(pady=10)

        self.torna_indietro_btn = ttk.Button(self, text="Torna Indietro", command=self.destroy)
        self.torna_indietro_btn.pack(pady=10)

        #self.controller.elimina_prenotazioni_scadute()
        self.carica_prenotazioni_disponibili(self.posti_disponibili)
        self.carica_prenotazioni_effettuate(self.posti_prenotati)

    def carica_prenotazioni_disponibili(self, disponibili):
        for item in self.prenotazioni_lista.get_children():
            self.prenotazioni_lista.delete(item)
    
        for prenotazione in disponibili:
            self.prenotazioni_lista.insert('', 'end', values=(prenotazione.get_id(), 
                                                              prenotazione.get_data_e_ora(), prenotazione.get_stato()))

    def carica_prenotazioni_effettuate(self, prenotati):
        for item in self.prenotazioni_effettuate_lista.get_children():
            self.prenotazioni_effettuate_lista.delete(item)

        for prenotazione in prenotati:
            self.prenotazioni_effettuate_lista.insert('', 'end', values=(prenotazione.get_id(), 
                                                                        prenotazione.get_data_e_ora(), 
                                                                        prenotazione.get_stato()))

    def prenota(self):
        selected_item = self.prenotazioni_lista.selection()
        if not selected_item:
            messagebox.showerror("Errore", "Seleziona una prenotazione")
            return

        prenotazione_valori = self.prenotazioni_lista.item(selected_item)['values']
        codice_selezionato = prenotazione_valori[0] 

        prenotazione_da_prenotare = next(
            (p for p in self.posti_disponibili if p.get_id() == codice_selezionato),
            None
        )

        if not prenotazione_da_prenotare:
            messagebox.showerror("Errore", "Prenotazione non trovata!")
            return

        try:
            # Cambia lo stato della prenotazione e associa il paziente
            prenotazione_da_prenotare.stato = "prenotato"
            prenotazione_da_prenotare.paziente = self.paziente

            # Salva il cambiamento nel database
            self.gestorePrenotazioni.prenota(prenotazione_da_prenotare)

            # Aggiorna le liste in memoria
            self.posti_disponibili.remove(prenotazione_da_prenotare)
            self.posti_prenotati.append(prenotazione_da_prenotare)

            # Aggiorna le viste
            self.carica_prenotazioni_disponibili(self.posti_disponibili)
            self.carica_prenotazioni_effettuate(self.posti_prenotati)

            messagebox.showinfo("Successo", "Prenotazione avvenuta con successo!")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

            
            
    def cancella_prenotazione_effettuata(self):
        selected_item = self.prenotazioni_effettuate_lista.selection()
        if not selected_item:
            messagebox.showerror("Errore", "Seleziona una prenotazione da cancellare")
            return

        prenotazione = self.prenotazioni_effettuate_lista.item(selected_item)['values']
        codice_selezionato = prenotazione[0]
        
        prenotazione_da_eliminare = next(
            (p for p in self.posti_prenotati if p.get_id() == codice_selezionato),
            None
        )

        risposta = messagebox.askyesno("Conferma", "Sei sicuro di voler cancellare la prenotazione?")
        if risposta:
            try:
                self.gestorePrenotazioni.elimina_prenotazione(prenotazione_da_eliminare)

                self.prenotazioni_effettuate_lista.delete(selected_item)
                self.posti_disponibili.append(prenotazione_da_eliminare)

                self.carica_prenotazioni_disponibili(self.posti_disponibili)  
                self.carica_prenotazioni_effettuate(self.posti_prenotati)


                messagebox.showinfo("Successo", "Prenotazione cancellata e ora disponibile!")
            except Exception as e:
                messagebox.showerror("Errore", str(e))


