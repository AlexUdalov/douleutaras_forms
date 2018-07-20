import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException, \
    ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import argparse
import random

parser = argparse.ArgumentParser(description='Process website with page id')
parser.add_argument('--page', default='metafores-times', help="Set page id ")
args = parser.parse_args()


driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

driver.get("https://www.production.stage.douleutaras.com/job/create/" + args.page)
driver.switch_to.frame(driver.find_element_by_name("iFrameForm"))

try:
    category = driver.find_element(By.XPATH, "//*[@class='landing-frame__list ng-scope']")
    if category.is_displayed():
        time.sleep(3)
        options = driver.find_elements(By.CSS_SELECTOR, ".landing-frame__item.ng-scope")
        index = random.randint(1, len(options))
        options[index - 1].click()
except NoSuchElementException:
    category = 0

time.sleep(3)

def check_box_fucn(web_element):
    for check_box in web_element:
        item = check_box.find_elements(By.XPATH, ".//div")
        amount_check = random.randint(1, len(item))
        for i in range(0, amount_check):
            driver.execute_script("arguments[0].style.border='3px solid green'", item[i])
            time.sleep(0.1)
            item[i].click()
    return len(web_element)

def select_fucn(web_element):
    minus = 0
    plus = 0
    for inx in web_element:
        if -1 == inx.find_element(By.XPATH, './../../../../../..').get_attribute("class").find("success"):
            try:
                inx.click()
                elements = inx.find_elements(By.XPATH, "./../div/div/span")
                s_index = random.randint(1, len(elements))
                elements[s_index - 1].click()
                plus = plus + 1
            except ElementNotVisibleException:
                minus = minus - 1
                inx.click()
            time.sleep(0.15)
    return plus + minus

def radio_fucn(web_element):
    minus = 0
    for block in web_element:
        try:
            radio_button = block.find_elements(By.XPATH, "./div")
            index = random.randint(1, len(radio_button))
            driver.execute_script("arguments[0].style.border='3px solid black'",  radio_button[index-1])
            time.sleep(0.1)
            radio_button[index-1].click()
        except StaleElementReferenceException:
            minus = minus - 1
    return len(web_element) + minus

#FIRST SET
first_check = check_box_fucn(driver.find_elements(By.CSS_SELECTOR, ".landing-frame__field > form-input > nova-checkbox-input"))
first_radio = radio_fucn(driver.find_elements(By.CSS_SELECTOR, ".landing-frame__field > form-input > nova-radio-choice-input"))
first_select = select_fucn(driver.find_elements(By.XPATH, '//*[@class="dropdown-header dropdown-header--placeholder"]'))

checkboxes = driver.find_elements(By.CSS_SELECTOR, ".landing-frame__field > form-input > nova-checkbox-input")
selects = driver.find_elements(By.XPATH, '//*[@class="dropdown-header dropdown-header--placeholder"]')
radio_blocks = driver.find_elements(By.CSS_SELECTOR, ".landing-frame__field > form-input > nova-radio-choice-input")

