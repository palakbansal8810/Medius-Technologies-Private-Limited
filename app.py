import os
from flask import Flask, request, render_template
from flask_mail import Mail, Message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Initialize Flask app and Flask-Mail
app = Flask(__name__)      
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("GMAIL_ID")
app.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)

# filling google form and capturing ss
def filling_google_form():
    try:
        driver = webdriver.Chrome()

        form_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform?usp=send_form"
        driver.get(form_url)

        # Filling name
        name = driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
        name.send_keys("Palak Bansal")
        print("Name Done")

        # Filling contact number
        contact = driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
        contact.send_keys("9191919191")
        print("Contact Done")

        # Filling email-id
        email_id = driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
        email_id.send_keys("palakbansal8810@gmail.com")
        print("Email Done")

        # Filling address
        address = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i13']")
        address.send_keys("Delhi, India")
        print("Address Done")

        # Filling pincode
        pin_code = driver.find_element(By.XPATH, "//input[@aria-labelledby='i17']")
        pin_code.send_keys("110009")
        print("Pin Code Done")

        # Filling gender
        gender = driver.find_element(By.XPATH, "//input[@aria-labelledby='i26']")
        gender.send_keys("Female")
        print("gender Done")

        # Finding Code
        code = driver.find_element(By.XPATH, "//div[@id='i30']//span[@class='M7eMe']/b").text
        print(code)

        # Filling code
        code_field = driver.find_element(By.XPATH, "//input[@aria-labelledby='i30']")
        code_field.send_keys(code)
        print("Code input done")

        # Filling dob
        dob = driver.find_element(By.XPATH, "//input[@aria-labelledby='i25']")
        dob.send_keys("23012006")
        print("dob Done")

        # Submitting the form
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
        submit_button.click()

        # Taking Screenshot 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Your response has been recorded.")]')))

        # Saving the screenshot taken
        driver.save_screenshot('confirmation_screenshot.png')
        screenshot_path = 'confirmation_screenshot.png'
        driver.quit()

        return screenshot_path

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


@app.route('/send_email', methods=['POST'])
def send_email():
# Fill Google Form and capture screenshot
    screenshot_path = filling_google_form()

    if screenshot_path:
        try:
            print("Preparing to send email...")

# Preparing email message
            subject = 'Python (Selenium) Assignment - Palak Bansal'  
            body = 'Please find attached the submission for the Python (Selenium) assignment.'
            sender = 'palakbansal8810@gmail.com'
            recipients = ['palakb8810@gmail.com'] 

# Screenshot
            with app.open_resource(screenshot_path) as fp:
                msg = Message(subject=subject, sender=sender, recipients=recipients)
                msg.body = body
                msg.attach("screenshot.png", "image/png", fp.read())
                pdf_path = "resume.pdf"  
                with app.open_resource(pdf_path) as fp:
                    msg.attach("resume.pdf", "application/pdf", fp.read())
            
            print("Email message prepared")

            mail.send(msg)
            print("Email sent successfully")

# Deleting screenshot after sending email 
            os.remove(screenshot_path)
            print("Screenshot deleted")

            return {'message': 'Email sent successfully'}
        
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return { str(e)}

    else:
        print("Error occurred while filling Google Form and capturing screenshot.")
        return ('error filling Google Form and capturing screenshot.')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  

