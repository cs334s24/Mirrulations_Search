import smtplib
import boto3
import json

def lambda_handler(event, context):
    try:
        # Extract input data from the event
        to_email = event['to_email']
        docket_id = event['docket_id']

        client = boto3.client('secretsmanager', region_name='us-east-1')
        secret_name = "TestingZipSystemLambda"
        response = client.get_secret_value(SecretId=secret_name)
        secret_string = response['SecretString']
        secret_data = json.loads(secret_string)
        
        # Extract sender email and password from SecretString
        sender_email = list(secret_data.keys())[0]
        sender_password = list(secret_data.values())[0]
        
        # Content
        subject = "Mirrulations Download Started!"
        message = f"Your download for docket {docket_id} has begun and will be done shortly. Hang tight!"
        
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Compose the email
            email = f'Subject: {subject}\n\n{message}'
            
            # Send the email
            server.sendmail(sender_email, to_email, email)
            
        return "Email sent successfully!"
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
        return f"Failed to send email: {e}"
