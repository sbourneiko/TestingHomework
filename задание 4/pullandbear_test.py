# pip install webdriver-manager
# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.pullandbear.com/ru/%D0%B4%D0%BB%D1%8F-%D0%B6%D0%B5%D0%BD%D1%89%D0%B8%D0%BD-n6417')


#проверка поиска
def check_1():
    checkbox = driver.find_element(by=By.NAME, value='search-bar')
    checkbox.send_keys('Платье')
    checkbox.send_keys(Keys.ENTER)



#проверка поиска(негатив)
def check_2():
    checkbox = driver.find_element(by=By.NAME, value='white-search-box nav-item--search')
    checkbox.send_keys('Телевизор')
    checkbox.send_keys(Keys.ENTER)


#проверка добавления в корзину
def check_3():
    checkbox = driver.find_element(by=By.NAME, value='white-search-box nav-item--search')
    checkbox.send_keys('8711326')
    checkbox.send_keys(Keys.ENTER)
    button = driver.find_element(by=By.CLASS_NAME, value='S-product-item__name')
    button.click()
    button = driver.find_element(by=By.CLASS_NAME, value='product-intro__size-radio-inner')
    button.click()




    button = driver.find_element(by=By.CLASS_NAME, value='product-intro__add-btn')
    button.click()



#проверка добавления в корзину(негатив)
def check_4():
    checkbox = driver.find_element(by=By.NAME, value='white-search-box nav-item--search')
    checkbox.send_keys('216069992')
    checkbox.send_keys(Keys.ENTER)


check_1()