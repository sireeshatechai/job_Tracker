# notifier.py - email digest
import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

import db

load_dotenv()


def build_digest(days=7):
    counts = db.get_stats()
    followups = db.get_followups(days)
    lines = ["Job tracker digest", "", "Applications by status:"]
    for status in db.STATUSES:
        lines.append(f"  {status:<10} {counts.get(status, 0)}")
    lines.append("")
    if followups:
        lines.append(f"Follow up on these ({days}+ days without an update):")
        for r in followups:
            lines.append(
                f"  #{r['id']} {r['company']} - {r['role']} "
                f"(last update {r['last_update']})"
            )
    else:
        lines.append("No follow-ups needed today.")
    return "\n".join(lines)


def send_digest(days=7):
    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_APP_PASSWORD")
    recipient = os.getenv("EMAIL_TO", sender)
    if not sender or not password:
        raise RuntimeError("Set EMAIL_ADDRESS and EMAIL_APP_PASSWORD in your .env file.")

    msg = EmailMessage()
    msg["Subject"] = "Job tracker daily digest"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(build_digest(days))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)