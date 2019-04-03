from tkinter import *
from PIL import Image, ImageTk
from BattleShip.Tile_Coordinate import Tile_Coordinate
from BattleShip.Ship_Data import Ship_Data


class GUI_Board():
    def __init__(self):
        self.window = Tk()
        self.window.title("BattleShip")
        self.window.config(bg="black")
        self.window.geometry("1100x850")
        # list of Ship_Data objects for each ship
        # keep track of all the ship names, coordinates, and check to see if is currenlty placed in a valid position
        self.ship_coordinates = []
        self.add_logo()

        # create canvas for ships to be placed
        # 4cbdff
        self.canvas = Canvas(self.window, width=1050, height=600, bg="black", highlightbackground="black")

        self.path0 = "../images/ship-569.png"
        self.load0 = Image.open(self.path0)
        self.load0 = self.load0.resize((1050,750), Image.ANTIALIAS)
        self.image0 = ImageTk.PhotoImage(self.load0)
        self.canvas.create_image(500, 400, image=self.image0)
        self.canvas.place(x=20, y=200)


        self.image_path1 = "../images/board2.png"
        self.load1 = Image.open(self.image_path1)
        self.load1 = self.load1.resize((600, 600), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.load1)
        self.canvas.create_image(700, 300, image=self.image1)

        self.tile_coordinates = []
        x1 = 475
        y1 = 81
        x2 = 523
        y2 = 126
        for i in range(10):
            for j in range(10):
                coord = Tile_Coordinate(i, j, x1, y1, x2, y2)
                self.tile_coordinates.append(coord)
                self.canvas.create_rectangle((x1, y1, x2, y2), fill = "red")
                if j >= 7:
                    x1 += 51
                    x2 += 52
                elif j >= 3:
                    x1 += 51
                    x2 += 50
                else:
                    x1 += 52
                    x2 += 52
            if i == 8:
                y1 += 50
                y2 += 50
                x1 = 476
                x2 = 523  
            elif i >= 5:
                y1 += 51
                y2 += 51
                x1 = 476
                x2 = 523
            else:
                x1 = 476
                x2 = 523
                y1 += 50
                y2 += 50


        # Keeps track of each ship that would be moved
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.create_ships()

        for coord in self.tile_coordinates:
            print ("x1 " + str(coord.x1) + " " + "y1 " + str(coord.y1) + " " + "x2 " + str(coord.x2) + "  y2  " + str(coord.y2) + " " + str(coord.gridx) + " " + str(coord.gridy))

        self.window.bindtags("ButtonPress-1")

        self.canvas.tag_bind("ship", "<ButtonPress-1>", self.on_ship_press)
        self.canvas.tag_bind("ship", "<ButtonRelease-1>", self.on_ship_release)
        self.canvas.tag_bind("ship", "<B1-Motion>", self.on_ship_motion)
        
        self.window.mainloop()

    def add_logo(self):
        image_path2 = "../images/battleship-logo.jpg"
        load2 = Image.open(image_path2)
        self.render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self.window, image=self.render2, bg=self.window['bg'])
        img2.place(x=250, y=0)

    def create_ships(self):
        self.path = "../images/"
        self.ship_images = ["aircraft carrier.png","battleship.png","cruiser.png","destroyer.png","submarine.png"]
        # sizing for the ship images
        self.ship_dictionary = {103 : (30, 225), 104 : (35, 175), 105 : (25, 120), 106 : (35, 75), 107 : (35, 115)}
        self.ship_sizes = [(30, 225), (35, 175), (25, 120), (35, 75), (35, 115)]
#         self.ship_sizes_y = [230, 190, 155, 90, 145]
        # List of ships stored to access them when figuring out which one is being moved
        self.ship_names = []

        i=0
        x=100
        y=100
        for ship in self.ship_images:
            self.image_path = self.path+ship
            self.load = Image.open(self.image_path)
            self.load = self.load.resize((self.ship_sizes[i][0], self.ship_sizes[i][1]), Image.ANTIALIAS)
            self.ship_names.insert(i, ImageTk.PhotoImage(self.load))
            # get the ship by splitting the image file name
            file_name = self.ship_images[i].split(".")
            name = file_name[0]
            self.ship = self.canvas.create_image(x, y, image=self.ship_names.__getitem__(i), tags="ship")
            # add the ship data to the ship_coordinates list
            self.ship_coordinates.append(Ship_Data(self.ship, name, 0, 0, 0, 0, False))
            
            if y == 500 and x == 100:
                x += 130
                y = 50

            y+=200
            i+=1

    # Keeps track of the position when a particular ship is clicked
        #Track starts from item 2
    def on_ship_press(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    # Keeps track of the position when a particular ship is released
    def on_ship_release(self, event):
        coord = self.canvas.coords(self._drag_data["item"])
        print("x " + str(coord[0]) + "  y " + str(coord[1] - 100))
        ship_dimensions = self.ship_dictionary[self._drag_data["item"]]
        ship_height = ship_dimensions[1]
        self.check_ship_coordinates(self._drag_data["item"], coord[0], coord[1] - (ship_height / 2), coord[1] + (ship_height / 2))
        # make sure all ships are in valid positions then let the game continue
        count = 0
        for ship in self.ship_coordinates:
            print(ship.valid_position)
            if ship.valid_position == True:
                count += 1
            else:
                count = 0
        if count == 5:
            print("All ships are valid, continue!")
        else:
            print("Please drag all ships to a valid position")
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0


    # Keeps track of the motion of a particular ship
    def on_ship_motion(self, event):
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

        # New position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        
    # takes in the x, top y, and bottom y coordinates of the dragged ship
    def check_ship_coordinates(self, ship_id, ship_x, ship_y, ship_y2):
        head_x = None
        head_y = None
        tail_x = None
        tail_y = None
        
        print("ship id is " + str(ship_id))
        # go through list of grid coordinates to see if a ship is within bounds of the grid
        for coord in self.tile_coordinates:
            # check to see if ship's head is within bounds
            if ship_x >= coord.x1 and ship_x <= coord.x2 and ship_y >= coord.y1 and ship_y <= coord.y2:
                print("head coordinate is " + str(coord.gridx) + " " + str(coord.gridy))
                head_x = coord.gridx
                head_y = coord.gridy
                # if head is in bounds then check to see if tail is within bounds
                for coord2 in self.tile_coordinates:
                    if ship_x >= coord2.x1 and ship_x <= coord2.x2 and ship_y2 >= coord2.y1 and ship_y2 <= coord2.y2:
                        print("tail coordinate is " + str(coord2.gridx) + " " + str(coord2.gridy))
                        tail_x = coord.gridx
                        tail_y = coord.gridy
        ship = None
        for s in self.ship_coordinates:
            if ship_id == s.id:
                ship = s
        # if the ship was placed in a valid position on the grid board then return the top x and y coordinates and the bottom x and y coordinates (ex: 0,0 and 0,5)
        # set all the parameters in the Ship_Data object
        if head_x != None and head_y != None and tail_x != None and tail_y != None:
            ship.top_x = head_x
            ship.top_y = head_y
            ship.bottom_x = tail_x
            ship.bottom_y = tail_y
            ship.valid_position = True
#             return (head_x, head_y, tail_x, tail_y)
        # prompt user to find a valid position
        # set all the parameters in the Ship_Data object
        # make valid_position False, since the ship is not placed correctly
        else:
            ship.top_x = head_x
            ship.top_y = head_y
            ship.bottom_x = tail_x
            ship.bottom_y = tail_y
            ship.valid_position = False
            print("Please drag the ship to a valid position")
        
                
        

GUI_Board()