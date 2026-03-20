#!/bin/bash

# Configuration - Replace these with your actual credentials
export EMAIL_SENDER="your_email@example.com"
export EMAIL_RECEIVER="recipient@example.com"
export EMAIL_PASSWORD="your_app_password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"

# Check if placeholders are still present
if [[ "$EMAIL_SENDER" == "your_email@example.com" || "$EMAIL_PASSWORD" == "your_app_password" ]]; then
    echo "Error: Please update the placeholders in run_test_email.sh with your actual credentials."
    exit 1
fi

echo "Starting email test..."
python3 test_send_email.py
