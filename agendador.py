from tkinter import ttk
from tkinter.constants import CENTER
from functions.aux_functions import createDesktopShortcut
from classes.webbrowser import WebBrowser
from classes.eprocfiles import EprocFiles
from classes.agendadorgui import AgendadorGUI


class ChildGUI(AgendadorGUI):

    def initButtons(self):
        st = ttk.Style()
        st.configure("W.TButton", background = "white", foreground = "black", font = ("Open Sans", 11))
        button_login = ttk.Button(self.root, style = "W.TButton", text = "  Login\nePROC", command = self.insert_login, width = 50.75)
        button_login.pack()
        button_login.place(relx = 0.23, rely = 0.72, anchor = CENTER)

        st = ttk.Style()
        st.configure("W.TButton", background = "white", foreground = "black", font = ("Open Sans", 11))
        self.button1 = ttk.Button(self.root, style = "W.TButton", text = "Clique aqui para iniciar o programa", command = runcode, width = 27.75)
        self.button1.pack()
        self.button1.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        self.button1.configure(state = "disabled")


def runcode():
    programGUI.changeLoadingLabel()
    programGUI.changeButtonState("disable")

    EprocFiles.resetFilesAndTables()

    browser = WebBrowser(programGUI.login, programGUI.passwd)
    browser.startBrowser()

    scFile = EprocFiles("sc")
    scFile.initFile()

    prFile = EprocFiles("pr")
    prFile.initFile()

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
# python -m PyInstaller --onedir --windowed --icon=icone.ico --name="Agendador ePROC" agendador.py
#
#
#