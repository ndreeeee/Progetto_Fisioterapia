import tkinter as tk
from tkinter import scrolledtext
from model.messaggio import Messaggio
from tkinter import font
import tkinter.ttk as ttk







class MessaggiView:
    
    
    def __init__(self, root, paziente, fisioterapista, flag):
        self.root = root
        self.paziente = paziente
        self.fisioterapista = fisioterapista
        self.flag = flag

        self.titolo_font = font.Font(family="Arial", size=20, weight="bold")
        self.messaggio_font = font.Font(family="Arial", size=12)
        
        button_font = ("Arial", 14, "bold")  
     
     

        self.main_frame = tk.Frame(self.root, width=900, height=700, bg="#f0f0f0")
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Chat", font=self.titolo_font, bg="#f0f0f0")
        self.label.pack(pady=10)

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

        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

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

        self.carica_messaggi(self.fisioterapista, self.paziente)

    
    def invia_messaggio(self, flag):
        try:
            testo = self.input_text.get().strip()
            if not testo:
                print("Nessun testo inserito.")
                return
            
            if flag == 1:
                self.fisioterapista.invia_messaggio(self.fisioterapista, self.paziente, testo)
            else:
                self.paziente.invia_messaggio(self.paziente, self.fisioterapista, testo)
                
            self.input_text.delete(0, tk.END)  # Pulisce l'area di input dopo l'invio

            print("Messaggio inviato. Ricarico i messaggi...")
            self.carica_messaggi(self.fisioterapista, self.paziente)  # Aggiorna la chat
        except Exception as e:
            print(f"Errore durante l'invio del messaggio: {e}")


    def carica_messaggi(self, fisioterapista, paziente):
        from model.fisioterapista import Fisioterapista
        from model.paziente import Paziente
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)

        db = Database()
        messaggi = db.ottieni_messaggi(fisioterapista, paziente)

        for messaggio in messaggi:
            
            if isinstance(messaggio.mittente, Fisioterapista):
                self.chat_area.insert(tk.END, f"{fisioterapista.nome} ({messaggio.data_invio}): {messaggio.descrizione}\n")
            if isinstance(messaggio.mittente, Paziente):
                self.chat_area.insert(tk.END, f"{paziente.nome} ({messaggio.data_invio}): {messaggio.descrizione}\n")

        self.chat_area.config(state='disabled')

        self.root.after(5000, lambda: self.carica_messaggi(self.fisioterapista, self.paziente))





        

    
            
            