import datetime
from functions.aux_functions import connectDataBase
from notifypy import Notify


class WindowsNotifier():

    def __init__(self):
        self.eprocState = []
        self.processNumbers = []
        self.processParts = []
        self.activityDueDates = []


    def setWeeklyDueDates(self):

        dateToday = datetime.date.today()
        self.dateToday = dateToday.strftime("%Y-%m-%d")

        con = connectDataBase()
        cur = con.cursor()

        cur.execute(f"SELECT * FROM agendadoreproc WHERE data = '{self.dateToday}' ORDER BY num_processo DESC;")
        result = cur.fetchall()

        if not result:
            self.processNumbers.append("Nenhuma intimação pendente!")
            self.processParts.append("Nenhum prazo pendente para o dia de hoje")
            self.activityDueDates.append("")
            self.eprocState.append("")

            con.commit()
            cur.close()
            con.close()
            return

        for field in result:
            self.processNumbers.append(field[0])
            self.processParts.append(field[1])
            formattedDate = field[2].strftime("%d/%m/%Y")
            self.activityDueDates.append(f"Prazo: {formattedDate}")
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
            notification = Notify()
            notification.application_name = "Intimações Pendentes"
            notification.title = f"{self.processNumbers[i]}\n{self.activityDueDates[i]}"
            notification.message = f"{self.processParts[i]}\n{self.eprocState[i]}"

            if self.eprocState[i] == "(𝐞𝐩𝐫𝐨𝐜-𝐒𝐂)":
                notification.icon = "img/scNotificationIcon.ico"
            else:
                notification.icon = "img/prNotificationIcon.ico"

            notification.send()