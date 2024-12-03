import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


class PrenotazioniView(tk.Toplevel):
    
    
    
    
    def __init__(self, root, paziente, posti_disponibili, gestore_dati):
        super().__init__(root)
        self.root = root
        self.title("Prenotazioni disponibili")
        self.geometry("900x700")  
        self.posti_disponibili = posti_disponibili
        self.gestore_dati = gestore_dati
        
        self.paziente = paziente
        self.posti_prenotati = paziente.get_prenotazioni()
        
        

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
            print(prenotazione)
            self.prenotazioni_lista.insert('', 'end', values=(prenotazione.codice, 
                                                              prenotazione.data_e_ora, prenotazione.stato))

    def carica_prenotazioni_effettuate(self, prenotati):
        for item in self.prenotazioni_effettuate_lista.get_children():
            self.prenotazioni_effettuate_lista.delete(item)

        for prenotazione in prenotati:
            self.prenotazioni_effettuate_lista.insert('', 'end', values=(prenotazione.codice, 
                                                                        prenotazione.data_e_ora, 
                                                                        prenotazione.stato))

            
    def prenota(self):
        # Ottieni l'elemento selezionato
        selected_item = self.prenotazioni_lista.selection()
        if not selected_item:
            messagebox.showerror("Errore", "Seleziona una prenotazione")
            return

        # Ottieni i valori della riga selezionata
        prenotazione_valori = self.prenotazioni_lista.item(selected_item)['values']
        codice_selezionato = prenotazione_valori[0]  # Supponendo che il codice sia il primo valore
        
        # Trova l'oggetto Prenotazione corrispondente
        prenotazione_da_prenotare = next(
            (p for p in self.posti_disponibili if p.codice == codice_selezionato),
            None
        )
        
        if not prenotazione_da_prenotare:
            messagebox.showerror("Errore", "Prenotazione non trovata!")
            return

        try:
            self.paziente.prenota(prenotazione_da_prenotare)
            self.posti_disponibili.remove(prenotazione_da_prenotare)
            
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
            (p for p in self.posti_prenotati if p.codice == codice_selezionato),
            None
        )

        risposta = messagebox.askyesno("Conferma", "Sei sicuro di voler cancellare la prenotazione?")
        if risposta:
            try:
                self.paziente.elimina_prenotazione(prenotazione_da_eliminare)

                self.prenotazioni_effettuate_lista.delete(selected_item)
                self.posti_disponibili.append(prenotazione_da_eliminare)

                self.carica_prenotazioni_disponibili(self.posti_disponibili)  
                self.carica_prenotazioni_effettuate(self.posti_prenotati)


                messagebox.showinfo("Successo", "Prenotazione cancellata e ora disponibile!")
            except Exception as e:
                messagebox.showerror("Errore", str(e))


