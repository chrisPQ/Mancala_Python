# Author: Christopher Qualls
# GitHub username: chrisPQ
# Date: 11/21/2022
# Description: Take in a list and output the maximum of the list
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
        pass

    def create_player(self, name):
        """
        will create a
        :param name:
        :return:
        """
        return Player(name)

    def add_player_to_game(self, player_object):
        """
        appends the given player object to the mancala game list of players
        :return:
        """
        pass

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
        pass

    def return_winner(self):
        """
        this method first iterates through each player's pit list, if they are all 0 then the game is over, it checks
        each player's score and returns who wins
        :return: returns the player object with the highest score if the game is in an end state
        """
        pass

    def print_board(self):
        """
        will print the board as integer values in a vertical
        will iterate through the board of both players, starting with their store value and then each pit with their value
        :return:
        """
        return


class Player:
    """

    """
    def __init__(self, name, seeds):
        """

        :param name:
        :param seeds:
        """
        pass

    def get_value_of_pit(self, pit_index):
        """
        will return the value of the player's pit at the given index, this is used to make moves within the game class
        :param pit_index:
        :return:
        """
        pass

    def update_pit_value(self, value):
        """
        updating the pit value is used when you move the pieces. You can set the pit to 0 when you start there, and add
        to the pit when you drop seeds off as you go, or when you activate the second special move and set the opponents
        pit value to 0
        :param value:
        :return:
        """
        pass

    def add_to_score(self, value):
        """
        adds value to the players private score, this represents the player's store pit
        :param value:
        :return:
        """
        pass

    def get_score(self):
        """
        returns the score of the player, used to determine the winner of the game
        :return:
        """
    pass