from flask import Flask, render_template, request, url_for, redirect 
from email.message import EmailMessage
import smtplib
import lorem

app = Flask(__name__)

@app.route('/')
def home():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('home.html')

@app.route('/explore')
def explore():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('index.html')

@app.route('/index')
def index():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('index.html')

@app.route('/educational')
def educational():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('edu.html')

@app.route('/professional')
def professional():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('professional.html')

@app.route('/projects')
def projects():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('projects.html')

@app.route('/contact')
def contact():
    lorem_text = lorem.paragraph()  # Generates a random paragraph
    return render_template('contact.html')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']
        
        # Your email credentials
        yourEmail = 'chamodidilhara261@gmail.com'
        yourPassword = 'YOUR_APP_PASSWORD'  # Use an App Password instead of the real password

        try:
            # Set up SMTP connection
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(yourEmail, yourPassword)
            
            # Create email message
            msg = EmailMessage()
            msg.set_content(f"First Name: {name}\n"
                            f"Email: {email}\n"
                            f"Subject: {subject}\n"
                            f"Message: {message}")
            
            msg['To'] = yourEmail  # Send email to yourself
            msg['From'] = email  # Sender's email
            msg['Subject'] = subject 
            
            # Send email
            server.send_message(msg)
            print("Email sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {e}")

        finally:
            server.quit()  # Close the SMTP connection
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
