# Flask Application for Automating Form Submission and Sending Emails

This project automates the process of filling out a Google Form using Selenium, captures a screenshot of the confirmation page, and sends an email with the screenshot of confirmation and the things mentioned in assignment.

## Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/palakbansal8810/Medius-Technologies-Private-Limited.git
   cd form_filling
   ```

2. **Install Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Mail and Passwords**:
   In .env --  
   Replace *YOUR_GMAIL_ID* with your gmail id and
   Replace *PASSWORD* with your password

*Note- if two-factor authentication is enabled for your gmail account, make a app-specific password, then replace *PASSWORD* with that password, *if not, use your gmail password.* 

4. **Run the app**:
   ```bash
   python app.py
   ```

5.  Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Application Components

### Flask App Initialization

- **Configurations**: The application initializes with Flask configurations for the SMTP server, port, and Gmail credentials.

### Google Form Automation with Selenium

- **Form Filling**: A function `filling_google_form` uses Selenium WebDriver to navigate to a Google Form, fill in the required details, and submit the form.
- **Screenshot Capture**: After form submission, a screenshot of the confirmation page is taken and saved locally.

### Email Sending Functionality

- **Email Preparation**: The `send_email` route triggers the form-filling function, prepares an email with the screenshot and required documents.
- **Attachment Handling**: The email includes the screenshot taken during form submission and a pre-existing PDF file named `resume.pdf`.

### Web Interface

- **Index Route**: The application serves an HTML page(index.html in templates folder) at the root URL (`/`).
- **Email Sending**: The email sending functionality is triggered via a POST request to the `/send_email` endpoint.

