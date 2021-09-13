#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read("FacebookPokesBot.ini", encoding="utf-8")

DRIVER_PATH = config["DEFAULT"]["DRIVER_PATH"]
PROFILE_PATH = config["DEFAULT"]["PROFILE_PATH"]
TIMEOUT = int(config["DEFAULT"]["TIMEOUT"])
FACEBOOK_POKE_BUTTON_TEXT = config["DEFAULT"]["FACEBOOK_POKE_BUTTON_TEXT"]

def findAndPrintNames(drv):
    names = drv.find_elements_by_xpath("//*[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']")
    if names:
        for x in names:
            print(f"[{datetime.now()}] {x.get_attribute('innerHTML')}")
        print()

def findAndPoke(drv):
    buttons = drv.find_elements_by_xpath(f"//*[contains(text(),'{FACEBOOK_POKE_BUTTON_TEXT}')]")
    if buttons:
        for x in buttons:
            ActionChains(drv).click(x).perform()
            # pass
        findAndPrintNames(drv)
        # drv.refresh()

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + PROFILE_PATH)
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get("https://facebook.com/pokes")

try:
    counter = 0
    while True:
        if counter >= int(180 / TIMEOUT) :
            print(f"[{datetime.now()}] REFRESHING PAGE...")
            counter = 0
            driver.refresh()
        
        sleep(TIMEOUT)

        findAndPoke(driver)

        counter += 1
    
except Exception as e:
    print(e)
    driver.quit()
    input("Press any key to exit...")
