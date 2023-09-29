import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'Put your account SID here'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'Put Your Auth Token here'
client = Client(account_sid, auth_token)

#Or otherwise, if you use their code, once you run the script, it will ask the Account SID and Auth code on the terminal

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+XXXXXXXXXXXX',
                     to='+91XXXXXXXXXX'
                 )

print(message.sid)