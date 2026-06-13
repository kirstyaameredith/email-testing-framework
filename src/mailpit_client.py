import time
import requests

class MailpitClient:
    def __init__(self, host="http://localhost:8025"):
        self.host = host

    def clear_inbox(self):
        """Delete all messages in Mailpit before each test."""
        resp = requests.delete(f"{self.host}/api/v1/messages")
        resp.raise_for_status()

    def wait_for_email(self, to, timeout=15):
        """
        Poll Mailpit until an email addressed to `to` appears.
        Uses the REST API directly (stable, reliable).
        """
        for _ in range(timeout):
            # 1. Get message summaries
            resp = requests.get(f"{self.host}/api/v1/messages")
            resp.raise_for_status()
            messages = resp.json().get("messages", [])

            for summary in messages:
                # Extract recipients
                recipients = [r.get("Address") for r in summary.get("To", [])]

                if to in recipients:
                    # 2. Fetch full message
                    msg_id = summary["ID"]
                    full = requests.get(f"{self.host}/api/v1/message/{msg_id}")
                    full.raise_for_status()
                    return full.json()

            time.sleep(1)

        raise AssertionError(f"Email to {to} not received within timeout")
