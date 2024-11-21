import tkinter as tk
from tkinter import scrolledtext
from model.messaggio import Messaggio
from tkinter import font
import tkinter.ttk as ttk




class MessaggiView:
    def __init__(self, root, paziente_id, fisioterapista_id, flag):
        self.root = root
        self.paziente_id = paziente_id
        self.fisioterapista_id = fisioterapista_id
        self.controller = Messaggio()
        self.flag = flag

        # Definizione di font moderni
        self.titolo_font = font.Font(family="Arial", size=20, weight="bold")
        self.messaggio_font = font.Font(family="Arial", size=12)
        
        button_font = ("Arial", 14, "bold")  # Font più grande e in grassetto
     


        # Creazione della finestra per la chat con dimensioni fisse
        self.main_frame = tk.Frame(self.root, width=900, height=700, bg="#f0f0f0")
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(padx=20, pady=20)

        # Titolo della sezione
        self.label = tk.Label(self.main_frame, text="Chat", font=self.titolo_font, bg="#f0f0f0")
        self.label.pack(pady=10)

        # ScrolledText per visualizzare i messaggi, con un'estetica migliorata
        self.chat_area = scrolledtext.ScrolledText(
            self.main_frame, 
            wrap=tk.WORD, 
            width=80, 
            height=20, 
            state='disabled', 
            font=self.messaggio_font, 
            bg="#ffffff", 
            fg="#333333",
            bd=2, 
            relief="flat"
        )
        self.chat_area.pack(padx=10, pady=10)

        # Frame per input e bottone
        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

        # Entry per inserire il nuovo messaggio con uno stile moderno
        self.input_text = tk.Entry(
            self.input_frame, 
            width=60, 
            font=self.messaggio_font, 
            bg="#ffffff", 
            fg="#333333", 
            bd=2, 
            relief="flat"
        )
        self.input_text.pack(side=tk.LEFT, padx=10)

        # Bottone per inviare il messaggio con uno stile moderno
        self.send_button = tk.Button(
            self.input_frame, 
            text="Invia", 
            command=lambda: self.invia_messaggio(self.flag),
            bg="#4CAF50", 
            fg="white", 
            font=self.messaggio_font, 
            bd=0, 
            relief="flat", 
            padx=15, 
            pady=5
        )
        self.send_button.pack(side=tk.LEFT, padx=10)
        
        indietro_button = ttk.Button(self.main_frame, text="Torna indietro", command=self.root.destroy, style='TButton')
        indietro_button.pack(pady=20, ipadx=20, ipady=10)
        
        style = ttk.Style()
        style.configure('TButton', font=button_font) 

        # Carica i messaggi esistenti
        self.carica_messaggi()

    def invia_messaggio(self, flag):
        # Recupera il testo dall'input
        testo = self.input_text.get()

        if testo.strip():  # Verifica che il messaggio non sia vuoto
            # Invia il messaggio usando il controller
            if flag == 1:
                self.controller.invia_messaggio(self.fisioterapista_id, self.paziente_id, testo)
            else:
                self.controller.invia_messaggio(self.paziente_id, self.fisioterapista_id, testo)

            


            # Azzera il campo di input dopo l'invio
            self.input_text.delete(0, tk.END)

            # Ricarica i messaggi per mostrare quello nuovo
            self.carica_messaggi()


    def carica_messaggi(self):
        """Carica e visualizza i messaggi nella chat."""
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)

        # Ottieni tutti i messaggi tra paziente e fisioterapista
        messaggi = self.controller.visualizza_messaggi(self.paziente_id, self.fisioterapista_id)

        for mittente_id, testo, timestamp in messaggi:
            # Usa il mittente_id per ottenere il nome corretto del mittente
            nome_mittente = self.controller.ottieni_nome_utente(mittente_id)

            # Inserisci il messaggio nella chat con il nome del mittente corretto
            self.chat_area.insert(tk.END, f"{nome_mittente} ({timestamp}): {testo}\n")

        self.chat_area.config(state='disabled')

        # Aggiorna la chat ogni 5 secondi
        self.root.after(5000, self.carica_messaggi)





        

    
            
            