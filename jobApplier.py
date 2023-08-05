from argparse import Action
from cgitb import text
from gettext import find
from operator import index, indexOf
from queue import Empty
from typing import final
from webbrowser import get
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class jobApplier:




    def __init__():

        #LOGIN STARTS
        NUM_TABS = 10
        MY__PASSWORD = None # Enter password here 
        MY_EMAIL_ADDRESS = None # Enter Email Address here
        MY_PATH = None # Enter chromedriver path here 

        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome-beta'
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_experimental_option("detach",True)

        
        driver = webdriver.Chrome(MY_PATH)
        driver.set_window_size(1920,927)
        driver.get('http://indeed.com')
        driver.implicitly_wait

        loggedIn = False

        while(not loggedIn):

            originalWindowHandle = driver.current_window_handle
            driver.find_element(By.LINK_TEXT,'Sign in').click()
            time.sleep(2)
            driver.find_element(By.ID,'login-google-button').click()
            time.sleep(2)

            for window_handle in driver.window_handles:
                if(window_handle!= originalWindowHandle):
                    driver.switch_to.window(window_handle)
                    temp = window_handle
                    break


            driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys(MY_EMAIL_ADDRESS)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys(Keys.ENTER)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys(MY__PASSWORD)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys(Keys.ENTER)
            loggedIn = True
            # LOGIN SUCCEEDED, begin opening tabs.
        time.sleep(5)

        # Iterates through a href type elements and opens the link a new tab
        driver.switch_to.window(originalWindowHandle)
        
        all_link_elements = driver.find_elements(By.TAG_NAME,"a")
        all_link_elements_string = []
        for string_element in all_link_elements:
            all_link_elements_string.append(string_element.text)
        beginIndex = all_link_elements_string.index("Employers: post a job")
        hrefs = []

    

        del all_link_elements[0:beginIndex + 1]
        del all_link_elements[49:len(all_link_elements)]

        #Job is a string(href)

        def alternativeJobFunction(job):
            #Checks if 'multiple choice selector' type questions occur
            selectorQuestions = driver.find_elements(By.CLASS_NAME, 'css-19kaor0 eu4oa1w0') 
            #Checks if textbook type questions occur 
            textboxQuestions = driver.find_elements(By.CLASS_NAME,'css-anc3lu e1jgz0i3') 
            #Checks if dropdown type questions occur
            dropdownQuestions = driver.find_elements(By.CLASS_NAME,'css-1jy7ya7 e1excnjx0') 
            
            questionTypes = [selectorQuestions,textboxQuestions,dropdownQuestions]
            
            for questionType in questionTypes:
                if(questionType== Empty):
                    questionTypes.remove(questionType)
            
            for questionType in questionTypes:
                for question in questionType:
                    question.click()
                    # Checks if Resume pop up occurs 
                    if(driver.find_element(By.CLASS_NAME,'ia-continueButton ia-Resume-continue css-vw73h2 e8ju0x51').is_displayed()):
                        driver.find_element(By.CLASS_NAME,'ia-continueButton ia-Resume-continue css-vw73h2 e8ju0x51').click()
                    elif(driver.find_element(By.CLASS_NAME,'ia-continueButton css-10eonrg e8ju0x51').is_displayed()):
                        driver.find_element(By.CLASS_NAME,'ia-continueButton css-10eonrg e8ju0x51').click()
                    else:
                        print("Error occured.")
                        
      
           
            

            
            


        def applyToJob(job):
            driver.get(job)
            driver.switch_to.window(driver.current_window_handle)

            

            try:
                if(driver.find_element(By.ID,"indeedApplyButton").is_displayed()):
                    driver.find_element(By.ID,"indeedApplyButton").click()
                    time.sleep(2)
                    if(driver.find_element(By.TAG_NAME,'button').is_displayed()):
                        tempElement = driver.find_element(By.TAG_NAME,'button')
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
                        tempElement.click()
                    else:
                        alternativeJobFunction(job) 
            except NoSuchElementException as ne:
                print("This website requires application on company site.This is the exception  " + str(ne) )
            


        for element in all_link_elements:
            hrefs.append(driver.find_element(By.LINK_TEXT,element.text).get_attribute('href'))
        
        for i in range(NUM_TABS):
            applyToJob(hrefs[i])
            time.sleep(2)
        
        

        

        
    



    if(__name__ == '__main__'):
        __init__()