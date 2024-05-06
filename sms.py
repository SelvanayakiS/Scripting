from twilio.rest import Client

account_sid = 'Enter account sid'
auth_token = 'Enter Auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
      from_='+15704109022',
      body='My first Twilio msg :)',
      to='phone numer'
    )

print(message.sid)