from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def main():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get('https://www.google.com')
    sleep(10)
    element = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
    element.send_keys('Hello World')
    element.submit()
    kolona = browser.find_element(By.ID,'center_col')
    linkovi = kolona.find_elements(By.CSS_SELECTOR,'a')
    for link in linkovi:
        if 'likendin' in link.get_attribute('href') and link.get_attribute('href') != None:
            print(link.get_attribute('href'))

    elementi = [element.get_attribute('href') for element in linkovi if element.get_attribute('href')]

if __name__ == "__main__":
    main()