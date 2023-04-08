from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import requests 
from bs4 import BeautifulSoup
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.nbcnews.com/health/")
driver.maximize_window()

url ="https://www.nbcnews.com/health"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

with open("article_titles.txt", "w", encoding="utf-8") as f:
    while True:
        lists = driver.find_elements(by=By.CLASS_NAME, value="wide-tease-item__wrapper")

        
        for lst in lists:
            title = lst.find_element(by=By.CLASS_NAME, value="wide-tease-item__headline").text
            f.write(title + "\n")

       
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)  # Wait for the "Load More" button to appear
        try:
            links = driver.find_element(by=By.CLASS_NAME, value="styles_loadMoreWrapper__pOldr")
            links.click()
        except:
            break

with open('article_titles.txt', 'r') as f_in:
    unique_lines = set(f_in.readlines())

with open('article_titles_fixing.txt', 'w') as f_out:
    f_out.writelines(unique_lines)



#driver.quit()

