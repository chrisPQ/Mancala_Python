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

    def create_player(self, player_name):
        """
        appends the given player object to the mancala game list of players
        :return:
        """
        if len(self.__player_list) < 2:
            self.__player_list.append(Player(player_name))
        else:
            return "can't add more players"

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
        # I comment this section heavily because it is confusing otherwise with a bunch of magic numbers

        # convert pit number to proper index values i.e. 1 is actually 0 in lists
        pit_number = pit_number - 1
        board_list = []
        # loading pit values
        for player_object in self.__player_list:
            board_list = board_list + player_object.get_pit_list()
            board_list.append(player_object.get_score())

        # first check which player is going, as each has to take into account their score pits in board_list
        if player_number == 1:
            moves_remaining = board_list[pit_number]
            board_list[pit_number] = 0

            # while we have pieces in our hand
            while moves_remaining > 0:
                if pit_number + 1 == 6:  # check if score pit
                    self.__player_list[0].add_to_score(1)
                    pit_number = pit_number + 1
                elif pit_number + 1 >= len(board_list) - 1:  # check if the index goes into player 2's score
                    pit_number = 0  # if it does, reset the pit you are on to your own first pit
                    board_list[pit_number] = board_list[pit_number] + 1
                else:  # add 1 to current pit and move forward
                    pit_number = pit_number + 1
                    board_list[pit_number] = board_list[pit_number] + 1
                moves_remaining = moves_remaining - 1

            if pit_number == 6:  # landing in score pit check
                print("player 1 take another turn")

            distance_to_score = 6 - pit_number  # check how far you are to your own score pit
            opposite_pit = distance_to_score * 2 + pit_number  # the opposite pit will be that distance doubled
            if board_list[pit_number] == 1:  # if the pit you are on at the end is 1, meaning it was empty
                opposite_pit_value = board_list[opposite_pit]  # get the opposite pit's value
                board_list[opposite_pit] = 0  # set both to 0
                board_list[pit_number] = 0
                self.__player_list[0].add_to_score(opposite_pit_value + 1)  # add both to your score (1 is your own pit)
        elif player_number == 2:
            pit_number = pit_number + 7  # offset the pit your on to player two's first pit
            moves_remaining = board_list[pit_number]
            board_list[pit_number] = 0
            while moves_remaining > 0:
                if pit_number + 1 == 13:  # check if score pit
                    self.__player_list[1].add_to_score(1)
                    pit_number = pit_number + 1
                elif pit_number + 1 > len(board_list) - 1:  # if you'd go outside the board list, go back to p1's pit 1
                    pit_number = 0
                    board_list[pit_number] = board_list[pit_number] + 1
                elif pit_number + 1 == 6:  # if you'd land in player 1's score pit, skip over it
                    pit_number = 7
                    board_list[pit_number] = board_list[pit_number] + 1
                else:
                    pit_number = pit_number + 1
                    board_list[pit_number] = board_list[pit_number] + 1
                moves_remaining = moves_remaining - 1
            if pit_number == 12:  # landing in score pit check
                print("player 2 take another turn")

            distance_to_score = 13 - pit_number
            # modulus needed as the opposite pit will always be the remainder of the board_list's length if you land in
            # a player 2 pit
            opposite_pit = (distance_to_score * 2 + pit_number) % 13 - 1  # minus 1 as indexes start at 0
            if board_list[pit_number] == 1:  # if the pit you are on at the end is 1, meaning it was empty
                opposite_pit_value = board_list[opposite_pit]
                board_list[opposite_pit] = 0
                board_list[pit_number] = 0
                self.__player_list[1].add_to_score(opposite_pit_value + 1)

        # spitting out new pit values to player object's pit lists
        for index in range(0, 6):
            self.__player_list[0].update_pit_value(index, board_list[index])
            self.__player_list[1].update_pit_value(index, board_list[index+7])

        # run return winner to update board if in game state
        self.return_winner()

        # reinserting score values into board list to return board
        board_list = []
        for player_object in self.__player_list:
            board_list = board_list + player_object.get_pit_list()-
            board_list.append(player_object.get_score())
        return board_list

    def return_winner(self):
        """
        this method first iterates through each player's pit list, if they are all 0 then the game is over, it checks
        each player's score and returns who wins
        :return: returns the player object with the highest score if the game is in an end state
        """
        pit_value = 0
        game_end_flag = False  # flag used to determine if game is in end state
        for player in self.__player_list:
            for y in range(0, 6):
                pit_value = pit_value + player.get_value_of_pit(y)
            if pit_value == 0:
                game_end_flag = True
            pit_value = 0
        if game_end_flag:  # the game is in an end state, add all the pit's values to the corresponding player's score
            for player in self.__player_list:
                for y in range(0, 6):
                    pit_value = pit_value + player.get_value_of_pit(y)
                    player.update_pit_value(y, 0)
                player.add_to_score(pit_value)
                pit_value = 0
        # check if game is over and who won
        if game_end_flag:
            if self.__player_list[0].get_score() > self.__player_list[1].get_score():
                return "Winner is player 1: " + str(self.__player_list[0].get_name())
            elif self.__player_list[0].get_score() < self.__player_list[1].get_score():
                return "Winner is player 2: " + str(self.__player_list[1].get_name())
            else:
                return "It's a tie"
        else:
            return "Game has not ended"

    def print_board(self):
        """
        will print the board as integer values in a horizontal
        will iterate through the board of both players, starting with their store and then each pit with their value

        assuming player 1 is facing upward:
        {player 2 score, player 2 pits: {pit6, pit5, pit4, pit3, pit2, pit1}, player 1 score}
        {player 2 score, player 1 pits: {pit1, pit2, pit3, pit4, pit5, pit6}, player 1 score}
        :return:
        """
        print("player1:")
        print("store: " + str(self.__player_list[0].get_score()))
        print(self.__player_list[0].get_pit_list())
        print("player2:")
        print("store: " + str(self.__player_list[1].get_score()))
        print(self.__player_list[1].get_pit_list())
        # print("_"*20)


