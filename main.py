from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
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

'''
THIS FUNCTION WILL RUN A WHILE LOOP BY FINDING CSS_SELECTOR (PARAMETER), ONCE IT FINDS THAT SPECIFIC
CSS SELECTOR, THEN IT WILL ADD IT TO THE ELEMENT LIST AND RETURNS THE ELEMENT.
'''
def wait_for_selectors(css_selector):
    elements = []
    while len(elements) == 0:
        elements = driver.find_elements_by_css_selector(css_selector)
        time.sleep(0.00001)
    return elements


'''
THIS FUNCTION WILL RUN A WHILE LOOP IF ELEMENT IS NONE BY FINDING CSS_SELECTOR (PARAMETER), ONCE IT FINDS THAT SPECIFIC
CSS SELECTOR, THEN IT WILL UPDATE THE ELEMENT VARIABLE AND RETURNS THE ELEMENT.
'''
def add_to_cart(css_selector):
    element = None
    while element is None:
        element = driver.find_element_by_css_selector(css_selector)
        time.sleep(0.00001)
    return element


'''
THIS FUNCTION WILL RUN A WHILE LOOP IF ELEMENT IS NONE BY FINDING CSS_SELECTOR (PARAMETER), ONCE IT FINDS THAT SPECIFIC
CSS SELECTOR, THEN IT WILL UPDATE THE ELEMENT VARIABLE AND RETURNS THE ELEMENT.
'''
def check_out_now(css_selector):
    element = None
    while element is None:
        element = driver.find_element_by_css_selector(css_selector)
        time.sleep(0.2)
    return element

search_term = "ENTER THE DESIRED PRODUCT/ITEM" #e.g. Box Logo
style = "ENTER THE DESIRED PRODUCT/ITEM'S COLOR" #e.g. White
#LIST OF ITEMS IN THE T-SHIRT CATEGORY.
items = driver.find_elements_by_css_selector('li a.name-link')

'''
LOOP THROUGH EACH ITEM IN THE ITEMS LIST AND IF THE SEARCH_ITEM(DESIRED PRODUCT) MATCHES THE ITEM IN THE FOR LOOP,
THEN THAT SPECIFIC ITEM WILL BE CLICKED AND WOULD CALL THE WAIT_FOR_SELECTORS(STYLE) FUNCTION TO ACCESS THE SPECIFIC COLOR
OF THE ITEM SELECTED AND SELECTS THE SIZE(e.g. small).
'''
for item in items:
    if search_term in item.text:
        item.click()
        color = wait_for_selectors(f"ul li button[data-style-name={style}]")
        color[0].click()
        size = driver.find_element_by_css_selector('fieldset select#s option')

        '''IF THE SIZE IS AVAILABLE, THEN WILL IT TRY TO CLICK ADD TO CART BUTTON, IF THE ADD TO CART BUTTON IS GRAYED
        OUT, THEN THAT MEANS THAT SPECIFIC SIZE IS SOLD OUT. HOWEVER, IN SUPREME WEBSITE, IF A SPECIFIC SIZE IS SOLD
        OUT FOR INSTANCE SIZE SMALL, THE DEFAULT OPTION WILL UNTO THE NEXT AVAILABLE SIZE. SINCE THIS IS SUPREME, AS
        LONG AS WE SECURE THAT ITEM, WE WANT TO GET THE NEXT BEST AVAILABLE SIZE. 
        ***NOTE: SOMETIMES THE PAGE HAVE A DELAY, THEREFORE, IT IS BEST TO ADD A SLEEPER TO KEEP 
        LOOKING FOR THAT BUTTON..
        '''
        if size.text == "Small":
            try:
                add = add_to_cart('fieldset input.button')
                add.click()
            except (StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException) as error:
                time.sleep(0.0001)
            '''
            ONCE THE SELECTED SIZE IS ADDED TO THE CART, IT WILL CLICK THE CHECK OUT NOW BUTTON. SOMETIMES THE PAGE
            HAVE A DELAY, THEREFORE, IT IS BEST TO ADD A SLEEPER TO KEEP LOOKING FOR THAT BUTTON.
            '''
            try:
                checkout = check_out_now('div a.button.checkout')
                checkout.click()
            except (StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException) as error:
                time.sleep(0.0001)