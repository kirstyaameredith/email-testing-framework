from src.email_sender import send_email

def test_email_contains_active_header(mailpit):
    test_email = "kirsty@example.com"

    send_email(test_email, active=True)

    msg = mailpit.wait_for_email(test_email)

    # We now check the body for the active flag
    assert "X-Active: true" in msg["Text"]
