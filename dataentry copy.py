from typing import ClassVar
import csv
import time
from selenium import webdriver


with open ('bikedata.csv','r') as csvfile:
    csv_read = csv.reader(csvfile)

    for line in csv_read:
        driver = webdriver.Safari()
        driver.get('https://main.d2pnbffsfyozjx.amplifyapp.com')

        

        time. sleep(1)

        reach = driver.find_element_by_xpath('//*[@id="reach"]')
        reach.send_keys(line[0])

        stack = driver.find_element_by_xpath('//*[@id="stack"]')
        stack.send_keys(line[1])

        spacer = driver.find_element_by_xpath('//*[@id="spacer"]')
        spacer.send_keys(line[2])

        stem = driver.find_element_by_xpath('//*[@id="stem"]')
        stem.send_keys(line[3])

        htangle = driver.find_element_by_xpath('//*[@id="htangle"]')
        htangle.send_keys(line[4])

        hbrise = driver.find_element_by_xpath('//*[@id="htrise"]')
        hbrise.send_keys(line[5])

        backsweep = driver.find_element_by_xpath('//*[@id="backsweep"]')
        backsweep.send_keys(line[6])

        upsweep = driver.find_element_by_xpath('//*[@id="upsweep"]')
        upsweep.send_keys(line[7])

        hblength = driver.find_element_by_xpath('//*[@id="handlebarlength"]')
        hblength.send_keys(line[8])

        bikename = driver.find_element_by_xpath('//*[@id="bikename"]')
        bikename.send_keys(line[9])



        submit = driver.find_element_by_xpath('/html/body/form/button')
        submit.click()

        time.sleep(1)

        

        driver.close()