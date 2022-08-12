from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os


class WebBrowser():

    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd


    def startBrowser(self):
        localPath = os.getcwd()

        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        preferences = {"download.default_directory": localPath, "directory_upgrade": True}
        options.add_experimental_option("prefs", preferences)                   

        driverPath = "/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = localPath + driverPath, options = options)
        self.driver.implicitly_wait(15)
        self.driver.get("https://eproc1g.tjsc.jus.br/eproc/externo_controlador.php?acao=principal")

        self.eprocLogin()

        self.downloadFile("tr0")
        self.goBack()
        self.downloadFile("tr1")

        time.sleep(3)

        self.driver.quit()


    def eprocLogin(self):
        loginField = self.driver.find_element(By.XPATH, '//*[@id="txtUsuario"]')
        loginField.send_keys(self.login)

        passwordField = self.driver.find_element(By.XPATH, '//*[@id="pwdSenha"]')
        passwordField.send_keys(self.passwd)

        loginButton = self.driver.find_element(By.XPATH, '//*[@id="sbmEntrar"]')
        loginButton.click()


    def goBack(self):
        oldURl = self.driver.window_handles[0]
        self.driver.switch_to.window(oldURl)
        self.driver.back()
        time.sleep(1)
    

    def downloadFile(self, element):
        
        eprocStateButton = self.driver.find_element(By.XPATH, f'//*[@id="{element}"]')
        eprocStateButton.click()

        intimacoesButton = self.driver.find_element(By.XPATH, '//*[@id="conteudoCitacoesIntimacoesSC"]/div[2]/table/tbody/tr[1]/td[2]/a')
        intimacoesButton.click()

        newURl = self.driver.window_handles[1]
        self.driver.switch_to.window(newURl)

        downloadButton = self.driver.find_element(By.ID, "sbmPlanilha")
        downloadButton.click()
        time.sleep(2)