class Player:
    """
        game object that holds a name, a score, and a list with values corresponding to stones in the pits
    """
    def __init__(self, name, seeds=0):
        """

        :param name:
        :param seeds:
        """
        self.__name = name
        self.__pits = []
        self.__store = seeds
        for x in range(0, 6):
            self.__pits.append(4)

    def get_name(self):
        """"
        return player's name
        """
        return self.__name

    def get_value_of_pit(self, pit_index):
        """
        will return the value of the player's pit at the given index, this is used to make moves within the game class
        :param pit_index:
        :return:
        """
        return self.__pits[pit_index]

    def get_pit_list(self):
        """

        :return: return player object's pit list
        """
        return self.__pits

    def update_pit_value(self, pit_index, value):
        """
        updating the pit value is used when you move the pieces. You can set the pit to 0 when you start there, and add
        to the pit when you drop seeds off as you go, or when you activate the second special move and set the opponents
        pit value to 0
        :param pit_index:
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
        self.__store = self.__store + value

    def get_score(self):
        """
        returns the score of the player, used to determine the winner of the game
        :return:
        """
        return self.__store

    def print_player_pits(self):
        """
        :return: just print the player's pit list, used for debugging
        """
        print(self.__pits)


def main():
    game = Mancala()
    game.create_player("Monkey")
    game.view_players()
    game.create_player("Gibbon")
    game.view_players()
    print(game.create_player("Siamang"))

    game.play_game(1, 1)
    game.play_game(1, 2)
    game.play_game(1, 3)
    game.play_game(1, 4)
    game.play_game(1, 5)
    game.play_game(1, 6)
    game.print_board()
    print(game.return_winner())


if __name__ == "__main__":
    main()
