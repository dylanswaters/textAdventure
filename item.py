class Item:
    # vars
    name = ""
    description = ""
    usableOn = []

    # init
    def __init__(self, name, description, usableOn):
        self.name = name
        self.description = description
        self.usableOn = usableOn

    # defs
    def

class UsableOn:
    # vars
    name = ""

    # init
    def __init__(self, name):
        self.name = name

    # defs
    def __str__(self):
        return self.name
