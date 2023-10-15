from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge Dev/Application/msedge.exe"
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options = options)
driver.get('https://quangtrinh1312.github.io/addition-calculate/')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'a').send_keys('1')
driver.find_element(By.ID, 'b').send_keys('2')
driver.find_element(By.ID, 'btn').click()
driver.maximize_window()