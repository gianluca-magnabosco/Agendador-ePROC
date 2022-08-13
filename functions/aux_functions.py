import psycopg2
import os
import winshell
from win32com.client import Dispatch
from dotenv.main import load_dotenv

def connectDataBase():

    load_dotenv()

    con = psycopg2.connect(
                            dbname = "agendador",
                            user = "postgres",
                            password = os.environ["DATABASE_PASSWORD"],
                            host = "localhost"
                        )

    return con


def createDesktopShortcut():
    local_path = os.getcwd()
    desktop = winshell.desktop()
    shortcutPath = os.path.join(desktop, "Agendador ePROC.lnk")
    target = os.path.join(local_path, "Agendador ePROC.exe")
    iconPath = os.path.join(local_path, "img/icon.ico")

    if not os.path.exists(shortcutPath):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcutPath)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = local_path
        shortcut.IconLocation = iconPath
        shortcut.save()
