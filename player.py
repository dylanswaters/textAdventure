class Player:
    # vars
    name = ""
    inventory = []
    roomLocation = None
    flagList = []

    # init
    def __init__(self, name, flags):
        self.name = name
        self.inventory = []
        self.roomLocation = None
        self.flagList = flags

    # defs
    def setRoom(self, room):
        self.roomLocation = room

    def toggleFlag(self, name):
        return self.flagList[name].toggleFlag()

    def checkFlag(self, name)
        return self.flagList[name].getActive()

    def addToInv(self, item):
        self.inventory.append(item)

    def removeFromInv(self, item):
        if item in inventory:
            self.inventory.remove(item)
            return True
        return False

    def checkInv(self, item):
        if item in inventory:
            return True
        return False

    def getName(self):
        return self.name

class Flag:
    # vars
    name = ""
    active = False
    actions = []

    # init
    def __init__(self, name, actions):
        self.name = name
        self.active = False
        self.actions = actions

    # defs
    def getActive(self):
        return self.active

    def toggleFlag(self):
        if(self.active = False):
            self.active = True
        else:
            self.active = False
        return self.active

    def getActions(self):
        return self.actions

class Action:
    # vars
    name = "" # name of action
    type = "" # type of thing the action will do
    target = "" # the target of the action
    result = "" # the result of the action
    flagTriggers = [] # list of flag names

    # init
    def __init__(self, name, type, target, result, triggers):
        self.name = name
        self.type = type
        self.target = target
        self.result = result
        self.flagTriggers = triggers

    # defs
    def getType(self):
        return self.type

    def getTarget(self):
        return self.target

    def getResult(self):
        return self.result

    def getTriggers(self):
        return self.flagTriggers

    def toggleFlags(self, player):
        for each flag in flagTriggers:
            player.toggleFlag(flag)
