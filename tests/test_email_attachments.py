from src.email_sender import send_email_with_attachment

def test_email_contains_attachment(mailpit):
    test_email = "kirsty@example.com"

    send_email_with_attachment(
        test_email,
        filename="test.txt",
        content=b"Hello attachment"
    )

    msg = mailpit.wait_for_email(test_email)

    attachments = msg["Attachments"]

    assert len(attachments) == 1
    assert attachments[0]["FileName"] == "test.txt"
