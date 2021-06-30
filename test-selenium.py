from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main import get_output_filepath
import urllib.request
import os
import json

# use adblocker to block ad popups that will disrupt DOM and cause element references to be stale
def get_adblocker_path():
    
    curr_dir = os.path.dirname(__file__)
    rel_path = 'ublock origin\extension_1_36_0_0.crx' 
    abs_path = os.path.join(curr_dir, rel_path)

    return abs_path

def create_chrome_driver():
        
    PATH = 'C:\Program Files (x86)\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_extension(get_adblocker_path())

    caps = DesiredCapabilities().CHROME
    caps['pageLoadStrategy'] = 'none'

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=caps, options=options)

    return driver

def get_categories_from_output():

    categories: dict = {}

    with open(get_output_filepath(), 'r') as output_file:
        categories = json.load(output_file)

    return categories

def loop_thru_categories(driver: WebDriver, categories: dict):

    for category in categories:   
        for item in categories[category]:

            search_terms = ''
            search_terms = item['search_terms']

            url = f'https://starwars.fandom.com/wiki/Special:Search?query={search_terms}&scope=internal&navigationSearch=true'.replace(' ', '+')
            driver.get(url)

            try:
                first_link: WebElement = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'unified-search__result__title'))
                )
                first_link.click()

                image: WebElement = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'pi-image-thumbnail'))
                )

                download_image(image, item)

            # in case DOM element cannot be found e.g. ad popup changes DOM structure after link element has been assigned, so now no reference
            except:
                first_link: WebElement = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'unified-search__result__title'))
                )
                first_link.click()

                image: WebElement = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'pi-image-thumbnail'))
                )

                download_image(image, item)

            finally:
                print('search terms: ', search_terms)

    driver.quit()   

def download_image(image: WebElement, item: dict):
    image_url = image.get_attribute("src")
    
    abs_path = os.path.dirname(__file__)
    rel_path = f'output\images\{item["category"]}-{str(item["id"])}.jpg'
    file_path = os.path.join(abs_path, rel_path)

    print('output image file: ', file_path)
    urllib.request.urlretrieve(url=image_url, filename=file_path)


if __name__ == '__main__':
    categories = get_categories_from_output()
    print(categories)

    driver = create_chrome_driver()
    loop_thru_categories(driver, categories)