from twilio.rest import TwilioRestClient

account_sid = "ACe1b543d359f73a2e499e14946378d186" # Your Account SID from www.twilio.com/console
auth_token  = "c2180b0082fa7ba2f97a2b1d0cc137f5"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Congrats Vara Prasad Now you are part of Amazon as Data Engineer",
    to="+917729862404",    # Replace with your phone number
    from_="+17862456187") # Replace with your Twilio number

print(message.sid)
