import pywhatkit

phone = input("Enter phone number (+countrycode): ")
msg = input("Enter message: ")
hour = int(input("Enter hour (24-hour format): "))
minute = int(input("Enter minute: "))

pywhatkit.sendwhatmsg(phone, msg, hour, minute)

print("Message scheduled successfully!")
