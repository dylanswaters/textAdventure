types:
remove x from y
    target x: item, object, exit, person
    target y: Room, Player
    ex: type: remove target: Person : dylan, Room : bedRoom

dialogue
    desc: starts dialogue
    target: Person : personName
    targetTypes: person
    ex: type: dialogue target: Person : dylan

unlock
