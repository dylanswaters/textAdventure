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
    def getDescription(self):
        return self.description

    def getUsableOn(self):
        return self.usableOn

class UsableOn:
    # vars
    name = ""
    usedOn = "" #item.name
    flagNeeded = "" #flag.name
    flagTriggered = "" #flag.name
    resultText = ""

    # init
    def __init__(self, name, usedOn, flagNeeded, flagTriggered, resultText):
        self.name = name
        self.usedOn = usedOn
        self.flagNeeded = flagNeeded
        self.flagTriggered = flagTriggered
        self.resultText = resultText

    # defs
    def getUsedOn(self):
        return self.usedOn

    def getFlagNeeded(self):
        return self.flagNeeded

    def getFlagTriggered(self):
        return self.flagTriggered

    def getResultText(self):
        return self.resultText
