from item import *
from person import *
from room import *
from player import *
from phrases import *

def mainMenu(input):
    if(input == "new"):

# return true is grammar is  all good
def checkValidStatement(input):
    input.split(" ")
    for i in input:
        
    # transform variables
    # compare to known phrases
    # return if valid
    pass

# should return
def checkContextStatement(input):
    pass

def processAction(action):
    # name = "" # name of action
    # description = ""
    # type = "" # type of thing the action will do
    # target = "" # the target of the action
    # flagTriggers = [] # list of flag names
    return

def inDialogue(player, person):
    print person.getGreeting()
    dialogueBuffer = ""
    while(dialogueBuffer != "goodbye"):
        # check for greeting
        if(dialogueBuffer in greetings):
            print person.getGreeting()
            continue
        # cycle through all subjects
        for d in person.getDialogues():
            # check for subject
            if(dialogueBuffer in d.getSubject()):
                # check for flag
                if(d.getFlagNeeded() != None):
                    if(player.checkFlag(d.getFlagNeeded()) == True):
                        print d.getResponse()
                    else:
                        print d.noFlagResponse()
                else:
                    print d.getResponse()
            else:
                print person.getDontUnderstandResponse()
    print(person.getGoodbye())
    print()
    print("dialogue with " + person.getName() + " has ended")


def main():
    mainMenu = True
    print("type 'new' for a new game, 'load' to load, and 'quit' to quit")
    inputBuffer = ""
    while(inputBuffer != "q"):
        if(mainMenu == True):
            mainMenu(inputBuffer)
        else:
            if(checkValidStatement(inputBuffer)):
                if(checkContextStatement(inputBuffer)):

            else:
                print("I don't understand")


if __name__ == '__main__':
    main()
