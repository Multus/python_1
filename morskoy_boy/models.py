class User(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Field(object):
    def __init__(self, size, ships, pice, length, high):
        self.size = size
        self.ships = ships
        self.pice = '~'
        self.high = high
        self.length = length

class Ship(object):
    def __init__(self, size, location, x1, x2, y1, y2, fragment):
        self.size = size
        self.x1 = x1
        self.x1 = x2
        self.x1 = y1
        self.x1 = y2
        self.pice = '#'
        self.location = None
        if Shot.location == self.location
            self.fragment = '*'
class Shot(object):
    def __init__(self,shooter,location,type, x,y, view):
        self.shooter = User.name
        self.location = [x,y]
        self.type = type
        self.view = view
        if type == False:
            self.view = 'O'
            else
            self.view = '*'



