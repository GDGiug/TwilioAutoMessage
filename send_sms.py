import twilio.rest
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc9f7213eced0b9a96dc37806cf229bfb"
# Your Auth Token from twilio.com/console
auth_token = "252bf3928d9b40fd59d40a7f394aa0bf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16479820220",
    from_="+13433384671",
    body="Lmfao")

print(message.sid)