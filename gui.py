from tkinter import *

class GUI(object):
    def changeLabel(self):
        text = "You have entered " + self.someName.get()
        self.labelText.set(text)
        self.someName.delete(0, END)
        self.someName.insert(0, "You've clicked!")
        self.personNumber = 0

    def __init__(self):
        app = Tk()
        app.title("GUI Test")
        app.geometry('450x300')

        self.labelText = StringVar()
        self.labelText.set("PersonNumber")
        label1 = Label(app, textvariable=self.labelText, height=4)
        label1.pack()

        userInput = StringVar(None)
        self.someName = Entry(app, textvariable=userInput)
        self.someName.pack()

        button1 = Button(app, text="Click Here", width=20,command=self.changeLabel)
        button1.pack(side='bottom',padx=15,pady=15)

        app.mainloop()

GUI() #calling the class to run