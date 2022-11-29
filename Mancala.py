# Author: Christopher Qualls
# GitHub username: chrisPQ
# Date: 11/21/2022
# Description: Mancala Game implementation

# "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"
# 1. The mancala class will be initiated and there will be an empty list created to hold the player objects. The create
# player method will then be called and the player, passed into the method, will be amended to this empty list.
# 2. The create player method will take in a player object as a parameter, and this object will be amended to the
# mancala class' player list, if the player list is already 2 long, the player won't be amended to the list to prevent
# too many players being added.
# 3. The print board method, first prints the first player's score, then goes through the first player's pit list,
# printing each value as it moves. The next player's pit list is then gone through, but in the opposite direction to
# reverse its order to appear the correct way around. The score of that player is then printed and the print_board
# method is complete.
# 4. If the sum of all a player's pit values is 0, then the game is in an end state. The game adds all the
# other player's pit values to their score value. The score values are then compared and the higher value wins. This is
# done by iterating through the player's pit list and adding the values of each index.
# 5. The value of the chosen pit is acquired by iterating through the pit list, this value is then used to iterate
# forward in the pit list that many indexes. Each index it passes over is added by 1. If it goes over a player's
# score pit, it checks if the player moving the piece owns that pit. If the index of the final move is the same as the
# player's score pit, the player is allowed to take another turn. If the player's pit is empty, then it checks the
# distance to the player's score pit, and moves that distance past the score pit. The pit it lands on is then set to 0
# and the value is added to the player's score pit.

class Mancala:
    """
    has a list of the two player objects, maxed out at two
    method create player creates a player object, who has a list of its pits and the values of the pits
    the play_game method utilizes the values within the player object to move the mancala pieces around the board.
    This includes making sure to enforce special rules, and
    """
    def __init__(self):
        """
        will create a private empty list to hold the player objects
        """
        self.__player_list = []

    def add_player_to_game(self, player_object):
        """
        appends the given player object to the mancala game list of players
        :return:
        """
        self.__player_list.append(player_object)

    def view_players(self):
        for x in self.__player_list:
            print(x)

    def play_game(self, player_number, pit_number):
        """
        defines which player is moving, and what pit they are using, they will take the value of their pit, and move
        forward through their board, based on the chosen pit's value, dropping off pieces as they go. They may need to
        go into the other player's pit as well, so there needs to be capabilities for the mancala class to access the
        other player's pits at the same time. Will only drop seeds into the chosen players score pit, however.
        will print the board everytime it is run to show the player the updated game board after the move (helpful for
        debugging as well).
        each time it is run, it runs the return_winner function to determine if the game is in an end state
        :param player_number: the index of the player object who is moving. either 0 or 1
        :param pit_number: the pit number of the player, between 1-6
        :return: will not return anything, will instead run the print board function
        """
        player = self.__player_list[player_number]
        pit_range = player.get_value_of_pit(pit_number)
        for x in range(pit_number, pit_range):
            new_value = player.get_value_of_pit(x+1) + 1
            player.update_pit_value(x+1, new_value)
        player.update_pit_value(pit_number, 0)

    def return_winner(self):
        """
        this method first iterates through each player's pit list, if they are all 0 then the game is over, it checks
        each player's score and returns who wins
        :return: returns the player object with the highest score if the game is in an end state
        """
        pit_value = 0
        for x in self.__player_list:
            for y in range(0, 6):
                pit_value = pit_value + x.get_value_of_pit(y)
            if pit_value == 0:
                return True
            pit_value = 0
        return False

    def print_board(self):
        """
        will print the board as integer values in a vertical
        will iterate through the board of both players, starting with their store value and then each pit with their value
        :return:
        """
        board_string = " "
        board_string = board_string + str(self.__player_list[1].get_value_of_pit(-1))
        for y in range(0, 7):
            pit_value = self.__player_list[0].get_value_of_pit(y)
            board_string = board_string + " " + str(pit_value)
        print(board_string)
        board_string = ""
        for y in range(1, 8):
            pit_value = self.__player_list[1].get_value_of_pit(-y)
            board_string = board_string + " " + str(pit_value)
        board_string = board_string + " " + str(self.__player_list[0].get_value_of_pit(6))
        print(board_string)


class Player:
    """

    """
    def __init__(self, name, seeds=0):
        """

        :param name:
        :param seeds:
        """
        self.__name = name
        self.__seeds = seeds
        self.__pits = []
        for x in range(0, 6):
            self.__pits.append(4)
        self.__pits.append(self.__seeds)

    def get_value_of_pit(self, pit_index):
        """
        will return the value of the player's pit at the given index, this is used to make moves within the game class
        :param pit_index:
        :return:
        """
        return self.__pits[pit_index]

    def update_pit_value(self, pit_index, value):
        """
        updating the pit value is used when you move the pieces. You can set the pit to 0 when you start there, and add
        to the pit when you drop seeds off as you go, or when you activate the second special move and set the opponents
        pit value to 0
        :param value:
        :return:
        """
        self.__pits[pit_index] = value

    def add_to_score(self, value):
        """
        adds value to the players private score, this represents the player's store pit
        :param value:
        :return:
        """
        self.__pits[6] = self.__pits[6] + value

    def get_score(self):
        """
        returns the score of the player, used to determine the winner of the game
        :return:
        """
        return self.__pits[6]


game = Mancala()
player1 = Player("Monkey")
player2 = Player("Gibbon")
game.add_player_to_game(player1)
game.view_players()
game.add_player_to_game(player2)
game.view_players()
player1.update_pit_value(6, 11)
for x in range(0, 4):
    player1.update_pit_value(x, 0)

print(game.return_winner())
game.play_game(0, 4)
game.print_board()