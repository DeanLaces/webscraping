from argparse import Action
from email import parser
from bs4 import BeautifulSoup
import time 
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import string







def search(keyword,price):

    print("Searching for " + keyword)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    driver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    driver.set_window_size(1920,927)
    driver.get('http://ebay.com')
    time.sleep(5)
    driver.find_element(By.ID, 'gh-as-a').click()
    time.sleep(2)
    driver.find_element(By.ID, '_nkw').send_keys(keyword)
    time.sleep(2)
    driver.find_element(By.NAME, '_udlo').send_keys('0')
    time.sleep(2)
    driver.find_element(By.NAME, '_udhi').send_keys(str(price))
    time.sleep(2)
    driver.find_element(By.NAME,'LH_Auction').click()
    time.sleep(2)
    driver.find_element(By.NAME,'LH_FS').click()
    time.sleep(2)
    sortBy = Select(driver.find_element(By.ID,'LH_SORT_BY'))
    sortBy.select_by_value('10')
    time.sleep(2)
    resultsPerPage = Select(driver.find_element(By.ID,'LH_IPP'))
    resultsPerPage.select_by_value('240')
    time.sleep(2)
    driver.find_element(By.ID,'searchBtnLowerLnk').click()


    url = driver.current_url
    data = requests.get(url)
    mySoup = BeautifulSoup(data.content,'html.parser')
    

  
    temp_prices = [item.get_text(strip=True) for item in mySoup.select("span.s-item__price")]
    finalPrices = []
    sum_values = 0

    

    for price in temp_prices:
        price = price.replace("$","")
        if(price.__contains__("to")):
            low_lim = float(price[0:price.index("to")])
            high_lim = float(price[price.index("to") + 2: len(price)])
            finalPrices.append(int((low_lim + high_lim) / 2))
        else:
            finalPrices.append(int(float(price)))

    



    for new_price in finalPrices:
        sum_values+= new_price

    pageAvg = sum_values / len(finalPrices)

    def minVal(nums,numElements):

        smallVals = []

        for i in range(numElements):
            min = nums[0] 
            for num in nums:
                if(min>num):
                    min = num
            nums.remove(min)
            smallVals.append(min)

        return smallVals

    print("The Page Average is " + str(pageAvg))
    smallest_values = minVal(finalPrices,10)
    print("The smallest values are:  \n")
    for val in smallest_values:
        print('$' + str(val))
    

    driver.close()








# Configure your items and their respective prices in this dict, I chose to query electronic parts
items = {'walkman':58, 'document camera': 50,'children camera':10, 
         'vcr belt': 8, 'ppj ac power cord': 10, 'wireless headphones': 5,
           'laser disc': 15, 'caregiver pager': 10}






    

def __main__():
    for item in items.items():
        search(item[0],item[1])
        
        
        
        
if(__name__ == '__main__'):
    while(True):
        __main__()
        time.sleep(60)
   

    
