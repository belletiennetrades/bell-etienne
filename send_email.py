import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_emails, sender_email, app_password):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message["From"] = f"Bell-Etienne Digital Handyman <{sender_email}>"
        message["To"] = ", ".join(to_emails)
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        # Login
        server.login(sender_email, app_password)
        
        # Send
        text = message.as_string()
        server.sendmail(sender_email, to_emails, text)
        server.quit()
        
        print(f"Successfully sent email to: {', '.join(to_emails)}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 send_email.py 'Subject' 'Body' 'recipient1,recipient2' 'sender@gmail.com' 'app_password'")
        sys.exit(1)
        
    subj = sys.argv[1]
    body = sys.argv[2]
    recipients = sys.argv[3].split(",")
    sender = sys.argv[4]
    password = sys.argv[5]
    
    send_email(subj, body, recipients, sender, password)
