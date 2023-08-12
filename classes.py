import os
from PIL import Image

class Character:
    def __init__(self, name: str, source):
        self.name = name
        self.source = source

#Returns a character object based on the image source
def create_character(image):
    index = image.index(".")
    name = image[:index].replace("_", " ").title()
    return Character(name, image)

class Set:
    def __init__(self):
        self.doubles: bool = None
        self.seperate_pools: bool = None
        self.picks: bool = None
        self.players = []
        self.round = 0 #The round of the draft. When a player's turn is over, round will go up 1.
        self.full_roster = sorted(list(map(create_character, os.listdir("images"))), 
                         key=lambda x: x.name)

   
    def set_doubles(self, instance):
        self.doubles = True

  
    def set_singles(self, instance):
        self.doubles = False

   
    def set_seperate_pools(self, instance):
        self.seperate_pools = True

  
    def set_collective_pool(self, instance):
        self.seperate_pools = False
    
  
    def add_player(self, player):
        self.players.append(player)

class Player:
    collective_pool = []
    def __init__(self, name: str):
        self.name = name
        self.pool = []
    
    def __str__(self):
        return self.name
    
    @classmethod
    def add2_collective(cls, character):
        cls.collective_pool.append(character)
    
    def add2_personal(self, character):
        self.pool.append(character)

class Team:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)


