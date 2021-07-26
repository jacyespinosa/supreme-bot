from selenium import webdriver
import time

chrome_driver_path = "ENTER OWN CHROMEDRIVER PATH"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)

driver.get("https://www.supremenewyork.com/shop/all")

#I WANT TO BUY ONE OF THEIR T-SHIRTS. FEEL FREE TO CHANGE PATH DEPENDING ON WHAT PRODUCT YOU WANT TO BUY.
tops = driver.find_element_by_xpath('//*[@id="nav-categories"]/li[5]/a')
tops.click()
#ADDING A DELAY SO THAT THE WEBSITE DOES NOT THINK I AM A BOT
time.sleep(1)


search_term = "ENTER THE DESIRED PRODUCT/ITEM" #e.g. Box Logo
style = "ENTER THE DESIRED PRODUCT/ITEM'S COLOR" #e.g. White
#LIST OF ITEMS IN THE T-SHIRT CATEGORY.
items = driver.find_elements_by_css_selector('li a.name-link')