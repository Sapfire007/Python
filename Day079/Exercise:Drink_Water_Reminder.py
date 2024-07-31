"""
Objective:
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system
"""
# This program is for windows
from plyer import notification
import time

if __name__=="__main__":
    while True:
        notification.notify(title ='Time to Hydrate!',app_name="Drink up!" ,message='Kindly have a drink of water; it has been 2 hours.',timeout=5 )
        time.sleep(3600)