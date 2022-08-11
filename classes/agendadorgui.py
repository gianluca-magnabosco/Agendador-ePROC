import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import CENTER
from functools import partial
import time

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


    def on_close_login(self):
        self.loginPopUp.destroy()
        self.root.attributes("-topmost", True)


    def initGUI(self):
        iconFile = "img/icone.ico"
        self.center_window(860, 640, self.root)
        self.root.title("Agendador ePROC")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closeroot)
        self.root.iconbitmap(default = iconFile)
        background_image = tk.PhotoImage(file = "img/background.png")
        background_label = ttk.Label(self.root, image = background_image)
        background_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.initComponents()
        self.insert_login()

        self.root.mainloop()


    def initComponents(self):
        self.initLabels()
        self.initButtons()


    def initLabels(self):
        status = tk.Label(text = "Seja bem-vindo!", wraplength = 200, font = ("", 15 ,"bold"), bg = "white")
        status.pack()
        status.place(relx = 0.5, rely = 0.52, anchor = CENTER)

        info = tk.Label(text = "Clique no botão abaixo para iniciar o programa e aguarde alguns instantes!", wraplength = 200, font = ("", 13), bg = "white")
        info.pack()
        info.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        version = tk.Label(text = "Versão: 1.15.8", font = ("", 7), bg = "white")
        version.pack()
        version.place(relx = 0.05, rely = 0.98, anchor = CENTER)

        feitopor = tk.Label(text = "Programa criado por: Gianluca Notari Magnabosco da Silva", font = ("", 7), bg = "white")
        feitopor.pack()
        feitopor.place(relx = 0.84, rely = 0.98, anchor = CENTER)


    def validateLogin(self, username, password):
        self.login = username.get()
        self.passwd = password.get()
        self.root.attributes("-topmost", True) 

        self.loginPopUp.destroy()
        self.button1.configure(state = "disabled")

        if self.login > "1" and self.passwd > "1":
            self.button1.configure(state = "enabled")
        else:
            self.button1.configure(state = "disabled")

        return self.login, self.passwd


    def insert_login(self):
            
        self.loginPopUp = tk.Toplevel(self.root)

        self.loginPopUp.title("Login ePROC")
        self.loginPopUp.attributes("-topmost", True)
        self.loginPopUp.protocol("WM_DELETE_WINDOW", self.on_close_login)
        self.center_window(240, 135, self.loginPopUp)

        tk.Label(self.loginPopUp, text = "Insira seu login e senha do ePROC:", font = ("Arial", 9)).place(relx = 0.50 , rely = 0.14, anchor = CENTER)

        usernameLabel = ttk.Label(self.loginPopUp, text = "Login: ")
        usernameLabel.place(relx = 0.21, rely = 0.37, anchor = CENTER)
        username = tk.StringVar()
        usernameEntry = ttk.Entry(self.loginPopUp, textvariable = username)
        usernameEntry.place(relx = 0.56, rely = 0.37, anchor = CENTER)

        passwordLabel = ttk.Label(self.loginPopUp, text = "Senha: ")
        passwordLabel.place(relx = 0.21, rely = 0.535, anchor = CENTER)
        password = tk.StringVar()
        passwordEntry = ttk.Entry(self.loginPopUp, textvariable = password, show = '*')
        passwordEntry.place(relx = 0.56, rely = 0.535, anchor = CENTER)

        validateLogin = partial(self.validateLogin, username, password)


        loginButton = ttk.Button(self.loginPopUp, text = "Login", command = validateLogin)
        loginButton.place(relx = 0.5, rely = 0.79, anchor = CENTER, width = 50) 
    
        def handler(e):
            validateLogin()

        self.loginPopUp.bind("<Return>", handler)

                

    def changeLoadingLabel(self):
        self.status = tk.Label(text = "Carregando... Aguarde" , wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.status.pack()
        self.status.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.status.update_idletasks()


    def changeButtonState(self, state):
        self.button1.update_idletasks()
        self.button1.configure(state = f"{state}d")
        self.button1.update_idletasks()
        time.sleep(1)


    def updateStatusLabel(self):
        self.status1 = tk.Label(text = "Concluído!", wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.status1.pack()
        self.status1.place(relx = 0.5, rely = 0.7, anchor = CENTER)


    def showSuccessPopUp(self):
        self.status1.destroy()
        self.on_closetop()


    def on_closetop(self):
        self.status2 = tk.Label(text = "As intimações foram importadas e se encontram no Google Agenda!", wraplength = 200, font = ("", 9, "bold"), bg = "white")
        self.status2.pack()
        self.status2.place(relx = 0.5, rely = 0.71, anchor = CENTER)
        self.status2.update_idletasks()
        close = messagebox.showinfo("Informação", "As intimações foram adicionadas no Google Agenda com sucesso!")
        if close:
            close2 = messagebox.askyesno("Sair","Deseja sair do programa?")
            if close2:
                self.root.destroy()
            else:
                self.status2.destroy()
                self.status2.update_idletasks()

        
    def complete(self):
        self.status.destroy()
        self.updateStatusLabel()

        closeconfirmation = messagebox.showinfo("Sucesso!", "O programa foi executado com sucesso!")
        if closeconfirmation:
            self.showSuccessPopUp()

        self.changeButtonState("enable")
