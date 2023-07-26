import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "your email app password"
EMAIL_SENDER = "The email address that will send the message (needs to be gmail)"
EMAIL_RECEIVER = "The email address that will receive the message (doesn't need to be gmail) "


def send_email(image_path):
    print("send_email function started")
    # Creates an email object instance
    email_message = EmailMessage()
    email_message["Subject"] = "Something showed up in the camera!"
    email_message.set_content("Hey, we just saw something in the camera!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_SENDER, PASSWORD)
    gmail.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email(image_path="images/19.png")
