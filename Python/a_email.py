# import csv
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Network Configuration
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# SENDER_EMAIL = "bajrangcrasher@gmail.com"
# SENDER_PASSWORD = "ubmjpervdnyfnoah" # Your 16-character app password
# print("Connecting to the mail server on port 587...")
# # 2. Use standard SMTP instead of SMTP_SSL
# with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    
#     # 3. Say hello to the server (Network Handshake)
#     server.ehlo() 
    
#     print("Upgrading connection to secure TLS encryption...")
#     # 4. Manually secure the socket connection
#     server.starttls() 
    
#     # 5. Say hello again now that the connection is secure
#     server.ehlo() 
    
#     print("Logging in...")
#     server.login(SENDER_EMAIL, SENDER_PASSWORD)
#     print("Logged in successfully!\n")

#     # Open and read the CSV file
#     with open("mails.csv", mode="r") as file:
#         # csv.DictReader maps the first row (headers) to keys in a dictionary
#         reader = csv.DictReader(file)
        
#         for row in reader:
#             # Extract data dynamically from the current row
#             name = row["Name"]
#             email = row["Email"]
#             topic = row["Topic"]
            
#             # Create a fresh email packet for this person
#             message = MIMEMultipart()
#             message["From"] = SENDER_EMAIL
#             message["To"] = email
#             message["Subject"] = f"Hey {name}, custom update on {topic}!"
            
#             # Personalize the text body
#             body = f"""Hi {name},

# This is an automated message. I saw you were interested in {topic}, 
# so I wanted to send you this custom update directly from my network script.

# Talk soon,
# Your Python System
# """
#             message.attach(MIMEText(body, "plain"))
            
#             # Send the email packet over the open socket
#             print(f"Sending network packet to {name} ({email})...")
#             server.sendmail(SENDER_EMAIL, email, message.as_string())
#             print(f"✅ Successfully sent to {name}!\n")

# print("✨ All emails from the spreadsheet have been delivered!")













import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "bajrangcrasher@gmail.com"
SENDER_PASSWORD = "ubmjpervdnyfnoah" 

print("Connecting to the mail server...")
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("Logged in successfully!\n")

    with open("mails.csv", mode="r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row["Name"]
            email = row["Email"]
            topic = row["Topic"]
            
            message = MIMEMultipart()
            message["From"] = SENDER_EMAIL
            message["To"] = email
            message["Subject"] = f"Exclusive Update: {topic} ✨"
            
            # --- THE FANCY HTML BODY ---
            # We use inline CSS styles to design the email nicely
            html_body = f"""
            <html>
                <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333333; line-height: 1.6; background-color: #f9f9f9; padding: 20px;">
                    <div style="max-width: 600px; margin: 0 auto; background: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #4CAF50;">
                        
                        <h2 style="color: #4CAF50; margin-top: 0;">Hey {name}! 👋</h2>
                        
                        <p>This isn't your average boring automated email. Your Python network script just leveled up!</p>
                        
                        <p>We saw that you are tracking updates for <strong>{topic}</strong>. Here is your personalized dashboard portal:</p>
                        
                        <div style="text-align: center; margin: 30px 0;">
                            <a href="https://www.py4e.com" style="background-color: #4CAF50; color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 5px; display: inline-block; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                Access {topic} Hub
                            </a>
                        </div>
                        
                        <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 20px 0;">
                        
                        <p style="font-size: 12px; color: #777777; text-align: center;">
                            Sent automatically via Python Socket Automation.<br>
                            To stop receiving these, go edit your script! 😉
                        </p>
                    </div>
                </body>
            </html>
            """
            
            # CRITICAL CHANGE: Change "plain" to "html"
            message.attach(MIMEText(html_body, "html"))
            
            print(f"Sending fancy network packet to {name}...")
            server.sendmail(SENDER_EMAIL, email, message.as_string())
            print(f"✅ Delivered to {name}!\n")

print("✨ All fancy emails delivered successfully!")






