from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

caps = DesiredCapabilities().CHROME
caps['pageLoadStrategy'] = 'none'

driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=caps, options=options)
search_terms = 'luke skywalker'
url = f'https://starwars.fandom.com/wiki/Special:Search?query={search_terms}&scope=internal&navigationSearch=true'.replace(' ', '+')
driver.get(url)

try:
    first_link = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "unified-search__result__title"))
    )
except:
    driver.quit()

first_link.click()
time.sleep(3)

driver.back()
driver.back()
driver.back()

driver.quit()