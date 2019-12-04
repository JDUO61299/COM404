class Gui(Tk):
    
    def __init__(self):
        super().__init__()

# load resources
        self.ambulance_image = PhotoImage(file="C:/Users/4DUOJ51/Downloads/ambulance.gif")
        self.bike_image = PhotoImage(file="C:/Users/4DUOJ51/Downloads/bike.gif")
        self.plane_image = PhotoImage(file="C:/Users/4DUOJ51/Downloads/plane.gif")
        
 
 # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
        
    def __add_ambulance_image_label(self):
        pass

    def __add_bike_image_label(self):
        pass
 
    def __add_plane_image_label(self):
        pass