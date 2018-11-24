from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox(executable_path='./geckodriver')

browser.get_window_size(1024,768)
