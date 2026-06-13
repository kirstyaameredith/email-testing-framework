from src.email_sender import send_email

def test_email_contains_html(mailpit):
    test_email = "kirsty@example.com"

    send_email(test_email, html=True)

    msg = mailpit.wait_for_email(test_email)

    # Mailpit exposes HTML content under "HTML"
    assert "<h1>" in msg["HTML"]
    assert "Hello from automated tests!" in msg["HTML"]
