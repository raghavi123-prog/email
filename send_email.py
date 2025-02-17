import sendgrid  
from sendgrid.helpers.mail import Mail
import pandas as pd  

sg = sendgrid.SendGridAPIClient(api_key="YOUR_SENDGRID_API_KEY")  
df = pd.read_csv("emails.csv")  

for index, row in df.iterrows():  
    message = Mail(  
        from_email="your-email@example.com",  
        to_emails=row['Email'],  
        subject=row['Subject'],  
        html_content=row['Message']  
    )  
    sg.send(message)  

print("Emails sent successfully!")  
