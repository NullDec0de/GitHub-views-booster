# Github views boost
# https://github.com/NullDec0de/GitHub-views-boost/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from random import randint
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
print('GitHub views boost')
print('https://github.com/NullDec0de/GitHub-views-boost/')
ask = input("Enter the required number of views: ")
url = input("Enter a link to the counter: ")
print("______________________________________________")
print("Execution started...")
count = int(ask)
i = 0
while i < count:
    driver.get(url)
    time.sleep(randint(0, 5))
    i = i+1
    print('Iteration done:', i)
    
print('Views added:', i)