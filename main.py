import email, smtplib, ssl
from hidden import password, user
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from template import set_name
import csv

def send_mail(name, receiver_email):
    sender_email = "lamendozac@unal.edu.co"
    receiver_email = "lamendozac@unal.edu.co"
    #password = input("Type your password and press enter:")
    subject = "Vacante: desarrollador en Python"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Set name within both plain/html templates
    template_text, template_html = set_name(name)
    
    # Turn body into plain/html MIMEText objects
    part1 = MIMEText(template_text, "plain")
    part2 = MIMEText(template_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    #message.attach(part1)
    message.attach(part2)

    filename = "files/1067957571_CVR_English_24Oct2022.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    #text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    

def run():
    with open("emails.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            print(f"Sending email to {name}")
            send_mail(name, email)

if __name__ == '__main__':
    run()