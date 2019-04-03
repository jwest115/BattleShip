class Ship_Data:
    def __init__(self, id, name, top_x, top_y, bottom_x, bottom_y, valid_position):
        self.id = id
        self.name = name
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y
        self.valid_position = valid_position

        print("Ship added with id ", self.id, " ", self.name, " top x ", self.top_x, " top y ", self.top_y, " bottom x " , self.bottom_x," bottom y ", self.bottom_y)