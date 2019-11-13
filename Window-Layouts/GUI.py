from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Gui")
        self.configure(bg="#eee",
        height=500, 
        width=500)

        self.add_heading_label()
        self.add_subheading_label()
        self.add_email_frame()
        self.add_email_entry()
        self.add_caption_label()
        self.add_subscribe_button()


    def add_heading_label(self):   
        self.heading_label = Label()
        self.heading_label.pack()

        self.heading_label.configure(font="Arial 24",
                        text="Receive Our Newsletter")

    def add_subheading_label(self):
        self.subheading_label = Label()
        self.subheading_label.pack()

        self.subheading_label.configure(font="Arial 12",
                        text="please enter your email below to receive our newsletter")

    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
    
    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)

    def add_caption_label(self):
        self.caption_label = Label(self.email_frame)
        self.caption_label.pack(side=LEFT)

        self.caption_label.configure(font="Arial 10",
                        text="Email:")

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.pack()

        self.subscribe_button.configure(font="Arial 14",
                        text="Subscribe")

    
