from func.mail import send_mail
import csv

def run():
    with open("emails.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        subject = "Vacante: desarrollador en Python"
        sender_email = "lamendozac@unal.edu.co"
        
        for name, receiver_email  in reader:
            print(f"Sending email to {name}")
            try:
                send_mail(name, sender_email, receiver_email, subject)
            except:
                "The email was sended"

if __name__ == '__main__':
    run()