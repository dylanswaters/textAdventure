class Room:
    # vars
    name = ""
    description = ""
    items = [] # list of item names
    people = [] # list of people names
    objects = [] # list of object names
    exits = []

    # init
    def __init__(self, name):
        self.name = name

    # defs
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getItems(self):
        return self.items

    def getPeople(self):
        return self.people

    def getObjects(self):
        return self.objects

    def getExits(self):
        return self.exits

class Object:
    # vars
    name = ""
    description = ""
    rejectPickupText = ""

    # init
    def __init__(self, name, description, rejectPickupText):
        self.name = name
        self.description = description
        self.rejectPickupText = rejectPickupText

    # defs
    def __str__(self):
        return self.name

class Exit:
    # vars
    door = False
    openItemName = ""
    description = ""
    direction = ""
    roomResult = "" #room name

    # init
    def __init__(self, door, openItemName, description, direction, roomResult):
        self.door = door
        self.openItemName = openItemName
        self.description = description
        self.direction = direction
        self.roomResult = roomResult

    # defs
    # returns 1 if unlocked, 0 if locked, -1 if failed
    def toggleLock(self, item):
        if(item.getName() = self.openItemName):
            if(self.door = False):
                self.door = True
                return 1
            else:
                self.door = False
                return 0
        else:
            return -1

    def getDescription(self):
        return self.description

    def getDirection(self):
        return self.direction

    def getRoomResult(self):
        return self.roomResult
