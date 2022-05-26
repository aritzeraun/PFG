import time

import null as null
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from fake_useragent import UserAgent


class Connections:
    URL = "http://wos.fecyt.es"
    URL_Deusto = ""
    driver = null

    def driverCreator(self):

        ROOT_DIR = os.path.abspath(os.curdir)
        ua = UserAgent()
        userAgent = ua.random
        ROOT_DIR = ROOT_DIR + '\Downloads'
        op = webdriver.ChromeOptions()
        op.add_argument('--headless')
        op.add_argument(f'user-agent={userAgent}')
        op.add_argument('--start-maximized')
        op.add_argument('--disable-extensions')
        op.add_argument("--window-size=1920,1080")
        op.add_argument('--ignore-certificate-errors')
        op.add_argument('--allow-running-insecure-content')
        prefs = {'download.default_directory': ROOT_DIR}
        op.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome("./Driver/chromedriver.exe", options=op)

    def loginWebOfScience(self, username, password, user_typology):
        data = requests.get(self.URL)

        soup = BeautifulSoup(data.content, 'html.parser')
        e = soup.find_all("option")
        for i in e:
            if "Universidad de Deusto" in i.text:
                self.URL_Deusto = i.get('value')
        self.driver.get(self.URL_Deusto)
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[4]/select').click()
        user = str(user_typology)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[4]/select/option[!]'
                                 .replace("!", user)).click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'regularsubmit').click()

        try:
            WebDriverWait(self.driver, 3).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="content"]/div/p[1]/b')))
            self.driver.close()
            return False
        except TimeoutException:
            return True

    def dataSearch(self, topic, search_error):

        if not search_error:
            try:
                WebDriverWait(self.driver, 5).until(
                    ec.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()
            except Exception:
                print("")

            self.driver.get(self.URL)
        try:
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'.replace(' ', '.')))).click()
        except TimeoutException:
            print("")

        self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(topic)

        try:
            WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="mat-dialog-0"]/div/div/div[3]/div/button'))).click()
        except Exception:
            print("")

        # select the data base of source
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="snSelectDb"]/button'.replace(' ', '.')))).click()
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="snSelectDb"]/button/span[1]'.replace(' ', '.')))).click()

        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="snSearchType"]/div[3]/button[2]'.replace(' ', '.')))).click()
        except Exception:
            self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)

        try:
            WebDriverWait(self.driver, 8).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="snSearchType"]/div[1]/b')))
            WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="snSearchType"]/div[4]/button[1]'))).click()
            return False
        except TimeoutException:

            number_of_results = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH,
                                                  "/html/body/app-wos/div/div/main/div/div[2]/app-input-route/app-base-summary-component/app-search-friendly-display/div[1]/app-general-search-friendly-display/h1/span"))).get_attribute(
                "innerHTML")

            number_of_results = number_of_results.replace(",", "")
            number_of_results_rounded = int(int(number_of_results) / 1000)

            # array that contents downloaded files name
            filesName = []

        for i in range(0, number_of_results_rounded + 1):

            # Gets image of the situation with headless
            # self.driver.get_screenshot_as_file('./Downloads/ej.png')

            #  export data file
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="snRecListTop"]/app-export-menu/div/button'.replace(' ', '.')))).click()

            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="exportToExcelButton"]'.replace(' ', '.')))).click()

            time.sleep(2)

            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, '//*[@id="radio3-input"]'))

            # insercion de valor de limite inferior

            position = 1 + (i * 2)
            position = str(position)

            self.driver.execute_script("arguments[0].value='';",
                                       self.driver.find_element(By.XPATH,
                                                                '//*[@id="mat-input-!"]'.replace('!', position)))

            limite_inferior = int(1 + (1000 * i))
            self.driver.find_element(By.XPATH, '//*[@id="mat-input-!"]'.replace("!", position)).send_keys(
                limite_inferior)

            # insercion de valor de limite superior

            position = 2 + i * 2
            position = str(position)

            self.driver.execute_script("arguments[0].value='';",
                                       self.driver.find_element(By.XPATH,
                                                                '//*[@id="mat-input-!"]'.replace("!", position)))

            if not i == number_of_results_rounded:
                limite_superior = int(1000 * (1 + i))
            else:
                limite_superior = number_of_results

            self.driver.find_element(By.XPATH, '//*[@id="mat-input-!"]'.replace("!", position)).send_keys(limite_superior)

            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//html/body/app-wos/div/div/main/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/div[2]/button[1]'.replace(' ', '.')))).click()

            time.sleep(5)

            # fileName = self.getDownLoadedFileName()
            # filesName.append(fileName)

        self.driver.close()
        # return filesName

    # method to get the downloaded file name
    def getDownLoadedFileName(self):

        self.driver.execute_script("window.open()")

        # switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # navigate to chrome downloads
        oldDriver = self.driver
        self.driver.get('chrome://downloads')
        # define the endTime
        endTime = time.time() + 10
        while True:
            try:

                fileName = self.driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver = oldDriver
                # return the file name once the download is completed
                return fileName
            except:
                pass
            time.sleep(1)
            if time.time() > endTime:
                break
