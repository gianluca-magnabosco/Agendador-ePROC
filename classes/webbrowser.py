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
        local_path = os.getcwd()

        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        preferences = {"download.default_directory": local_path, "directory_upgrade": True}
        options.add_experimental_option("prefs", preferences)                   

        driverpath = "/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = local_path + driverpath, options = options)
        self.driver.implicitly_wait(15)
        self.driver.get("https://eproc1g.tjsc.jus.br/eproc/externo_controlador.php?acao=principal")

        self.eprocLogin()

        self.downloadFiles("tr0")
        self.goBack()
        self.downloadFiles("tr1")

        time.sleep(3)

        self.driver.quit()


    def eprocLogin(self):
        loginxpath = self.driver.find_element(By.XPATH, '//*[@id="txtUsuario"]')
        loginxpath.send_keys(self.login)

        passwxpath = self.driver.find_element(By.XPATH, '//*[@id="pwdSenha"]')
        passwxpath.send_keys(self.passwd)

        loginbuttonxpath = self.driver.find_element(By.XPATH, '//*[@id="sbmEntrar"]')
        loginbuttonxpath.click()


    def goBack(self):
        oldURl = self.driver.window_handles[0]
        self.driver.switch_to.window(oldURl)
        self.driver.back()
        time.sleep(1)
    

    def downloadFiles(self, element):
        
        buttonxpath = self.driver.find_element(By.XPATH, f'//*[@id="{element}"]')
        buttonxpath.click()

        intimacoesxpath = self.driver.find_element(By.XPATH, '//*[@id="conteudoCitacoesIntimacoesSC"]/div[2]/table/tbody/tr[1]/td[2]/a')
        intimacoesxpath.click()

        newURl = self.driver.window_handles[1]
        self.driver.switch_to.window(newURl)

        gerarplanilhaid = self.driver.find_element(By.ID, "sbmPlanilha")
        gerarplanilhaid.click()
        time.sleep(2)
