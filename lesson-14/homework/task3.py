import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.demoblaze.com/")
time.sleep(3)


laptop_section = driver.find_element(By.LINK_TEXT, "Laptops")
laptop_section.click()
time.sleep(3)


laptop_data = []    
with open("laptops.json", "w") as json_file:
    json.dump(laptop_data, json_file, indent=4)

print("Datas are saved")


driver.quit()



