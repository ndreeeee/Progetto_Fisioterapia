import tkinter as tkk
from views.login_view import LoginView




def main():
    
    from database import Database
    db = Database()
    lista_utenti = db.carica_utenti()
    root = tkk.Tk()
    root.geometry("900x700")
    LoginView(root, lista_utenti)
    root.mainloop()

if __name__ == "__main__":
    main()