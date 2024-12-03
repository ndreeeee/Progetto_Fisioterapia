import tkinter as tkk
from views.login_view import LoginView




def main():
    root = tkk.Tk()
    root.geometry("900x700")
    LoginView(root)
    root.mainloop()

    

if __name__ == "__main__":
    main()