import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id = int(input("Enter ID : "))
options = webdriver.ChromeOptions()
options.add_argument(r"--executable_path=C:\\chromedriver.exe")
driver = webdriver.Chrome(options=options)  
driver.maximize_window()  # Maximize the browser window
base_url = "https://www.tesla.com/careers/search/job/apply/"
url_with_id = f"{base_url}{id}"

driver.get(url_with_id)
time.sleep(3)
print("successful")

driver.execute_script("window.scrollTo(0,350)")

fn_input = 'YOUR FIRST NAME'   # <------------ ENTER FIRST NAME
ln_input = 'YOUR LAST NAME'    # <------------ ENTER LAST NAME
pn_input = 'YOUR PERSONAL NAME' # <------------ ENTER PERSONAL NAME
phone_input = 'YOUR PHONE NO' # <------------ ENTER PHONE NO
email_input = 'YOUR EMAIL NO' # <------------ ENTER EMAIL NO
profile_input = 'YOUR LINKEDIN PROFILE (LINK IF ANY)' # <------------ ENTER LINKEDIN PROFILE LINK
file = "YOUR PATH TO YOUR RESUME FILE" # <------------ ENTER PATH TO YOUR RESUME FILE
dated = "ENTER DATE" # <------------ ENTER DATE

fn = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[1]/div/input")
fn.send_keys(fn_input)

ln = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[2]/div/input")
ln.send_keys(ln_input)

pn = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[4]/div/input")
pn.send_keys(pn_input)

phone = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[5]/div[1]/input")
phone.send_keys(phone_input)

ph = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[5]/div[1]/div/div/button")

cpt = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[6]/div[1]/select")
dropdown = Select(cpt)
dropdown.select_by_visible_text("Mobile")

email = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[7]/div/input")
email.send_keys(email_input)

country = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[8]/div[1]/select")
drop = Select(country)

for option in drop.options:
    if option.get_attribute("value") == "PK":
        option.click()
        break

dropdown_button = driver.find_element(By.CLASS_NAME, "tds-dropdown-trigger")
dropdown_button.click()
listbox_options = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[5]/div/div/div/div/ul/li[146]")
listbox_options.click()

button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[9]/button")
button.send_keys(Keys.ENTER)

profile = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[9]/div/div[2]/div/div/input")
profile.send_keys(profile_input)

profilelink = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/div/div[9]/div/div[3]/div/div/select")
dr = Select(profilelink)
dr.select_by_visible_text("LinkedIn")

time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

file_input_element = driver.find_element(By.CLASS_NAME,"tds-form-input-file-upload")
file_input_element.send_keys(file)

time.sleep(1)

next = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[2]/button")
next.send_keys(Keys.ENTER)

time.sleep(1)

date = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset/div[1]/div/div[1]/div[1]/button")
date.click()

d = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset/div[1]/div/div[1]/div[2]/div/div[1]/button[2]")
d.click()

da = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset/div[1]/div/div[1]/div[2]/div/div[3]/button[6]")
da.click()

month = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset/div[2]/div/div/select")
monthdrop = Select(month)
monthdrop.select_by_visible_text("7 months or more")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)

time1 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset/div[3]/div/div[1]/select")
timedrop = Select(time1)
timedrop.select_by_visible_text("Full time")

report = driver.find_element(By.CLASS_NAME, "tds-form-input-choice").is_selected()
print(report)
driver.find_element(By.CLASS_NAME, "tds-form-input-choice").click()
report = driver.find_element(By.CLASS_NAME, "tds-form-input-choice").is_selected()
print(report)

next1 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[2]/button[2]")
next1.send_keys(Keys.ENTER)

time.sleep(1)

avail = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[1]/div/div/select")
availdrop = Select(avail)
availdrop.select_by_visible_text("In 1-2 weeks")

button1 = driver.find_element(By.CLASS_NAME, "tds-form-input-choice").is_selected()
print(button1)
button1 = driver.find_element(By.CLASS_NAME, "tds-form-input-choice")
button1.click()
print("yes")


driver.execute_script("window.scrollTo(0,400)")

time.sleep(1)

driver.find_element(By.XPATH, '//input[@name="legal.legalImmigrationSponsorship" and @value="yes"]').click()
driver.find_element(By.XPATH, '//input[@name="legal.legalFormerTeslaEmployee" and @value="no"]').click()
driver.find_element(By.XPATH, '//input[@name="legal.legalFormerTeslaInternOrContractor" and @value="no"]').click()

driver.execute_script("window.scrollTo(0,750)")
time.sleep(1)

driver.find_element(By.XPATH, '//input[@name="legal.legalUniversityStudent" and @value="yes"]').click()

driver.execute_script("window.scrollTo(0,800)")
time.sleep(1)

date1 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[1]/button")
date1.click()
d1 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[1]/button[2]")
da1 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[1]/label")

while da1.text != 'September 2025':
    d1.click()

dd = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[7]/div/div/div[2]/div/div[3]/button[16]")
dd.click()

time.sleep(1)

driver.find_element(By.XPATH, '//input[@name="legal.legalReceiveNotifications" and @value="yes"]').click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

driver.find_element(By.NAME, "legal.legalAcknowledgment").click()

legalname = 'YOUR FULL NAME' # <------------ ENTER LEGAL NAME
legaln = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[3]/div/div/input")
legaln.send_keys(legalname)

next2 = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[2]/button[2]")
next2.send_keys(Keys.ENTER)

time.sleep(3)

driver.execute_script("window.scrollTo(0,700)")
time.sleep(2)

elements_to_modify = driver.find_elements(By.CLASS_NAME , "tds--disabled")
for el in elements_to_modify:
    driver.execute_script("arguments[0].classList.remove('tds--disabled');", el)

script = """
var element = document.querySelector('[disabled]');
if (element) {
    element.removeAttribute('disabled');
}
"""
driver.execute_script(script)
print("done")
time.sleep(1)

checkbox = driver.find_element(By.XPATH , "/html/body/div/div/div/form/div/div[1]/fieldset[1]/div[2]/div/input")
checkbox.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(2)

gender = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[1]/div[1]/div/select")
gendrop = Select(gender)
gendrop.select_by_visible_text("Male")

veteran = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[1]/div[2]/div/select")
vetdrop = Select(veteran)
vetdrop.select_by_visible_text("I am not a protected veteran")

race = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[2]/div[1]/div/select")
racedrop = Select(race)
racedrop.select_by_visible_text("Asian")

dis = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[2]/div[2]/div/select")
disdrop = Select(dis)
disdrop.select_by_visible_text("No, I don't have a disability")

legal = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[1]/fieldset[2]/div[3]/div/div/input")
legal.send_keys(legalname)

submit = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[2]/button[2]")
submit.send_keys(Keys.ENTER)

time.sleep(7)
print("submitted")

driver.quit()