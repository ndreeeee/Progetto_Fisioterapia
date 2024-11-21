import tkinter as tk

from tkinter import scrolledtext  
import tkinter.ttk as ttk
from tkinter import font, messagebox, simpledialog, filedialog

class MostraFormAggiungiEsercizio:
    def __init__(self, root, fisioterapista):
        self.root = root
        self.fisioterapista = fisioterapista
        self.file_video_path = ""
        

        form_window = tk.Toplevel(self.root)
        form_window.title("Aggiungi nuovo Esercizio")
        
        self.main_frame = tk.Frame(form_window, width=900, height=700)
        self.main_frame.pack_propagate(False)  
        self.main_frame.pack(pady=10)
        
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"))
        
        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
        ttk.Label(self.main_frame, text="Titolo Esercizio", font=("Arial", 12)).pack(pady=5)
        titolo_entry = ttk.Entry(self.main_frame, font=("Arial", 12), width=40)
        titolo_entry.pack(pady=10)
        
        
        ttk.Label(self.main_frame, text="Descrizione", font=("Arial", 12)).pack(pady=5)
        descrizione_entry = tk.Text(self.main_frame, height=5, width=40)  
        descrizione_entry.pack(pady=10)
        
        self.upload_button = ttk.Button(self.main_frame, text="Carica un Video", command=self.carica_file_video)
        self.upload_button.pack(pady=20, ipadx=10, ipady=5)

        self.file_label = ttk.Label(self.main_frame, text="Nessun file selezionato", font=("Arial", 12)).pack(pady=5)
        
        submit_button = ttk.Button(self.main_frame, text="Aggiungi Esercizio", 
                                  command=lambda: self.aggiungi_esercizio(titolo_entry.get(), 
                                                                          descrizione_entry.get("1.0", "end-1c"), 
                                                                          self.file_video_path, form_window))
        submit_button.pack(pady=20, ipadx=10, ipady=5)
        
        back_button = ttk.Button(self.main_frame, text="Torna Indietro", command=form_window.destroy)
        back_button.pack(pady=20, ipadx=10, ipady=5)
        
        self.spazio2 = ttk.Label(self.main_frame)
        self.spazio2.pack(expand=True)
        
    def carica_file_video(self):
        file_path = simpledialog.askstring("Carica Video", "Inserisci l'URL del video:")
        if file_path:
            self.file_video_path = file_path  
            self.file_label.config(text=f"Video selezionato: {file_path.split('/')[-1]}")
        
        
    def aggiungi_esercizio (self, titolo, descrizione, video_url, window):
        if titolo and descrizione:
            video_url = ""
        self.fisioterapista.aggiungi_nuovo_esercizio(titolo, descrizione, video_url)        
        window.destroy()
        