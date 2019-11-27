from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

    # set window attributes
        self.title("Song Maker")
        self.configure(padx=10, pady=10)

    # add components
        self.__add_heading_label()
        self.__add_subheading_label()
        self.__add_lyric_entry()
        self.__add_add_button()
        self.__add_subheading_label2()
        self.__add_listbox()

    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        # layout
        self.heading_label.grid(row=0, column=0)
        # style
        self.heading_label.configure(   font="Arial 24", 
                                        text="Song Maker")

    def __add_subheading_label(self):
        self.subheading_label = Label()
        self.subheading_label.grid(row=1, column=0)
        self.subheading_label.configure(font="Arial 16",text="Lyric to add:")
    
    def __add_lyric_entry(self):
        self.lyric_entry = Entry()
        self.lyric_entry.grid(row=2, column=0, sticky=N+E+S+W, pady=10)
    
    def __add_add_button(self):
        self.add_button = Button()
        self.add_button.grid(row=2, column=1)
        self.add_button.configure(text="Add")
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_2_subheading_label(self):
        self.subheading_label2 = Label()
        self.subheading_label2.grid(row=3, column=0)
        self.subheading_label2.configure(font="Arial 16", text="Lyrics:")

    def __add_listbox(self):
        self.listbox = Listbox()
        self.listbox.grid(row=4, column=0)
    