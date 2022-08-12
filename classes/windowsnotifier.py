import datetime
from win10toast import ToastNotifier
from functions.aux_functions import connectDataBase


class WindowsNotifier():

    def __init__(self):
        self.eprocState = []
        self.processNumbers = []
        self.processParts = []
        self.activityDueDates = []
        self.toaster = ToastNotifier()


    def setWeeklyDueDates(self):

        dateToday = datetime.date.today()
        dateOneWeekFromNow = dateToday + datetime.timedelta(days = 7)
        self.dateToday = dateToday.strftime("%Y-%m-%d")
        self.dateOneWeekFromNow = dateOneWeekFromNow.strftime("%Y-%m-%d")

        con = connectDataBase()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM agendadoreproc WHERE data BETWEEN '{self.dateToday}' AND '{self.dateOneWeekFromNow}' ORDER BY data DESC, num_processo DESC;")
        result = cur.fetchall()

        for field in result:
            self.processNumbers.append(field[0])
            self.processParts.append(field[1])
            formattedDate = field[2].strftime("%d/%m/%Y")
            self.activityDueDates.append(formattedDate)
            if field[3] == "eproc-SC":
                self.eprocState.append("(𝐞𝐩𝐫𝐨𝐜-𝐒𝐂)")
            else:
                self.eprocState.append("(𝐞𝐩𝐫𝐨𝐜-𝐏𝐑)")
            
        con.commit()
        cur.close()
        con.close()
    

    def sendNotifications(self):
        
        self.setWeeklyDueDates()

        for i in range(len(self.processNumbers)):
            try:
                self.toaster.show_toast(f"Processo nº {self.processNumbers[i]}\nPrazo: {self.activityDueDates[i]}",
                                f"{self.processParts[i]}\n{self.eprocState[i]}",
                                icon_path = "img/icone.ico",
                                duration = None)
            except:
                pass
