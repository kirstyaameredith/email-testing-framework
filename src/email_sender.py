import smtplib
from email.message import EmailMessage

def send_email(to_address, active=False, html=False):
    msg = EmailMessage()
    msg["From"] = "no-reply@test.com"
    msg["To"] = to_address
    msg["Subject"] = "Test Email"

    body = "Hello from automated tests!\n"

    if active:
        body = "X-Active: true\n" + body

    if html:
        msg.set_content(body)
        msg.add_alternative(
            f"<html><body><h1>{body}</h1></body></html>",
            subtype="html"
        )
    else:
        msg.set_content(body)

    with smtplib.SMTP("localhost", 1025) as smtp:
        smtp.send_message(msg)


def send_email_with_attachment(to_address, filename, content):
    """
    Sends an email with a single attachment.
    `content` must be bytes.
    """
    msg = EmailMessage()
    msg["From"] = "no-reply@test.com"
    msg["To"] = to_address
    msg["Subject"] = "Email With Attachment"

    msg.set_content("Please see attached file.")

    msg.add_attachment(
        content,
        maintype="text",
        subtype="plain",
        filename=filename
    )

    with smtplib.SMTP("localhost", 1025) as smtp:
        smtp.send_message(msg)
