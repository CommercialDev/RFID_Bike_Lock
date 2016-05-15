#!/usr/bin/python3
from tkinter import *
import time
import subprocess
import re
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

class Application(Frame):
    # auth_headers = {'X-ZUMO-APPLICATION': os.environ['RFID_APP_KEY']}


    def bike(self, bike):
        print("This is Bike", bike)
        self.checkout = Button(self, text = "Checkout", command = lambda: self.checkoutbike(bike), height = 100, width = 100)
        self.checkout.pack()
        self.bike1.destroy()
        self.bike2.destroy()

    def checkoutbike(self, bike):
        allowed = False
        print("Checking out bike", bike)
        # self.entrythingy = Entry()
        # self.RFID = Button(self, text = "Scan Your RFID Tag", height = 100, width = 100)
        # self.RFID.pack()
        print("Starting RFID Process")
        # here is the application variable
        # self.contents = StringVar()
        # set it to some value
        # self.contents.set("Scan your RFID")
        # print("Scan Your RFID Tag")
        # # tell the entry widget to watch this variable
        # self.entrythingy["textvariable"] = self.contents
        # self.entrythingy.pack()


        p = subprocess.Popen('/home/pi/libnfc-1.4.1/examples/nfc-poll', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ""
        for line in iter(p.stdout.readline, b''):
            print("inside loop")
            print(line)
            output = output + str(line)

        print("outside loop")
        p.stdout.close()
        self.checkout.destroy()
        # output = input()
        print(output)
        code = re.findall('target', output)
        print(code)
        # auth = requests.get('http://gwsmobileservice.azure-mobile.net/api/getuserinfo?rfid='+code, headers=auth_headers)
        # authjson = auth.json()[0]
        if code:
            allowed = True
            print("Authenticated")
            # self.RFID.destroy()
            # self.auth = Button(self, text = "Authenticated", height = 100, width = 100)
            # self.auth.pack()
        else:
            print("Not Authenticated")
            allowed = False
            # self.RFID.destroy()
            # self.auth = Button(self, text = "Not Authenticated", height = 100, width = 100)
            # self.auth.pack()
        if allowed:
            GPIO.output(18, True)
            print("Open the Lock")
            time.sleep(60)
            os.execv('RFID.py', sys.argv)
        else:
            GPIO.output(18, False)
            print("Do Not Open")
            os.execv('RFID.py', sys.argv)

    def createWidgets(self):
        self.bike1 = Button(self, text = "Bike 1", command = lambda: self.bike(1), height = 100, width = 100)
        self.bike1.pack({"side": "left"})
        self.bike2 = Button(self, text = "Bike 2", command = lambda: self.bike(2), height = 100, width = 100)
        self.bike2.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
# root.attributes("-fullscreen", True)
app = Application(master=root)
app.mainloop()
root.destroy()