while first_select < len(selects) \
        or first_radio < len(radio_blocks) \
        or first_check < len(checkboxes):
    try:
        tmp1 = len(selects)
        tmp2 = len(radio_blocks)
        tmp3 = len(checkboxes)

        if first_radio < len(radio_blocks):
            for radio in radio_blocks:
                if -1 == radio.find_element(By.XPATH,'./../../..').get_attribute("class").find("success"):
                    radio_button = radio.find_elements(By.XPATH, "./div")
                    index = random.randint(1, len(radio_button))
                    radio_button[index-1].click()

            checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                              ".landing-frame__field > form-input > nova-checkbox-input")
            selects = driver.find_elements(By.XPATH, '//*[@class="dropdown-header dropdown-header--placeholder"]')
            radio_blocks = driver.find_elements(By.CSS_SELECTOR,
                                                ".landing-frame__field > form-input > nova-radio-choice-input")

        if first_select < len(selects):
            for s in selects:
                if -1 == s.find_element(By.XPATH,'./../../../../../..').get_attribute("class").find("success"):
                    #EC.element_to_be_clickable(selects[i])
                    s.click()
                    #drop_list = driver.find_elements(By.XPATH, "//*[@class='dropdown-box']")
                    #single_drop = drop_list[i]
                    elements = s.find_elements(By.XPATH, "./../div/div/span")
                    index = random.randint(1, len(elements))
                    try:
                        elements[index - 1].click()
                    except IndexError:
                        elements[0].click()

            checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                              ".landing-frame__field > form-input > nova-checkbox-input")
            selects = driver.find_elements(By.XPATH, '//*[@class="dropdown-header dropdown-header--placeholder"]')
            radio_blocks = driver.find_elements(By.CSS_SELECTOR,
                                                ".landing-frame__field > form-input > nova-radio-choice-input")

        if first_check < len(checkboxes):
            for checkbox in checkboxes:
                if -1 == checkbox.find_element(By.XPATH,'./../../../..').get_attribute("class").find("success"):
                    check = checkbox.find_elements(By.XPATH, ".//div")
                    amount_check = random.randint(1, len(check))
                    for i in range(0, amount_check):
                        check[i].click()

            checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                              ".landing-frame__field > form-input > nova-checkbox-input")
            selects = driver.find_elements(By.XPATH, '//*[@class="dropdown-header dropdown-header--placeholder"]')
            radio_blocks = driver.find_elements(By.CSS_SELECTOR,
                                                ".landing-frame__field > form-input > nova-radio-choice-input")

        first_select = tmp1
        first_radio = tmp2
        first_check = tmp3
    except ElementNotVisibleException and StaleElementReferenceException:
        driver.find_element_by_tag_name("body").send_keys(Keys.UP)

try:
    datapicker = driver.find_element(By.CSS_SELECTOR, "#element_10565_container > div > form-input > date-input > div > input")
    if datapicker.is_displayed():
        datapicker.click()
        days = driver.find_elements(By.XPATH, "//*[@class='day']")
        day_index = random.randint(0, len(days))
        days[day_index].click()
except NoSuchElementException:
    day_index = 0

try:
    location = driver.find_element(By.XPATH, "//*[@class='landing-frame__field landing-frame__field--location']/input")
    if location.is_displayed():
        location.send_keys("a")
        time.sleep(2)
        wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@class='pac-container pac-logo'][3]")))
        places = driver.find_elements(By.XPATH, "//*[@class='pac-container pac-logo'][3]/div")
        index_p = random.randint(1, len(places))
        places[index_p-1].click()
except NoSuchElementException:
    index_p = 0



text_areas = driver.find_elements(By.CSS_SELECTOR, ".landing-frame__field > form-input > nova-textarea-input > textarea")
for text in text_areas:
    text.send_keys("test")

phone = driver.find_element(By.XPATH, ".//*[@type='tel']")
number = random.randint(10000000, 99999999)
phone.send_keys("69" + str(number))

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user_email_linput"]')))
email = driver.find_element(By.XPATH, '//*[@id="user_email_linput"]')
email.send_keys("test@mail.com")

first_name = driver.find_element(By.XPATH, '//*[@id="user_first_name_linput"]')
first_name.send_keys("First")

last_name = driver.find_element(By.XPATH, '//*[@id="user_last_name_linput"]')
last_name.send_keys("Second")

#if(args.page != "metafores-times"):
accept = driver.find_elements(By.XPATH,'//*[@class="checkbox-custom-label ng-binding"]')
driver.execute_script("arguments[0].style.border='3px solid red'", accept[len(accept)-2])

ActionChains(driver).move_to_element_with_offset(accept[len(accept)-2],12,4).click().perform()

next = driver.find_element(By.CSS_SELECTOR,'.btn.btn-blue.ng-binding')
next.click();

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-directive.ng-scope")))
assert driver.find_element(By.CSS_SELECTOR, ".modal-directive.ng-scope").is_displayed()
print(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/h3").text)
driver.close()

