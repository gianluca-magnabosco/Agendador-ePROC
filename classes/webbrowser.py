from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os


class WebBrowser():

    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd
        self.thread = True


    def startBrowser(self):
        localPath = os.getcwd()

        preferences = {"download.default_directory": localPath, "directory_upgrade": True}
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("prefs", preferences)                   

        driverPath = "/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = localPath + driverPath, options = options)
        self.driver.implicitly_wait(60)
        self.driver.get("https://eproc1g.tjsc.jus.br/eproc/externo_controlador.php?acao=principal")

        self.eprocLogin()

        folderFilesCount = len(os.listdir(localPath))

        self.downloadFile("tr0")
        self.goBack()
        self.downloadFile("tr1")

        
        while len(os.listdir(localPath)) != folderFilesCount + 2:
            time.sleep(1)

        self.thread = False
        self.driver.quit()


    def getElement(self, element_type, element):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((element_type, element)))


    def eprocLogin(self):
        loginField = self.getElement(By.ID, "txtUsuario")
        loginField.send_keys(self.login)

        passwordField = self.getElement(By.ID, "pwdSenha")
        passwordField.send_keys(self.passwd)

        loginButton = self.getElement(By.ID, "sbmEntrar")
        loginButton.click()


    def goBack(self):
        oldURl = self.driver.window_handles[0]
        self.driver.switch_to.window(oldURl)
        self.driver.back()
    

    def downloadFile(self, element):
        
        eprocStateButton = self.getElement(By.ID, element)
        eprocStateButton.click()

        intimacoesButton = self.getElement(By.XPATH, '//*[@id="conteudoCitacoesIntimacoesSC"]/div[2]/table/tbody/tr[1]/td[2]/a')
        intimacoesButton.click()

        newURl = self.driver.window_handles[1]
        self.driver.switch_to.window(newURl)

        downloadButton = self.getElement(By.ID, "sbmPlanilha")
        downloadButton.click()
