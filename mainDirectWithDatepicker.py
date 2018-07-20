from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import random

parser = argparse.ArgumentParser(description='Process website with page id')
parser.add_argument('--page', default='78', help="Set page id ")
args = parser.parse_args()

driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window();
wait = WebDriverWait(driver, 10)

driver.get("https://www.production.stage.douleutaras.com/jobs/create/signup/" + args.page)

def check_box_fucn(web_element):
    for check_box in web_element:
        item = check_box.find_elements(By.XPATH, ".//div//div")
        amount_check = random.randint(1, len(item))
        for i in range(0, amount_check):
            item[i].click()
    return len(web_element)

def select_fucn(web_element):
    for el in web_element:
        el.click()
        rows = el.find_elements(By.XPATH, ".//ul//li//a")
        index = random.randint(1, len(rows))
        rows[index-1].click()
    return len(web_element)

def radio_fucn(web_element):
    for block in web_element:
        radio_button = block.find_elements(By.XPATH, "./div/div")
        index = random.randint(1, len(radio_button))
        radio_button[index-1].click()
    return len(web_element)

#FIRST SET
first_check = check_box_fucn(driver.find_elements(By.XPATH, ".//*[@class='checkbox-section']"))
first_select = select_fucn(driver.find_elements(By.XPATH, '//*[@class="custom-modal-selectbox gradient-box"]'))
first_radio = radio_fucn(driver.find_elements(By.XPATH, "//*[@class='radio-section']"))
checkboxes = driver.find_elements(By.XPATH, ".//*[@class='checkbox-section']")
selects = driver.find_elements(By.XPATH, '//*[@class="custom-modal-selectbox gradient-box"]')
radio_blocks = driver.find_elements(By.XPATH, "//*[@class='radio-section']")

while first_select < len(selects) or first_radio < len(radio_blocks) or first_check < len(checkboxes):
    tmp1 = len(selects)
    tmp2 = len(radio_blocks)
    tmp3 = len(checkboxes)

    if first_select < len(selects):
        for select in selects:
            if -1 == select.find_element(By.XPATH,'./parent::select-choice-input/parent::form-input/parent::div/parent::div').get_attribute("class").find("has-success"):
                select.click()
                rows = select.find_elements(By.XPATH, ".//ul//li//a")
                index = random.randint(1, len(rows))
                rows[index-1].click()
        checkboxes = driver.find_elements(By.XPATH, ".//*[@class='checkbox-section']")
        selects = driver.find_elements(By.XPATH, '//*[@class="custom-modal-selectbox gradient-box"]')
        radio_blocks = driver.find_elements(By.XPATH, "//*[@class='radio-section']")


    if first_radio < len(radio_blocks):
        for radio in radio_blocks:
            if -1 == radio.find_element(By.XPATH,'./../../../..').get_attribute("class").find("has-success"):
                radio_button = radio.find_elements(By.XPATH, "./div/div")
                index = random.randint(1, len(radio_button))
                radio_button[index-1].click()
        checkboxes = driver.find_elements(By.XPATH, ".//*[@class='checkbox-section']")
        selects = driver.find_elements(By.XPATH, '//*[@class="custom-modal-selectbox gradient-box"]')
        radio_blocks = driver.find_elements(By.XPATH, "//*[@class='radio-section']")

    if first_check < len(checkboxes):
        for checkbox in checkboxes:
            if -1 == checkbox.find_element(By.XPATH,'./../../../..').get_attribute("class").find("has-success"):
                check = checkbox.find_elements(By.XPATH, ".//div//div")
                amount_check = random.randint(1, len(check))
                for i in range(0, amount_check):
                    check[i].click()
        checkboxes = driver.find_elements(By.XPATH, ".//*[@class='checkbox-section']")
        selects = driver.find_elements(By.XPATH, '//*[@class="custom-modal-selectbox gradient-box"]')
        radio_blocks = driver.find_elements(By.XPATH, "//*[@class='radio-section']")
    first_select = tmp1
    first_radio = tmp2
    first_check = tmp3

try:
    datapicker = driver.find_element(By.CSS_SELECTOR, "#element_10565_container > div > form-input > date-input > div > input")
    if datapicker.is_displayed():
        datapicker.click()
        days = driver.find_elements(By.XPATH, "//*[@class='day']")
        day_index = random.randint(0, len(days))
        days[day_index].click()
except NoSuchElementException:
    day_index = 0;

text_areas = driver.find_elements(By.CSS_SELECTOR, ".controls > form-input > textarea-input > textarea")
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

accept = driver.find_element(By.XPATH,
                             '//*[@id="termsAndConditions_container"]/div/form-input/consents-checkbox-input/div/div/label')
#accept.click();
ActionChains(driver).move_to_element_with_offset(accept,1,0).click().perform()

next = driver.find_element(By.XPATH,
                           '//*[@id="default-form-page"]/div/div[2]/div[1]/job-posting-form-container/form/div/div/div[2]/button')
next.click();

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-directive.ng-scope")))
assert driver.find_element(By.CSS_SELECTOR, ".modal-directive.ng-scope").is_displayed()
print(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/h3").text)
driver.close()

