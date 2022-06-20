import smtplib as sm

s = sm.SMTP('smpt.gmail.com', 587) # Creating SMPT session , port number

s.starttls()  # TLS - Transfer Layer Security

sender_mail = input('Enter sender\'s mail')
password = input('Enter sender\'s password')

receiver_mail = input('Enter receiver\'s mail')
message = input('Enter message to be sent')

s.login(sender_mail, password)
s.sendmail(sender_mail, receiver_mail, message)

s.quit()  # Terminating the session
