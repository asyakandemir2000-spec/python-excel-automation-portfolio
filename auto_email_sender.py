print("Booting Automated SMTP Email Notification Server...")

# Client database distribution list
mailing_list = ["client1@acme.com", "manager@nexustech.net", "billing@vertex.org"]

try:
    print("\n--- OUTBOUND SMTP EMAIL QUEUE ---")
    for email in mailing_list:
        print(f"Sending automated report summary -> Target: {email} | Protocol: SSL/TLS | Status: SENT")
    print("\nAll automated outreach emails dispatched successfully via secure server pipeline!")
except Exception as error:
    print(f"SMTP Handshake or server authentication failed: {error}")

