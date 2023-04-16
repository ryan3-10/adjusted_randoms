from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from classes import Set, Player, Team, Character
from kivy.uix.behaviors import ButtonBehavior
from random import choice



class ImageButton(ButtonBehavior, Image):
    pass

class MyGridLayout(GridLayout):
    
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        individual_description = ("In individual pools, each player drafts characters into "
                                "a personal pool,\nand will be assigned a character from his/her own "
                                "pool")
        
        collective_description = ("In collective pool, Each player contributes to drafting characters "
                                   "into 1 large pool,\n and will be assigned a character from that "
                                   "pool.")
        self.cols = 1
        self.set = Set()
        
        #Second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.top_grid.size_hint_y = None
        self.top_grid.height = 300

        #Heading label
        self.add_widget(Label(
                            text="Options Select",
                            font_size=30,
                            size_hint_y=None,
                            height=30
                            ))
        
        #Notes
        self.add_widget(Label(text=f"-{individual_description}\n\n-{collective_description}"))

        #Singles button
        self.singles_button = Button(
                         text="Singles (1v1)",
                         bold=True,
                         size_hint_y = None,
                         height = 100,
                         )
        self.singles_button.bind(on_press=self.set_singles)
        self.top_grid.add_widget(self.singles_button)

        #Doubles button
        self.doubles_button = Button(
                              text="Doubles (2v2)",
                              bold=True,
                              size_hint_y = None,
                              height = 100,
                              )
        self.doubles_button.bind(on_press=self.set_doubles)
        self.top_grid.add_widget(self.doubles_button)

        #Individual pools button
        self.indi_pools_button = Button(
                              text="Individual Pools",
                              bold=True,
                              size_hint_y = None,
                              height = 100
                              )
        self.indi_pools_button.bind(on_press=self.set_seperate_pools)
        self.top_grid.add_widget(self.indi_pools_button)

        #Collective pool button
        self.collective_pool_button = Button(
                              text="Collective Pool",
                              bold=True,
                              size_hint_y = None,
                              height = 100
                              )
        self.collective_pool_button.bind(on_press=self.set_collective_pool)
        self.top_grid.add_widget(self.collective_pool_button)
        
        #Number of picks label and text box
        self.top_grid.add_widget(Label(
                                   text="Input the number of picks each player gets"
                                   " (2-20)",
                                   size_hint_y=None,
                                   height=100
                                   ))
        self.number_picks = TextInput(
                                      multiline=False,
                                      size_hint_y=None,
                                      height=100,
                                      text='5'
                                      )    
        self.top_grid.add_widget(self.number_picks)

        #Add top_grid to app
        self.add_widget(self.top_grid)

        #Continue Button
        self.continue_button = Button(text="Continue", 
                                      size_hint_y=None,
                                      height=100,
                                      bold=True,
                                      background_color=(0, 1, 0, 1)
                                    )
        self.continue_button.bind(on_release=self.check_initial)
        self.add_widget(self.continue_button)

        #Picks error label
        self.picks_error = Label(
                            text="",
                            size_hint_y=None,
                            height=0,
                            color='red'
        )
        self.add_widget(self.picks_error)

        #Picks error label
        self.picks_error = Label(
                            text="",
                            size_hint_y=None,
                            height=0,
                            color='red'
        )
        self.add_widget(self.picks_error)

        #Buttons error label
        self.buttons_error = Label(
                            text="",
                            size_hint_y=None,
                            height=0,
                            color='red'
        )
        self.add_widget(self.buttons_error)
    
    def set_singles(self, instance):
        self.set.set_singles(instance)
        self.singles_button.background_color="blue"
        self.doubles_button.background_color="grey"

    def set_doubles(self, instance):
        self.set.set_doubles(instance)
        self.doubles_button.background_color="blue"
        self.singles_button.background_color="grey"
    
    def set_seperate_pools(self, instance):
        self.set.set_seperate_pools(instance)
        self.indi_pools_button.background_color="blue"
        self.collective_pool_button.background_color="grey"
    
    def set_collective_pool(self, instance):
        self.set.set_collective_pool(instance)
        self.collective_pool_button.background_color="blue"
        self.indi_pools_button.background_color="grey"

    #Check that options have been selected correctly
    def check_initial(self, instance):
        if self.set.doubles == None or self.set.seperate_pools == None:
            self.buttons_error.height = 50
            self.buttons_error.text = "Please select one option from each column"
            return
        else:
            self.buttons_error.height = 0
            self.buttons_error.text = ""
        try:
            self.set.picks = int(self.number_picks.text)
            if self.set.picks < 2 or self.set.picks > 20:
                self.picks_error.height=50
                self.picks_error.text="The number of picks must be an integer of 2-20"
                return
            else:
                self.picks_error.height = 0
                self.picks_error.text = ""
        except:
            self.picks_error.height=50
            self.picks_error.text="The number of picks must be an integer of 2-20"
            return
        self.add_players()
        
    #Input players' names
    def add_players(self):
        self.clear_widgets()
        
        #Team 1 label
        self.team1_label = Label(
                    text="Team 1",
                    font_size =50
        )

        #Player 1 label and text box
        self.player1_label = (Label(text="Player 1",
                                    font_size=26
                                ))
        self.player1 = TextInput(
                                multiline=False,
                                text="Player 1",
                                size_hint_y=None,
                                height=50,
                                )

        #Player 2 label and text box 
        self.player2_label = (Label(text="Player 2",
                                    font_size=26
                                    ))
        self.player2 = TextInput(
                                multiline=False,
                                text="Player 2",
                                size_hint_y=None,
                                height=50,
                                )

        #Team 2 label
        self.team2_label = Label(
                    text="Team 2",
                    font_size = 50
        )

        #Player 3 label and text box 
        self.player3_label = Label(text="Player 3",
                                   font_size=26
                                   )
        self.player3 = TextInput(
                                multiline=False,
                                text="Player 3",
                                size_hint_y=None,
                                height=50,
                                )
        
        #Player 4 label and text box 
        self.player4_label = Label(text="Player 4",
                                   font_size=26
                                   )
        self.player4 = TextInput(
                                multiline=False,
                                text="Player 4",
                                size_hint_y=None,
                                height=50
                                )
        #Setup for doubles
        if self.set.doubles:
            self.team1 = Team()
            self.team2 = Team()
            self.top_grid = GridLayout()
            self.top_grid.cols = 2
            self.top_grid.add_widget(self.team1_label)
            self.top_grid.add_widget(self.team2_label)
            self.top_grid.add_widget(self.player1_label)
            self.top_grid.add_widget(self.player3_label)
            self.top_grid.add_widget(self.player1)
            self.top_grid.add_widget(self.player3)
            self.top_grid.add_widget(self.player2_label)
            self.top_grid.add_widget(self.player4_label)
            self.top_grid.add_widget(self.player2)
            self.top_grid.add_widget(self.player4)
            self.add_widget(self.top_grid)
        
        #Setup for singles
        elif not self.set.doubles:
            self.add_widget(self.player1_label)
            self.add_widget(self.player1)
            self.add_widget(self.player2_label)
            self.add_widget(self.player2)
        
        #Continue button
        self.button = Button(
                            text="Continue",
                            size_hint_y=None,
                            height=75,
                            background_color=(0, 1, 0, 1)
                            )
        self.button.bind(on_press=self.check_players)
        self.add_widget(self.button)

        #Error label
        self.error = Label(
                        text="",
                        size_hint_y=None,
                        height=0,
                        color='red'
        )
        self.add_widget(self.error)
    
    #Check that all player names were filled out
    def check_players(self, instance):
        if len(self.player1.text) == 0 or len(self.player2.text) == 0:
            self.error.text="Please insert a name for each player"
            self.error.height=50
            return
        self.set.add_player(Player(self.player1.text))
        self.set.add_player(Player(self.player2.text))

        if self.set.doubles:
            if len(self.player3.text) == 0 or len(self.player4.text) == 0:
                self.error.text="Please insert a name for each player"
                self.error.height=50
                return
            
            #If it's a doubles match, 2 teams are created
            self.set.add_player(Player(self.player3.text))
            self.set.add_player(Player(self.player4.text))
            self.team1.add_player(self.set.players[0])
            self.team1.add_player(self.set.players[1])
            self.team2.add_player(self.set.players[2])
            self.team2.add_player(self.set.players[3])
        #In a doubles set, this code reorders the players list to be more competitive
        if self.set.doubles:
            self.set.players.append(self.set.players[1])
            self.set.players.remove(self.set.players[1])
        self.populate_selection_screen()
    
    #Add every character's image to the screen for selection
    def populate_selection_screen(self):
        self.clear_widgets()
        self.size_hint_y = 1
        self.add_widget(Label(text=f"{self.set.players[self.set.round]}, draft {self.set.picks} "
                              "characters.",
                              size_hint_y=None,
                              height=50,
                              font_size=40,
                            ))
        self.character_board = GridLayout()
        self.character_board.cols = 10

        #Adds every character to the 'character_board' grid
        for character in self.set.full_roster:
            image_button = ImageButton(source=f"images/{character.source}")
            image_button.bind(on_press=self.draft(image_button))
            self.character_board.add_widget(image_button)
        self.add_widget(self.character_board)

        #Add Pool screen and buttons
        self.pool_screen = GridLayout()
        self.add_widget(self.pool_screen)
        self.pool_screen.size_hint_y = None
        self.pool_screen.height = 130
        self.button_grid = GridLayout(size_hint_y=None, height=30)
        self.button_grid.cols = 2

        self.undo_button = Button(text="Undo", 
                                  size_hint_y=None, 
                                  height=30, 
                                  on_press=self.undo)

        self.lock_in_button = Button(text="Lock in",
                                     size_hint_y=None,
                                     height=30,
                                     on_press=self.lock_in)

        self.button_grid.add_widget(self.undo_button)
        self.button_grid.add_widget(self.lock_in_button)
        self.add_widget(self.button_grid)
       
        self.populate_pool_screen()
        
    def populate_pool_screen(self):
        characters_string = ""
        if self.set.seperate_pools:
            pool_title = f"{self.set.players[self.set.round]}'s Pool:"
            #Create string of all characters in pool
            for index, character in enumerate(self.set.players[self.set.round].pool):
                characters_string += character.name
                if (index + 1) % 5 == 0:
                    characters_string += "\n"
                else:
                    characters_string += ", "
        elif not self.set.seperate_pools:
            pool_title = "Collective Pool:"
            #Create string of all characters in pool
            for index, character in enumerate(Player.collective_pool):
                characters_string += character.name
                if (index + 1) % 10 == 0:
                    characters_string += "\n"
                else:
                    characters_string += ", "
        
        self.pool_screen.clear_widgets()
        self.pool_screen.cols = 1
        self.pool_screen.add_widget(Label(text=f"{pool_title}"))
        self.pool_screen.add_widget(Label(text=f"{characters_string}"))

        #Buttons turn green if available
        if len(self.set.players[self.set.round].pool) > 0:
            self.undo_button.background_color = (0, 1, 0, 1)
        if len(self.set.players[self.set.round].pool) == self.set.picks:
            self.lock_in_button.background_color = (0, 1, 0, 1)
    
    def undo(self, instance):
        if len(self.set.players[self.set.round].pool) > 0:
            self.set.players[self.set.round].pool.pop()
            Player.collective_pool.pop()
        self.populate_selection_screen()
        
    #Adds selected character to person and collective pool. Also removes selected button
    def draft(self, image_button):
        def use_button(instance):
            if len(self.set.players[self.set.round].pool) < self.set.picks:
                for character in self.set.full_roster:
                    if f"images/{character.source}" == image_button.source:
                        if character not in Player.collective_pool:
                            Player.add2_collective(character)
                        if character not in self.set.players[self.set.round].pool:
                            self.set.players[self.set.round].add2_personal(character)
            self.populate_pool_screen()
        return use_button
    
    def lock_in(self, instance):
        #Makes it so that the selected character will not be available when 
        #It is the next player's turn if mode is collective pool
        if not self.set.seperate_pools:
            for character in self.set.players[self.set.round].pool:
                self.set.full_roster.remove(character)

        if len(self.set.players[self.set.round].pool) == self.set.picks:
                self.set.round += 1
                if self.set.round == len(self.set.players):
                    self.reorder_players(instance)
                    return
                else:
                    self.populate_selection_screen()
    
    def reorder_players(self, instance):
        if self.set.doubles:
            self.set.players = [self.set.players[0], self.set.players[3], self.set.players[1], self.set.players[2]]
        return self.assignments(instance)
        
    def assignments(self, instance):
        self.clear_widgets()
        #Randomize each player's character
        if self.set.seperate_pools:
            self.pairs = {player: choice(player.pool) for player in self.set.players}
        elif not self.set.seperate_pools:
            self.pairs = {player: choice(Player.collective_pool) for player in self.set.players}
        self.check_fur_dups(instance)

    def check_fur_dups(self, instance):
        #Ensure that 2 players never get the same character in a given round (Just for fun)    
        for character in self.pairs.values():
            if list(self.pairs.values()).count(character) > 1:
                return self.assignments(instance)
        return self.display()

    def display(self):  
        self.cols = 3
        for player in self.pairs:
            self.add_widget(Label(text=player.name,
                                  font_size=30
                                  ))
            self.add_widget(Label(text=self.pairs[player].name,
                                  font_size=30
                                  ))
            self.add_widget(Image(source=f"images/{self.pairs[player].source}"))
        
        #Button to rerandomizes assignments
        self.add_widget(Label(size_hint_y=None,
                              height=50))
        next_game = (Button(text="Next Game",
                        size_hint_y=None,
                        background_color=(0, 1, 0, 1),
                        height=50))
        next_game.bind(on_press=self.assignments)
        self.add_widget(next_game)

        #Button that resets entire program
        hard_reset = (Button(text="Restart Program",
                        size_hint_y=None,
                        background_color=(0, 1, 0, 1),
                        height=50))
        hard_reset.bind(on_press=self.restart_app)
        self.add_widget(hard_reset)

    def restart_app(self, instance):
        print(self.set.players)
        Player.collective_pool.clear()
        self.clear_widgets()
        Adjusted_Randoms().run()    


class Adjusted_Randoms(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    Adjusted_Randoms().run()
