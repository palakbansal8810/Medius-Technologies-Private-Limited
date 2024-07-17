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
app.config['MAIL_USERNAME'] = 'GMAIL_ID' # replace it with YOUR GMAIL ID
app.config['MAIL_PASSWORD'] = 'PASSWORD' # replace it with PASSWORD

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)

# filling google form and capturing ss
@app.route('/fill_form', methods=['POST'])
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
        if screenshot_path:
            
            return 'path of screenshot of confirmation\n'+ screenshot_path

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

@app.route('/send_email', methods=['POST'])
def send_email():
# Fill Google Form and capture screenshot
    screenshot_path = 'confirmation_screenshot.png'

    if screenshot_path:
        try:
            print("Preparing to send email...")

# Preparing email message
            subject = 'Python (Selenium) Assignment - Palak Bansal'  
            body = '''
Dear Hiring Manager,

    I am submitting my assignment for the Python (Selenium) project. Please find the required items attached and linked below:
        1.Screenshot: The screenshot of the form filled via code is attached to this email.

        2.Source Code: "https://github.com/palakbansal8810/Medius-Technologies-Private-Limited.git"

        3.Documentation: A brief documentation of my approach is included in the README.md file in the repository.

        4.Resume: My resume is attached in the repository.

        5.Past Projects: 
            Here's my some of the scraping and automation work using selenium and bs4:
               1. https://github.com/palakbansal8810/google-lens-web-scraping- (google-lens)
               2. https://github.com/palakbansal8810/web_scraping.git (pharmeasy, apollo24, tata1mg)
               3. https://github.com/palakbansal8810/linkedin-ws (linkedin)

            Some of my machine learning projects:
                1. https://github.com/palakbansal8810/anaemia_pred_endtoend.git
                2. https://github.com/palakbansal8810/MovieRecommender.git
                3. https://github.com/palakbansal8810/HomePricePredictor.git
                4. https://github.com/palakbansal8810/Code-Interpreter.git (Code Interpreter)

        6.Availability: I confirm my availability to work as intern from 10 am to 7 pm for the next 3-6 months.
    
    
    Thank you for considering my application. Please let me know if you need any further information.
    
    Github-id-
        https://github.com/palakbansal8810
    Linkedin id-
        https://www.linkedin.com/in/palak-bansal-60166828a/ 

Best regards,
Palak Bansal'''
        
            sender = 'palakbansal8810@gmail.com'
            recipients = ['tech@themedius.ai'] 
            cc = ['hr@themedius.ai']

            with app.open_resource(screenshot_path) as fp:
                msg = Message(subject=subject, sender=sender, recipients=recipients,cc=cc)
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

            return ('message : Email sent successfully')
        
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return {'error':str(e)}

    else:
        print("Error occurred while filling Google Form and capturing screenshot.")
        return ('error filling Google Form and capturing screenshot.')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  