#!/bin/python

import pyttsx3
import pywhatkit
import os
import time

engine = pyttsx3.init()
engine.setProperty("voice", "english+f3")
engine.setProperty("rate", 140)


cmd = "acpi"  # command to get battery status
# os commad to store data in variable data and then send it to whatsapp
termdata = os.popen(cmd).read()

# read the data user configured
user_data = {
    "number": "",  # enter your number with country code
    "msg": f"{termdata}",  # enter your message here
}  # enter numver with country code
# def status():

# send data to whatsapp
def whatsapp():
    try:
        pywhatkit.sendwhatmsg_instantly(
            f"{user_data['number']}", f"{user_data['msg']}", 6, True
        )
        engine.say("Master Check your Whatsapp")
        engine.runAndWait()
    except:
        print("Please check your user_data")
        os.system("pwd")
        engine.say("Message not sent")
        engine.runAndWait()


# start the program
def main():
    if True:
        whatsapp()
        time.sleep(2)
        os.system("poweroff")
