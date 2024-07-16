from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

form_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform?usp=send_form"
driver.get(form_url)

#Filling name
name = driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
name.send_keys("Palak Bansal")
print("Name Done")

#Filling contact number
contact = driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
contact.send_keys("9191919191")
print("Contact Done")

#Filling email-id
email_id = driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
email_id.send_keys("palakbansal8810@gmail.com")
print("Email Done")

#Filling address
address = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i13']")
address.send_keys("Delhi, India")
print("Address Done")

#Filling pincode
pin_code = driver.find_element(By.XPATH, "//input[@aria-labelledby='i17']")
pin_code.send_keys("110009")
print("Pin Code Done")

#Filling gender
gender = driver.find_element(By.XPATH, "//input[@aria-labelledby='i26']")
gender.send_keys("Female")
print("gender Done")

#Finding Code
code = driver.find_element(By.XPATH, "//div[@id='i30']//span[@class='M7eMe']/b").text
print(code)

#Filling code
code_field = driver.find_element(By.XPATH, "//input[@aria-labelledby='i30']")
code_field.send_keys(code)
print("Code input done")

#Filling dob
dob = driver.find_element(By.XPATH, "//input[@aria-labelledby='i25']")
dob.send_keys("23012006")
print("dob Done")

#submitting the form
submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
submit_button.click()

#Taking Screenshot 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Your response has been recorded.")]')))

#Saving the screenshot taken
driver.save_screenshot('confirmation_screenshot.png')

driver.quit()

