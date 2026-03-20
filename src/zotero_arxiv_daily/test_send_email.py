import os
from omegaconf import OmegaConf
from zotero_arxiv_daily.utils import send_email
from loguru import logger

def test_manual_send_email():
    # Load configuration from environment variables
    # You should set these in your environment before running the script:
    # export EMAIL_SENDER="your_email@example.com"
    # export EMAIL_RECEIVER="recipient@example.com"
    # export EMAIL_PASSWORD="your_password_or_app_password"
    # export SMTP_SERVER="smtp.example.com"
    # export SMTP_PORT=587
    
    sender = os.environ.get("EMAIL_SENDER")
    receiver = os.environ.get("EMAIL_RECEIVER")
    password = os.environ.get("EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))

    if not all([sender, receiver, password]):
        logger.error("Please set EMAIL_SENDER, EMAIL_RECEIVER, and EMAIL_PASSWORD environment variables.")
        return

    config = OmegaConf.create({
        "email": {
            "sender": sender,
            "receiver": receiver,
            "sender_password": password,
            "smtp_server": smtp_server,
            "smtp_port": smtp_port
        }
    })

    html_content = """
    <html>
        <body>
            <h1>Test Email from Zotero arXiv Daily</h1>
            <p>This is a test email to verify that the <code>send_email</code> function in <code>utils.py</code> is working correctly.</p>
            <p>Sent at: {}</p>
        </body>
    </html>
    """.format(os.popen('date').read().strip())

    logger.info(f"Attempting to send test email from {sender} to {receiver} via {smtp_server}:{smtp_port}...")
    
    try:
        send_email(config, html_content)
        logger.success("Email sent successfully!")
    except Exception as e:
        logger.exception(f"Failed to send email: {e}")

if __name__ == "__main__":
    test_manual_send_email()
