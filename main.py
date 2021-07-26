from selenium import webdriver


chrome_driver_path = "ENTER OWN CHROMEDRIVER PATH"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)

driver.get("https://www.supremenewyork.com/shop/all")