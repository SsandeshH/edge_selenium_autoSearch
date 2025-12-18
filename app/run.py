from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# ------------------ SETUP ------------------
edge_options = Options()
edge_options.add_argument("--start-maximized")

# ======================== kill all tasks of ms edge for this.. multiple profile browser

# edge_options.add_argument(
#     r"--user-data-dir=C:\Users\ASUS\AppData\Local\Microsoft\Edge\User Data"
# )
# edge_options.add_argument("--profile-directory=Profile 1")



# ================================

service = Service(r"F:\edge_automator\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_options)

wait = WebDriverWait(driver, 20)

driver.get("https://www.bing.com")

# ------------------ SEARCH TERMS ------------------
with open("words.json","r",encoding="utf-8") as file:
    data = json.load(file)

search_words = data['search_words']

# ------------------ LOOP ------------------
for words in search_words:
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "sb_form_q"))
    )

    search_box.clear()
    search_box.send_keys(words)
    search_box.send_keys(Keys.ENTER)

    # wait for results page to load
    wait.until(
        EC.presence_of_element_located((By.ID, "b_content"))
    )

    time.sleep(8)  # optional (visual pause)

# driver.quit()

