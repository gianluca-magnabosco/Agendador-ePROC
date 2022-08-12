from tkinter import ttk
from tkinter.constants import CENTER
from functions.aux_functions import createDesktopShortcut
from classes.webbrowser import WebBrowser
from classes.eprocfiles import EprocFiles
from classes.agendadorgui import AgendadorGUI
from classes.windowsnotifier import WindowsNotifier


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


def getProcessesData():
    EprocFiles.resetFilesAndTables()

    browser = WebBrowser(programGUI.login, programGUI.password)
    browser.startBrowser()

    scFile = EprocFiles("sc")
    scFile.initFile()

    prFile = EprocFiles("pr")
    prFile.initFile()

    notifier = WindowsNotifier()
    notifier.sendNotifications()


 
def start():
    programGUI.changeLoadingLabel()
    programGUI.changeButtonState("disable")

    getProcessesData()

    programGUI.complete()


def main():
    global programGUI

    createDesktopShortcut()
    programGUI = ChildGUI()
    programGUI.initGUI()


if __name__ == "__main__":
    main()



#
#
#
# python -m PyInstaller --onedir --windowed --icon=icone.ico --name="Agendador ePROC" -F --add-data "Winico;winico" agendador.py
#
#
#