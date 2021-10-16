from enum import Enum

class Position(Enum):
    Goalie = 1,
    Defence = 2,
    Forward = 3

class Player:
    def __init__(self, name: str, pos: Position):
        self._name = name    
        self._pos = pos


p = Player("Foppa", Position.Forward) 
p2 = Player("Sudden", Position.Forward) 




def printplayer(namn: str, age: int, position: Position) :
    if position == Position.Forward:
        print("Anfallare")
    if position == Position.Defence:
        print("Försvarare")
    if position == Position.Goalie:
        print("Målis")
    print(namn + "," + str(age))

printplayer("Mats Sundin", 50, Position.Forward )
