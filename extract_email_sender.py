import re

# File paths
email_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\email.txt"
output_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\email-sender.txt"

# Read the email content
with open(email_file, "r", encoding="utf-8") as file:
    email_content = file.read()

# Regular expression to find the email address
email_pattern = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
match = re.search(email_pattern, email_content)

# If a match is found, write the email address to the output file
if match:
    sender_email = match.group(0)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(sender_email)
    print(f"Task A7 completed: Email sender extracted and saved to {output_file}")
else:
    print("No email address found in the email content.")
