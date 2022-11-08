import email, smtplib, ssl
from hidden import password, user
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from func.template import set_name

def send_mail(name, sender_email, receiver_email, subject):
    
    #password = input("Type your password and press enter:")
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Set name within both plain/html templates
    template_text, template_html = set_name(name)
    
    # Turn body into plain/html MIMEText objects
    #part1 = MIMEText(template_text, "plain")
    part2 = MIMEText(template_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    #message.attach(part1)
    message.attach(part2)

    # files to attach
    files = ["files/1067957571_CVR_English_24Oct2022.pdf", "files/1067957571_CVR_Español_10Oct2022.pdf"]
    
    for file in files:  # add files to the message       
        # Open PDF file in binary mode
        try:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(file,"rb").read())  

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                "attachment", filename=file
            )
            # Add attachment to message
            message.attach(part)
        except:
            print(f"We could not attach the file: {file}")

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
 