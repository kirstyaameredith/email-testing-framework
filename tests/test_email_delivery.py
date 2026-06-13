from src.email_sender import send_email

def test_email_is_sent_and_received(mailpit):
    test_email = "kirsty@example.com"

    send_email(test_email)

    msg = mailpit.wait_for_email(test_email)

    assert msg["Subject"] == "Test Email"
    assert "Hello from automated tests!" in msg["Text"]
