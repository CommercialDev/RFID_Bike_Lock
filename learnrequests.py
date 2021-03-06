from tkinter import *
import time
import subprocess
import re
auth_headers = {'X-ZUMO-APPLICATION': os.environ['RFID_APP_KEY']}

class Application(Frame):
    auth_headers = {'X-ZUMO-APPLICATION': os.environ['RFID_APP_KEY']}

    def bike(self, bike):
        print("This is Bike", bike)
        self.checkout = Button(self, text = "Checkout", command = lambda: self.checkoutbike(bike))
        self.checkout.pack()
        self.bike1.destroy()
        self.bike2.destroy()

    def checkoutbike(self, bike):
        allowed = False
        print("Checking out bike", bike)
        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.checkout.destroy()
        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("Scan your RFID")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # p = subprocess.Popen('./test.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # time.sleep(10)
        # output = str(p.stdout.readline())
        output = input()
        code = re.findall('\d+', output)[0]
        auth = requests.get('http://gwsmobileservice.azure-mobile.net/api/getuserinfo?rfid='+code, headers=auth_headers)
        authjson = auth.json()[0]
        if 'FirstName' in authjson:
            allowed = True
            print("Authenticated")
        else:
            print("Not Authenticated")
            allowed = False
        if allowed:
            print("Open the Lock")
            root.destroy()

    def createWidgets(self):
        self.bike1 = Button(self, text = "Bike 1", command = lambda: self.bike(1))

        self.bike1.pack({"side": "left"})

        self.bike2 = Button(self, text = "Bike 2", command = lambda: self.bike(2))

        self.bike2.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
