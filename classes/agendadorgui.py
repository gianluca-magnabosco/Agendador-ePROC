import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import CENTER
from functools import partial
import os
import re
from dotenv.main import load_dotenv

class AgendadorGUI():

    root = tk.Tk()

    def center_window(self, width, height, window):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))


    def on_closeroot(self):
        close = messagebox.askokcancel("Confirmação", "Tem certeza que deseja fechar o programa?")
        if close:
            self.root.destroy()


    def initGUI(self):
        iconFile = "img/icone.ico"
        self.center_window(860, 640, self.root)
        self.root.title("Agendador ePROC")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closeroot)
        self.root.iconbitmap(default = iconFile)
        self.root.resizable(0, 0)
        backgroundImage = tk.PhotoImage(file = "img/background.png")
        backgroundLabel = ttk.Label(self.root, image = backgroundImage)
        backgroundLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.initComponents()

        load_dotenv()

        try:
            self.login = os.environ["EPROC_LOGIN"]
            self.password = os.environ["EPROC_PASSWORD"]
        except:
            self.insert_login()
        else:
            if re.match("^[a-zA-Z]{2}\d{6}$", os.environ["EPROC_LOGIN"]):
                self.changeButtonState("enabled")
            else:
                self.insert_login()

        self.root.mainloop()


    def initComponents(self):
        self.initLabels()
        self.initButtons()


    def initLabels(self):
        self.welcomeLabel = tk.Label(text = "Seja bem-vindo!", wraplength = 200, font = ("", 15, "bold"), bg = "white")
        self.welcomeLabel.pack()
        self.welcomeLabel.place(relx = 0.5, rely = 0.52, anchor = CENTER)

        self.infoLabel = tk.Label(text = "Clique no botão abaixo para iniciar o programa e aguarde alguns instantes!", wraplength = 200, font = ("", 13), bg = "white")
        self.infoLabel.pack()
        self.infoLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        self.versionLabel = tk.Label(text = "Versão: 1.15.8", font = ("", 7), bg = "white")
        self.versionLabel.pack()
        self.versionLabel.place(relx = 0.05, rely = 0.98, anchor = CENTER)

        self.creditsLabel = tk.Label(text = "Programa criado por: Gianluca Notari Magnabosco da Silva", font = ("", 7), bg = "white")
        self.creditsLabel.pack()
        self.creditsLabel.place(relx = 0.84, rely = 0.98, anchor = CENTER)


    def closeLoginPopUp(self):
        self.loginPopUp.destroy()
        self.root.attributes("-topmost", True)


    def insert_login(self):
        self.loginPopUp = tk.Toplevel(self.root)

        self.loginPopUp.title("Login ePROC")
        self.loginPopUp.attributes("-topmost", True)
        self.loginPopUp.protocol("WM_DELETE_WINDOW", self.closeLoginPopUp)
        self.loginPopUp.resizable(0, 0)

        self.center_window(265, 135, self.loginPopUp)

        self.loginLabel = tk.Label(self.loginPopUp, text = "Insira seu login e senha do ePROC:", font = ("Arial", 9))
        self.loginLabel.place(relx = 0.50 , rely = 0.14, anchor = CENTER)

        self.usernameLabel = ttk.Label(self.loginPopUp, text = "Login: ")
        self.usernameLabel.place(relx = 0.21, rely = 0.37, anchor = CENTER)
        username = tk.StringVar()
        self.usernameEntry = ttk.Entry(self.loginPopUp, textvariable = username)
        self.usernameEntry.place(relx = 0.56, rely = 0.37, anchor = CENTER)

        self.passwordLabel = ttk.Label(self.loginPopUp, text = "Senha: ")
        self.passwordLabel.place(relx = 0.21, rely = 0.535, anchor = CENTER)
        password = tk.StringVar()
        self.passwordEntry = ttk.Entry(self.loginPopUp, textvariable = password, show = '*')
        self.passwordEntry.place(relx = 0.56, rely = 0.535, anchor = CENTER)

        validateLogin = partial(self.validateLogin, username, password)

        self.loginButton = ttk.Button(self.loginPopUp, text = "Login", command = validateLogin)
        self.loginButton.place(relx = 0.5, rely = 0.79, anchor = CENTER, width = 50) 
    
        def handler(e):
            validateLogin()

        self.loginPopUp.bind("<Return>", handler)


    def validateLogin(self, username, password):
        self.login = username.get()
        self.password = password.get()
 
        self.startButton.configure(state = "disabled")

        if not re.match("^[a-zA-Z]{2}\d{6}$", self.login) or len(self.password) < 4:
            self.loginPopUp.attributes("-topmost", False)
            tk.messagebox.showerror(title = "Atenção!", message = "Login inválido")
            self.loginPopUp.attributes("-topmost", True)
            self.startButton.configure(state = "disabled")

            return False

        self.startButton.configure(state = "enabled")

        try:
            aux = [os.environ["EPROC_LOGIN"], os.environ["EPROC_PASSWORD"]]
        except:
            with open(".env", "a") as file:
                file.write(f'\nEPROC_LOGIN = "{self.login}"')
                file.write(f'\nEPROC_PASSWORD = "{self.password}"')
        else:
            db_password = os.environ["DATABASE_PASSWORD"]
            with open(".env", "w") as file:
                file.write(f'DATABASE_PASSWORD = "{db_password}"')
                file.write(f'\nEPROC_LOGIN = "{self.login}"')
                file.write(f'\nEPROC_PASSWORD = "{self.password}"')

        self.closeLoginPopUp()                 

        return self.login, self.password
                

    def changeLoadingLabel(self):
        self.statusLabel = tk.Label(text = "Carregando... Aguarde", wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.statusLabel.pack()
        self.statusLabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.statusLabel.update_idletasks()


    def changeButtonState(self, state):
        try:
            self.startButton.update_idletasks()
            self.startButton.configure(state = f"{state}d")
            self.startButton.update_idletasks()
        except:
            pass


    def updateStatusLabel(self):
        self.statusLabel.destroy()
        self.statusLabel = tk.Label(text = "Concluído!", wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.statusLabel.pack()
        self.statusLabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.statusLabel.update_idletasks()

        
    def complete(self):
        self.updateStatusLabel()

        closeconfirmation = messagebox.showinfo("Sucesso!", "O programa foi executado com sucesso!")
        if closeconfirmation:
            self.showSuccessPopUp()

        self.changeButtonState("enable")


    def showSuccessPopUp(self):
        self.statusLabel.destroy()
        self.statusLabel.update_idletasks()
        self.showSuccessConfirmation()


    def showSuccessConfirmation(self):
        self.statusLabel = tk.Label(text = "As intimações foram importadas e se encontram no Banco de Dados!", wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.statusLabel.pack()
        self.statusLabel.place(relx = 0.5, rely = 0.71, anchor = CENTER)
        self.statusLabel.update_idletasks()
        infoBox = messagebox.showinfo("Informação", "As intimações foram inseridas no Banco de Dados com sucesso!")
        if infoBox:
            self.statusLabel.destroy()
            self.statusLabel.update_idletasks()
            closeConfirmation = messagebox.askyesno("Sair", "Deseja sair do programa?")
            if closeConfirmation:
                self.root.destroy()
