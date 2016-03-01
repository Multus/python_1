class User(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Field(object):
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships

class Ship(object):
    def __init__(self, lenght, location,):
        self.length = length
        self.location = None
class Shot(object):
    def __init__(self,shooter,location,type):
        self.shooter = User.name
        self.location = [x,y]
        self.type = type



