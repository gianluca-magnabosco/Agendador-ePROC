import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import CENTER
from functools import partial
import re
from dotenv.main import load_dotenv
import sys
import os


class AgendadorGUI():

    root = None
    active = False
    loginFail = False

    def centerWindow(self, width, height, window):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))


    def onCloseRoot(self):
        self.root.destroy()
        self.active = False
        self.root = None
        
    
    def closeRootTray(self):
        close = messagebox.askokcancel("Confirmação", "Tem certeza que deseja fechar o programa?")
        if close:
            if self.root is not None:
                self.root.destroy()
            self.trayIcon.stop()
            sys.exit()


    def initGUI(self, error = False):
        if self.root is not None and self.active is True:
            self.root.destroy()
            self.active = False
            self.root = None
            return

        self.root = tk.Tk()
        self.active = True

        iconFile = "img/icon.ico"
        self.centerWindow(860, 640, self.root)
        self.root.title("Agendador ePROC")
        if error is True:
            self.root.attributes("-topmost", True)
            
        self.root.protocol("WM_DELETE_WINDOW", self.onCloseRoot)
        self.root.iconbitmap(default = iconFile)
        self.root.resizable(False, False)
        backgroundImage = tk.PhotoImage(file = "img/background.png")
        backgroundLabel = ttk.Label(self.root, image = backgroundImage)
        backgroundLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
        self.initComponents()

        try:
            with open(".env", "r") as file:
                file.readline()
                self.login = file.readline()[15:-2]
                self.password = file.readline()[18:-1]
                if len(self.login) < 6 or len(self.password) < 4:
                    raise Exception
        except:
            if self.loginFail is True:
                self.loginFail = False
                confirm = messagebox.showerror(title = "Erro no login", message = "Login ou senha do ePROC incorretos!")
                if confirm:
                    self.insert_login()
            else:
                self.insert_login()
        else:
            if re.match("^[a-zA-Z]{2}\d{6}$", self.login):
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


    def changeButtonState(self, state):
        try:
            self.startButton.update_idletasks()
            self.startButton.configure(state = f"{state}d")
            self.startButton.update_idletasks()
        except:
            pass


    def updateStatusLabel(self, text, destroy = False):
        if destroy is True:
            self.statusLabel.destroy()

        self.statusLabel = tk.Label(text = text, wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.statusLabel.pack()
        self.statusLabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.statusLabel.update_idletasks()


    def closeLoginPopUp(self):
        self.loginPopUp.destroy()
        self.root.attributes("-topmost", True)


    def togglePassword(self):
        if self.passwordEntry.cget("show") == '*':
            self.passwordEntry.config(show = '')
        else:
            self.passwordEntry.config(show = '*')


    def insert_login(self):
        load_dotenv()
        self.loginPopUp = tk.Toplevel(self.root)

        self.loginPopUp.title("Login ePROC")
        self.loginPopUp.attributes("-topmost", True)
        self.loginPopUp.protocol("WM_DELETE_WINDOW", self.closeLoginPopUp)
        self.loginPopUp.resizable(False, False)

        self.centerWindow(265, 135, self.loginPopUp)

        self.loginLabel = tk.Label(self.loginPopUp, text = "Insira seu login e senha do ePROC:", font = ("Arial", 9))
        self.loginLabel.place(relx = 0.50 , rely = 0.14, anchor = CENTER)

        self.usernameLabel = ttk.Label(self.loginPopUp, text = "Login: ")
        self.usernameLabel.place(relx = 0.21, rely = 0.37, anchor = CENTER)
        self.usernameVariable = tk.StringVar()
        self.usernameEntry = ttk.Entry(self.loginPopUp, textvariable = self.usernameVariable)
        self.usernameEntry.place(relx = 0.56, rely = 0.37, anchor = CENTER)


        self.passwordLabel = ttk.Label(self.loginPopUp, text = "Senha: ")
        self.passwordLabel.place(relx = 0.21, rely = 0.535, anchor = CENTER)
        self.passwordVariable = tk.StringVar()
        self.passwordEntry = ttk.Entry(self.loginPopUp, textvariable = self.passwordVariable, show = '*')
        self.passwordEntry.place(relx = 0.56, rely = 0.535, anchor = CENTER)

        validateLogin = partial(self.validateLogin, self.usernameVariable, self.passwordVariable)

        self.revealPasswordCheckBox = tk.Checkbutton(self.loginPopUp, command = self.togglePassword, variable = self.passwordEntry)
        self.revealPasswordCheckBox.place(relx = 0.9, rely = 0.535, anchor = CENTER)

        self.revealPasswordLabel = ttk.Label(self.loginPopUp, text = "Mostrar")
        self.revealPasswordLabel.place(relx = 0.9, rely = 0.65, anchor = CENTER)


        self.loginButton = ttk.Button(self.loginPopUp, text = "Login", command = validateLogin)
        self.loginButton.place(relx = 0.5, rely = 0.79, anchor = CENTER, width = 50)

    
        try:
            with open(".env", "r") as file:
                file.readline()
                currentUsername = file.readline()[15:-2]
                currentPassword = file.readline()[18:-1]
        except:
            pass
        else:
            self.usernameEntry.insert(0, currentUsername)
            self.passwordEntry.insert(0, currentPassword)

        def handler(e):
            validateLogin()

        self.loginPopUp.bind("<Return>", handler)


    def regexMatchUserInfo(self):
        if not re.match("^[a-zA-Z]{2}\d{6}$", self.login) or len(self.password) < 4:
            self.loginPopUp.attributes("-topmost", False)
            messagebox.showerror(title = "Atenção!", message = "Login inválido")
            self.loginPopUp.attributes("-topmost", True)
            
            return False

        return True
        

    def validateLogin(self, username, password):
        self.login = username.get()
        self.password = password.get()
        load_dotenv()
 
        try:
            aux = [os.environ["EPROC_LOGIN"], os.environ["EPROC_PASSWORD"]]
        except:
            self.startButton.configure(state = "disabled")
        else:
            if not self.regexMatchUserInfo():
                self.login = os.environ["EPROC_LOGIN"]
                self.password = os.environ["EPROC_PASSWORD"]
                self.startButton.configure(state = "enabled")
                self.closeLoginPopUp()

                return self.login, self.password

        if not self.regexMatchUserInfo():
            return False
        
        try:
            aux = [os.environ["EPROC_LOGIN"], os.environ["EPROC_PASSWORD"]]
        except:
            with open(".env", "a") as file:
                file.write(f'\nEPROC_LOGIN = "{self.login}"')
                file.write(f'\nEPROC_PASSWORD = "{self.password}"')
                file.close()
        else:
            db_password = os.environ["DATABASE_PASSWORD"]
            with open(".env", "w") as file:
                file.write(f'DATABASE_PASSWORD = "{db_password}"')
                file.write(f'\nEPROC_LOGIN = "{self.login}"')
                file.write(f'\nEPROC_PASSWORD = "{self.password}"')
                file.close()


        with open(".env", "r") as file:
            file.readline()
            self.login = file.readline()[15:-2]
            self.password = file.readline()[18:-1]

        self.startButton.configure(state = "enabled")
        self.closeLoginPopUp()

        return self.login, self.password
                
    
    def complete(self, error = False):
        if error is True:
            self.statusLabel.destroy()
            self.statusLabel.update_idletasks()
            self.changeButtonState("enable")
            self.root.update()
            return

        self.root.update()
        self.updateStatusLabel("Concluído!", destroy = True)

        closeconfirmation = messagebox.showinfo("Sucesso!", "O programa foi executado com sucesso!")
        if closeconfirmation:
            self.showSuccessPopUp()

        self.changeButtonState("enable")


    def showSuccessPopUp(self):
        self.statusLabel.destroy()
        self.statusLabel.update_idletasks()
        self.showSuccessConfirmation()


    def showSuccessConfirmation(self):
        self.updateStatusLabel("As notificações foram enviadas para a barra lateral do Windows!")
        infoBox = messagebox.showinfo("Informação", "As notificações foram enviadas com sucesso!")
        if infoBox:
            self.statusLabel.destroy()
            self.statusLabel.update_idletasks()
            closeConfirmation = messagebox.askyesno("Minimizar", "Deseja minimizar o programa?")
            if closeConfirmation:
                self.root.destroy()
                self.root = None
                self.active = False
