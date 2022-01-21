import time

import null as null
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Connections:

    URL = "http://wos.fecyt.es"
    URL_Deusto = ""
    driver = null

    def driverCreator(self):

        op = webdriver.ChromeOptions()
        # op.add_argument('--headless')
        op.add_argument('--start-maximized')
        op.add_argument('--disable-extensions')

        self.driver = webdriver.Chrome("C:\\Users\\eraun\\OneDrive\\Escritorio\\chromedriver.exe", options=op)

    def loginWebOfScience(self, username, password, user_tipology):

        data = requests.get(self.URL)

        soup = BeautifulSoup(data.content, 'html.parser')
        e = soup.find_all("option")
        for i in e:
            if "Universidad de Deusto" in i.text:
                self.URL_Deusto = i.get('value')

        self.driver.get(self.URL_Deusto)
        self.driver.find_element(By.NAME, 'username').send_keys(username)

        self. driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[4]/select').click()
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[4]/select/option[1]').click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'regularsubmit').click()

        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/p[1]/b')))
            return 1
        except TimeoutException:
            print("todo correcto")
            return 0

    def dataSearch(self, topic):

        self.driver.get(self.URL)

        WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'.replace(' ', '.')))).click()

        self.driver.find_element(By.NAME, 'search-main-box').send_keys(topic)

        # select the data base of source
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="snSelectDb"]/button'.replace(' ', '.')))).click()
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="snSelectDb"]/button/span[1]'.replace(' ', '.')))).click()

        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="snSearchType"]/div[3]/button[2]'.replace(' ', '.')))).click()

        number_of_results = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, "/html/body/app-wos/div/div/main/div/div[2]/app-input-route/app-base-summary-component/app-search-friendly-display/div[1]/app-general-search-friendly-display/h1/span"))).get_attribute("innerHTML")

        number_of_results = number_of_results.replace(",", "")
        number_of_results_rounded = int(int(number_of_results)/1000)

        for i in range(0, number_of_results_rounded+1):
            #  export data file
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="snRecListTop"]/app-export-menu/div/button'.replace(' ', '.')))).click()

            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="exportToExcelButton"]'.replace(' ', '.')))).click()

            time.sleep(2)

            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, '//*[@id="radio3-input"]'))

            # insercion de valor de limite inferior
            self.driver.execute_script("arguments[0].value='';",
                                       self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]'))

            limite_inferior = int(1 + (1000 * i))
            self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(limite_inferior)

            # insercion de valor de limite superior
            self.driver.execute_script("arguments[0].value='';",
                                       self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]'))

            limite_superior = 1000 * (1+i)
            self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(limite_superior)

            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '/html/body/app-wos/div/div/main/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[2]/button[1]'.replace(' ', '.')))).click()
