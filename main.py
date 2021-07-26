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

time.sleep(1)