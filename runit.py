from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import key_actions
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import streamlit as st 

prompt = st.text_input('Input product name')
if prompt:
    PATH = r"C:\Users\weepo\Desktop\chromedriver\chromedriver.exe"
    website = 'https://www.lazada.sg/'

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  #  Waits for page to be interactive


    driver = webdriver.Chrome(PATH,desired_capabilities=caps)
    driver.get(website)
    titleslist = []
    pricelist = []

    time.sleep(5)

    nameofobject = f'{prompt}'
    search = driver.find_element(By.NAME,"q")
    search.send_keys(f'{nameofobject}')
    search.send_keys(Keys.RETURN)

    time.sleep(5)

    search2 = driver.find_elements(By.CLASS_NAME ,"dumOn")[1].click()

    time.sleep(5)
    try:
        collects = driver.find_elements(By.CLASS_NAME,"buTCk")

        for i,collect in enumerate(collects):
            collect2 = collect
            get_title = collect.find_element(By.TAG_NAME,"a")
            titleslist.append(get_title.get_attribute("title"))


            get_price = collect2.find_element(By.TAG_NAME,"span")
            pricelist.append(get_price.text)

            if i == 6:
                break
    except:
        driver.refresh()
        collects = driver.find_elements(By.CLASS_NAME,"buTCk")    
        
        for i,collect in enumerate(collects):
            collect2 = collect
            get_title = collect.find_element(By.TAG_NAME,"a")
            titleslist.append(get_title.get_attribute("title"))


            get_price = collect2.find_element(By.TAG_NAME,"span")
            pricelist.append(get_price.text)

            if i == 6:
                break




    import pandas as pd
    df = pd.DataFrame(list(zip(titleslist,pricelist)),
                columns =['Name', 'price'])
    
    st.dataframe(df)

