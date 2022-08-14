from tkinter import ttk
from tkinter.constants import CENTER
from functions.aux_functions import createDesktopShortcut
from classes.webbrowser import WebBrowser
from classes.eprocfiles import EprocFiles
from classes.agendadorgui import AgendadorGUI
from classes.windowsnotifier import WindowsNotifier
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
from dotenv.main import load_dotenv
from threading import Thread
import time
import os


class ChildGUI(AgendadorGUI):

    def initButtons(self):
        self.buttonStyle = ttk.Style()
        self.buttonStyle.configure("W.TButton", background = "white", foreground = "black", font = ("Open Sans", 11))
        
        self.rootLoginButton = ttk.Button(self.root, style = "W.TButton", text = "  Login\nePROC", command = self.insert_login, width = 50.75)
        self.rootLoginButton.pack()
        self.rootLoginButton.place(relx = 0.23, rely = 0.72, anchor = CENTER)

        self.startButton = ttk.Button(self.root, style = "W.TButton", text = "Clique aqui para iniciar o programa", command = start, width = 27.75)
        self.startButton.pack()
        self.startButton.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        self.startButton.configure(state = "disabled")


    def addToSystemTray(self):
        self.iconImage = Image.open("img/icon.ico")

        self.trayMenu = menu(
                                item("Abrir", self.initGUI, default = True),
                                item("Enviar notificações", getProcessesData),
                                item("Fechar programa", self.closeRootTray)
                            )

        self.trayIcon = icon("Agendador ePROC", icon = self.iconImage, menu = self.trayMenu, title = "Agendador ePROC")
        self.trayIcon.run()



def getProcessesData():
    global browser
    EprocFiles.resetFilesAndTables()

    if len(programGUI.login) < 6 or len(programGUI.password) < 4:
        programGUI.initGUI()
        return

    try:
        browser = WebBrowser(programGUI.login, programGUI.password)
    except:
        programGUI.initGUI()
        return

    Thread(target = browser.startBrowser(), daemon = True).start()

    while browser.thread is True:
        time.sleep(1)
    
    if browser.loginFail is True:
        programGUI.loginFail = True
        programGUI.initGUI()
        return

    if browser.error is True:
        if programGUI.active is False:
            programGUI.initGUI(error = True)
        return

    if programGUI.active is True:
        programGUI.root.update()

    scFile = EprocFiles("sc")
    scFile.initFile()

    prFile = EprocFiles("pr")
    prFile.initFile()

    if programGUI.active is True:
        programGUI.updateStatusLabel("Enviando notificações...", destroy = True)

    notifier = WindowsNotifier()
    notifier.sendNotifications()


def start():
    programGUI.updateStatusLabel("Carregando... Aguarde")
    programGUI.changeButtonState("disable")

    getProcessesData()
    
    programGUI.complete(error = browser.error)


 
def main():
    global programGUI

    load_dotenv()

    createDesktopShortcut()

    programGUI = ChildGUI()
    try:
        programGUI.login = os.environ["EPROC_LOGIN"]
        programGUI.password = os.environ["EPROC_PASSWORD"]
    except:
        programGUI.initGUI()
    else:
        getProcessesData()
        
    programGUI.addToSystemTray()




if __name__ == "__main__":
    main()



#
#
#
# python3 -m PyInstaller --noconsole --onedir --icon=img/icon.ico --name="Agendador ePROC" agendador.py
#
#
#