class Person:
    # vars
    name = ""
    dialogues = []
    description = ""
    greeting = ""
    dontUnderstandResponse = ""
    goodbye = ""

    # init
    def __init__(self, name, dialogues, description, greeting, dontUnderstandResponse, goodbye):
        self.name = name
        self.dialogues = dialogues
        self.description = description
        self.greeting = greeting
        self.dontUnderstandResponse = dontUnderstandResponse
        self.goodbye = goodbye

    # defs
    def getDialogues(self):
        return self.dialogues

    def getDescription(self):
        return self.description

    def getGreeting(self):
        return self.greeting

    def getDontUnderstandResponse(self):
        return self.dontUnderstandResponse

    def getGoodbye(self):
        return self.goodbye

class Dialogue:
    # vars
    flagNeeded = "" #flag.name
    subject = "" #trigger phrases - what the player brings up
    responses = "" #what gets said to the player
    noFlagResponse = "" #what gets said to the player if they do not have the flag
    flagsTriggered = [] #flags to be toggles once this dialogue happens

    # init
    def __init__(self, name):
        self.name = name

    # defs
    def getFlagNeeded(self):
        return self.flagNeeded

    def getSubject(self):
        return self.subject

    def getResponses(self):
        return self.responses

    def getNoFlagResponse(self):
        return self.noFlagResponse
