import tkinter as tk
import tkinter.ttk as ttk

from database import Database
    
class ModificaPaziente:
    def __init__(self, root, paziente, fisioterapista):
        self.root = root
        self.paziente = paziente
        self.fisioterapista = fisioterapista
        
        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modifica Paziente")

        modify_frame = ttk.Frame(modify_window, width=900, height=700)
        modify_frame.pack_propagate(False)
        modify_frame.pack(pady=20, padx=20)  

        db = Database()

        ttk.Label(modify_frame, text="Nome Paziente", font=("Arial", 16)).pack(pady=5)
        nome_entry = ttk.Entry(modify_frame, font=("Arial", 14), width=70)
        nome_entry.insert(0, self.paziente.nome) 
        nome_entry.pack(pady=10)

        ttk.Label(modify_frame, text="Email Paziente", font=("Arial", 16)).pack(pady=5)
        email_entry = ttk.Entry(modify_frame, font=("Arial", 14), width=70)
        email_entry.insert(0, self.paziente.email) 
        email_entry.pack(pady=10)

        ttk.Label(modify_frame, text="Password Paziente", font=("Arial", 16)).pack(pady=5)
        password_entry = ttk.Entry(modify_frame, show="*", font=("Arial", 14), width=70)  
        password_entry.pack(pady=10)

       
        submit_button = ttk.Button(modify_frame, text="Salva Modifiche", 
                                command=lambda: (db.modifica_paziente(self.paziente, nome_entry.get(), email_entry.get(), password_entry.get()), 
                                                 self.fisioterapista.modifica_paziente(nome_entry.get(), email_entry.get(), password_entry.get(), modify_window, self.paziente)),
                                style="TButton")
        submit_button.pack(pady=15, ipadx=10, ipady=5)

      
        back_button = ttk.Button(modify_frame, text="Torna Indietro", command=modify_window.destroy, style="TButton")
        back_button.pack(pady=10, ipadx=10, ipady=5)
        
   