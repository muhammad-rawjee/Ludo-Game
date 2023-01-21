# Author: Muhammad Ali Rawjee
# GitHub username: muhammad-rawjee
# Date: 08/10/2022
# Description: "LudoGame.py" is a program that allows two to four people to play a simplified version of the game
#               of Ludo. In the game of Ludo two, three, or four players (A, B, C or D) can play.
#               Each player has 2 tokens (p and q). At the beginning of the game, each player's
#               two tokens are in the player's home yard. Each player takes a turn by rolling the dice.
#               On a turn, a player can move a token that is on the board clockwise the number of steps
#               indicated by the die along the track. Moving a token out of the home yard onto the board’
#               “ready to go position” can only be done by rolling a 6. Rolling a 6 earns the player an
#               additional roll in that turn.If the bonus roll results in a 6 again, there is no additional
#               roll again.
#
#               After a certain number of steps, the token will enter that player’s home squares
#               which no opponent may enter. Then the token will try to enter the finishing square (end).
#               The token must reach the finishing square on an exact roll. If the roll number is larger
#               than the steps needed to get to the finishing square, the token will bounce back the
#               remaining number of steps.
#
#               WINNING THE GAME: the first player whose 2 tokens have entered the finishing square will
#               win the game. The rest will continue playing until there is only one player left.

class Player:
    """
    A class to represent a Player object, with named position ('A','B','C','D'),
    token positions for tokens 'p' and 'q' and start and end positions for both tokens
    'p' and 'q'. Used by LudoGame class.
    """
    def __init__(self):
        """
        The constructor for Player class. Takes no parameters.
        Initializes the required data members. All data members are private.
        """
        self._position = None          # ('A','B','C' or 'D')
        self._start = None             # Start position for tokens (p,q)
        self._end = None               # Home position for tokens (p,q)
        self._current_position = []    # ‘H’:home yard, ‘R’: ready to go position, ‘E’:finished position, '**': num pos
        self._current_state = False    # Status of Player: whether the player has won or is still playing
        self._token_p_step_count = -1  # token 'p' total step count
        self._token_q_step_count = -1  # token 'q' total step count
        self._stacked = 0              # 1 if tokens (p,q) stacked, else 0

    def set_position(self, position):
        """
        Set method for position, ('A', 'B', 'C', or 'D')
        Parameter 'position' used to set relevant private value.
        Used by LudoGame class to set positions of Player objects

        :return: None
        """
        self._position = position

    def get_position(self):
        """
        Get method for position, ('A', 'B', 'C', or 'D')
        Used by LudoGame class, to get position and update
        the values of the object with said position.

        :return: position ('A', 'B', 'C', or 'D')
        """
        return self._position

    def set_start_and_end(self, position):
        """
        Set method for start position and end position of tokens 'p' and 'q'
        (Different for each 'A','B','C', and 'D')
        Parameter 'position' used to set relevant private values.
        Used by LudoGame class to set start and end positions of tokens 'p' and 'q'
        for positions ('A','B','C', and 'D')

        :return: None
        """
        if position == 'A':
            self._start = 0
            self._end = 50
        elif position == 'B':
            self._start = 14
            self._end = 8
        elif position == 'C':
            self._start = 28
            self._end = 22
        elif position == 'D':
            self._start = 42
            self._end = 36

    def get_start(self):
        """
        Get method for start position of token 'p' and 'q' (0, 14, 28, or 42)

        :return: start (start position for tokens)
        """
        return self._start

    def get_end(self):
        """
        Get method for start position of token 'p' and 'q' (0, 14, 28, or 42)

        :return: end (end position for both tokens)
        """
        return self._end

    def get_token_p_step_count(self):
        """
        Get method for token 'p' total step count (Not True position on board)

        :return: token_p_step_count (total steps taken by token 'p')
        """
        return self._token_p_step_count

    def get_token_q_step_count(self):
        """
        Get method for token 'q' total step count (Not True position on board)

        :return: token_q_step_count (total steps taken by token 'q')
        """
        return self._token_q_step_count

    def set_token_p_step_count(self, step_count):
        """
        Set method for token 'p' total step count
        Method updates token_p_step_count to param step_count
        Parameter 'step_count' used to set relevant private value.
        Used by move_token() method in LudoGame class to set values of tokens
        'p' according to dice rolled.

        :return: None
        """
        self._token_p_step_count = step_count

    def set_token_q_step_count(self, step_count):
        """
        Set method for token 'q' total step count
        Method updates token_q_step_count to param step_count
        Parameter 'step_count' used to set relevant private value.
        Used by move_token() method in LudoGame class to set values of tokens
        'q' according to dice rolled.

        :return: None
        """
        self._token_q_step_count = step_count

    def get_stacked(self):
        """
        Get method for players stacked value, stacked value is 1
        if both tokens are stacked. Else stacked value is 0

        :return: stacked (1 or 0)
        """
        return self._stacked

    def set_stacked(self, stacked_val):
        """
        Set Method for stacked value
        Method updates stacked_val to parameter stacked_val.
        Used by move_token() method in LudoGame class to set stacked value to 1,
        If both tokens ('p','q') are stacked (i.e. land on same spot).

        :return: None
        """
        self._stacked = stacked_val

    def set_current_position(self):
        """
        Set Method for current position
        Uses the get methods for token_p_step_count and
        token_q_step_count, then uses the get_space_name() method and
        updates the position_list data member with the string values of the
        positions of each token ('p','q').

        :return: None
        """
        # Current position returns list of two string vals, position of token 'p' and 'q'
        position_list = []

        # FOR TOKEN P
        token_p_position = self.get_token_p_step_count()
        token_p_position_string = self.get_space_name(token_p_position)
        position_list.append(token_p_position_string)

        # FOR TOKEN Q
        token_q_position = self.get_token_q_step_count()
        token_q_position_string = self.get_space_name(token_q_position)
        position_list.append(token_q_position_string)
        self._current_position = position_list

    def get_current_position(self):
        """
        Get Method for current position, Method returns
        list of two string vals, position of token 'p' and 'q'.

        :return: current_position (list of two string vals)
        """
        # Current position returns list of two string vals, position of token 'p' and 'q' respectively.
        return self._current_position

    def get_completed(self):
        """
        Get Method for current state of player, returns True if
        both tokens are landed on 'E' (finishing square), Else returns False

        :return: completed (True or False)
        """
        # Takes no parameters and returns True or False if the player has finished or not finished the game
        return self._current_state

    def set_completed(self, completed_val):
        """
        Set method for current state of player (completed or not).
        Method updates current_state to parameter completed_val.

        :return: None
        """
        self._current_state = completed_val

    def get_space_name(self, token_spaces):
        """
        Get method for string name of space.
        Method takes as an argument token_space (int val),
        and returns a string value of the TRUE position of the token_space for token 'p' or 'q'.
        The method takes into consideration which player ('A','B','C' or 'D') is asking for a space
        name (considering they all have different start positions)

        :return: space_name (string val)
        """
        # Start position of a token (0, 14, 28, 42)
        token_begin = self.get_start()

        # Position ('A','B','C' or 'D')
        token_position = self.get_position()

        # For board positions ('A1','B1',etc...)
        final_string = token_position

        # For integer board positions
        final_integer = token_begin

        # Take an integer, and depending on its value and player value (A, B, C, D), return TRUE board position (string)
        if token_spaces == 0:
            return 'R'
        elif token_spaces == -1:
            return 'H'
        # For integer input > 50
        elif token_spaces > 50:
            if token_spaces == 57:
                return 'E'
            else:
                position_str = str(token_spaces % 50)
                final_string += position_str
                return final_string
        # For input > 0 and input =< 50
        else:
            final_integer += token_spaces
            final_integer = final_integer % 56
            return str(final_integer)


class LudoGame:
    """
    A class to represent a LudoGame object. Game is played by a
    minimum of two players and a maximum of four players.
    Player class is used to initialize these players and their
    relevant attributes.
    """
    def __init__(self):
        """
        The constructor for LudoGame class. Takes no parameters.
        Initializes the required data members. All data members are private
        """
        self._players_list = []

    def get_players_list(self):
        """
        Get Method for players_list, returned list
        is a list of Player objects.

        :return: players_list (List of objects)
        """
        return self._players_list

    def get_player_by_position(self, token_name):
        """
        Get Method for player object, method returns player object,
        If parameter token_name (string value) is a match for the
        position ('A','B','C' or 'D') the method returns that Player
        object value.

        :return: Player Object (from players_list)
        """
        # Get method returns list of Player Objects
        players_list = self.get_players_list()

        # Iterate through Player Objects list
        for element in players_list:
            # If a Player Objects data member 'position' matches token_name, return Player Object
            if element.get_position() == token_name:
                return element
        # Else return "Player not found!"
        return "Player not found!"

    def move_token(self, player_obj, token_name, steps_taken_by_token):
        """
        move_token method takes three parameters: the player object, the token name (‘p’ or ‘q’)
        and the steps the token will move on the board (int). This method will take care of one
        token moving on the board. It will also update the token’s total steps, and it will take
        care of kicking out other opponent tokens as needed. The play_game method will use this method.

        :return: None
        """
        # player_obj's position (A,B,C or D)
        player_obj_position = player_obj.get_position()
        # Token 'p' and 'q' step count values, BEFORE any dice roll
        player_p_token_pos = player_obj.get_token_p_step_count()
        player_q_token_pos = player_obj.get_token_q_step_count()
        # Amount to "BOUNCE BACK" tokens 'p' and 'q' by AFTER any dice roll
        bounce_p = (player_p_token_pos + steps_taken_by_token) % 57
        bounce_q = (player_q_token_pos + steps_taken_by_token) % 57

        # TOKEN "P"
        if token_name == 'p':
            # Token 'p' step count values, AFTER any dice roll
            set_steps = player_p_token_pos + steps_taken_by_token
            # If step count value for token 'p' BEFORE any dice roll is 57 (At ending square 'E')
            if player_p_token_pos == 57:
                player_obj.set_token_p_step_count(57)
            # If step count value for token 'p' AFTER any dice roll > 57, bounce token back by some factor
            elif set_steps > 57:
                set_steps = 57 - bounce_p
                player_obj.set_token_p_step_count(set_steps)
            # If step count value for token 'p' AFTER any dice roll < 57
            else:
                player_obj.set_token_p_step_count(set_steps)

        # TOKEN "Q"
        else:
            # Token 'q' step count values, AFTER any dice roll
            set_steps = player_q_token_pos + steps_taken_by_token
            # If step count value for token 'q' BEFORE any dice roll is 57 (At ending square 'E')
            if player_q_token_pos == 57:
                player_obj.set_token_q_step_count(57)
            # If step count value for token 'q' AFTER any dice roll > 57, bounce token back by some factor
            elif set_steps > 57:
                set_steps = 57 - bounce_q
                player_obj.set_token_q_step_count(set_steps)
            # If step count value for token 'q' AFTER any dice roll < 57
            else:
                player_obj.set_token_q_step_count(set_steps)

        # Token 'p' step count, and TRUE position (str) on board AFTER any dice roll
        token_p_numerical_position = player_obj.get_token_p_step_count()
        token_p_true_position = player_obj.get_space_name(token_p_numerical_position)

        # Token 'q' step count, and TRUE position (str) on board AFTER any dice roll
        token_q_numerical_position = player_obj.get_token_q_step_count()
        token_q_true_position = player_obj.get_space_name(token_q_numerical_position)

        # If token 'p' lands on token 'q' or vice versa,
        if (token_p_numerical_position == token_q_numerical_position) and (token_p_numerical_position > 0 and token_q_numerical_position > 0):
            player_obj.set_stacked(1)

        # Check if parameter player_obj tokens (p,q) on another players objects tokens
        # players_list is a shallow copy of original Player Object List.
        players_list = self.get_players_list().copy()

        # Modify players_list, delete parameter player_obj from players_list
        for element in players_list:
            if element.get_position() == player_obj_position:
                players_list.remove(element)

        # Now iterate through the remaining Player Objects and check if player_obj tokens (p,q) lands on any of the
        # remaining Player Object tokens (p,q).
        for element in players_list:
            # Assign tokens (p,q) step count, and their TRUE positions on board (string) to named variables
            token_p_num_pos = element.get_token_p_step_count()
            token_p_str_pos = element.get_space_name(token_p_num_pos)
            token_q_num_pos = element.get_token_q_step_count()
            token_q_str_pos = element.get_space_name(token_q_num_pos)

            # Change token 'p' tokens step count to -1 , if token 'p' TRUE position (string) on board is equal to
            # player_obj's token 'p' or token 'q' TRUE position (string) on board.
            if (token_p_num_pos > 0) and (token_p_num_pos < 50) and (token_p_str_pos == token_p_true_position or token_p_str_pos == token_q_true_position):
                element.set_token_p_step_count(-1)

            # Change token 'q' tokens step count to -1 , if token 'q' TRUE position (string) on board is equal to
            # player_obj's token 'p' or token 'q' TRUE position (string) on board.
            if (token_q_num_pos > 0) and (token_q_num_pos < 50) and (token_q_str_pos == token_p_true_position or token_q_str_pos == token_q_true_position):
                element.set_token_q_step_count(-1)

            # NOTE: Above code takes care of STACKED values since checks both tokens (p,q) separately.

    def play_game(self, players_list, turns_list):
        """
        :param players_list: List of positions players choose, such as: [‘A’, ‘C’]

        :param turns_list:  Turns list is a list of tuples with one value in the tuple
                            being a player ('A','B','C' or 'D') and the other being the
                            dice roll value for that player.

        :return: A list of strings representing the current spaces (string values)
                 of all the tokens ('p','q') for each player in the list.
        """
        # List to store Player Objects
        player_object_list = []
        # List to store Player Objects TRUE position on board for each token ('p' and 'q')
        player_token_list = []

        # Iterate through parameter players_list and for each iteration create Player Objects,
        # set their data members and append to player_object_list
        for element in players_list:
            if element.upper() == 'A':
                playerA = Player()
                playerA.set_position(element)
                playerA.set_start_and_end(element)
                playerA.set_current_position()
                player_object_list.append(playerA)
            elif element.upper() == 'B':
                playerB = Player()
                playerB.set_position(element)
                playerB.set_start_and_end(element)
                playerB.set_current_position()
                player_object_list.append(playerB)
            elif element.upper() == 'C':
                playerC = Player()
                playerC.set_position(element)
                playerC.set_start_and_end(element)
                playerC.set_current_position()
                player_object_list.append(playerC)
            elif element.upper() == 'D':
                playerD = Player()
                playerD.set_position(element)
                playerD.set_start_and_end(element)
                playerD.set_current_position()
                player_object_list.append(playerD)

        # Update players_list with newly created Player Objects list (player_object_list)
        self._players_list = player_object_list

        # Iterate through turns_list (tuple values of length 2).
        # Call priority_rules method for each item in turns_list
        # priority_rules method will ensure that each token will be moved according to the game rules.
        for item in turns_list:
            self.priority_rules(item)

        # Make shallow copy of Player Objects list and class data member players_list
        players_list = self.get_players_list().copy()

        # Iterate through newly created Player Objects List, players_list
        for element in players_list:
            # Set the TRUE positions on the board (str) of the tokens (p,q) for element (Player Object)
            element.set_current_position()
            # position_list is list of TRUE positions on board of tokens p and q respectively, list size = 2
            position_list = element.get_current_position()
            # Iterate through positions_list and add elements of position_list to player_token_list above
            for positions in position_list:
                player_token_list.append(positions)
            # If both tokens (p,q) are on finishing square ('E'), set completed status of Player to TRUE (player wins)
            if position_list[0] == 'E' and position_list[1] == 'E':
                element.set_completed(True)
        # Return list of strings representing the current spaces of tokens (p,q) for each player object in list
        return player_token_list

    def priority_rules(self, tuple_val):
        """
        Method enforces the rules listed below to move tokens to their appropriate places in the board.
        Method is used exclusively by the play_game() method. This method is the most important in the
        LudoGame class as it enforces a majority of the rules of the game.

        PRIORITY RULES:

        1. If the die roll is 6, try to let the token that still in the home yard get out of the home yard
        (if both tokens are in the home yard, choose the first one ‘p’)

        2. If one token is already in the home square and the step number is exactly what
           is needed to reach the end square, let that token move and finish

        3. If one token can move and kick out an opponent token, then move that token

        4. Move the token that is further away from the finishing square

        :return: None
        """
        # Player value ('A','B','C', or 'D'), (string value)
        player_token = tuple_val[0]
        # Dice rolled value (1-6), (int value)
        dice_rolled = tuple_val[1]

        # Player Object (Depends on value of player_token)
        player_playing = self.get_player_by_position(player_token)
        # Shallow copy of list of Player Objects and class data member players_list
        players_list = self.get_players_list().copy()
        # List to store TRUE token (p,q) board values of Player Objects in players_list other than player_playing
        other_players_position = []

        # Iterate through players_list and remove player_playing from it
        # (We do this to check if any player_playing tokens land on any other Player Objects' tokens (p,q))
        for element in players_list:
            if element.get_position() == player_token:
                players_list.remove(element)

        # Iterate through newly updated players_list and add
        # TRUE board positions of tokens (p,q) to other_players_position
        for element in players_list:
            # For each element set TRUE board positions for tokens (p,q)
            element.set_current_position()
            # position_list is list of TRUE positions on board of tokens p and q respectively, for Player Object element
            position_list = element.get_current_position()
            # Iterate through positions_list and add positions to positions_list
            for positions in position_list:
                other_players_position.append(positions)

        # player_playing's 'p' and 'q' token step count. (int)
        player_token_p = player_playing.get_token_p_step_count()
        player_token_q = player_playing.get_token_q_step_count()

        # player_playing's stacked value (1 if stacked, 0 if not)
        player_stacked = player_playing.get_stacked()

        # RAW token 'p' and 'q' step count AFTER dice roll (int)
        token_p_after = player_token_p + dice_rolled
        token_q_after = player_token_q + dice_rolled

        # Token 'p' and 'q' TRUE position on board after dice roll
        string_p_after = player_playing.get_space_name(token_p_after)
        string_q_after = player_playing.get_space_name(token_q_after)

        # Distance from finishing square for tokens 'p' and 'q'
        finish_dis_p = 57 - player_token_p
        finish_dis_q = 57 - player_token_q

        # RULES SECTION
        # Rule 1 Logic. (If die roll is 6, let token still in home yard get out of home yard, else let 'p' get out)
        if (dice_rolled == 6) and (player_token_p == -1 or player_token_q == -1):
            if player_token_p == -1 and player_token_q == -1:
                self.move_token(player_playing, 'p', 1)
            elif player_token_p == -1:
                self.move_token(player_playing, 'p', 1)
            elif player_token_q == -1:
                self.move_token(player_playing, 'q', 1)

        # Rule 2 Logic. (If one token already in the home square and step number is exactly what
        #                is needed to reach end square, let that token move and finish)
        elif (player_token_p >= 50 or player_token_p >= 50) and (token_p_after == 57 or token_q_after == 57):
            if player_stacked == 1:
                self.move_token(player_playing, 'p', dice_rolled)
                self.move_token(player_playing, 'q', dice_rolled)
            elif player_token_p >= 50 and token_p_after == 57:
                self.move_token(player_playing, 'p', dice_rolled)
            elif player_token_q >= 50 and token_q_after == 57:
                self.move_token(player_playing, 'q', dice_rolled)

        # Rule 3 Logic. (If one token can move and kick out an opponent token, then move that token)
        elif string_p_after in other_players_position or string_q_after in other_players_position:
            if player_stacked == 1:
                self.move_token(player_playing, 'p', dice_rolled)
                self.move_token(player_playing, 'q', dice_rolled)
            elif string_p_after in other_players_position:
                self.move_token(player_playing, 'p', dice_rolled)
            elif string_q_after in other_players_position:
                self.move_token(player_playing, 'q', dice_rolled)

        # Rule 4 Logic. (Move the token that is further away from the finishing square)
        elif finish_dis_q == finish_dis_p and (player_token_p != -1 and player_token_q != -1):
            if player_stacked == 1:
                self.move_token(player_playing, 'p', dice_rolled)
                self.move_token(player_playing, 'q', dice_rolled)
            else:
                self.move_token(player_playing, 'p', dice_rolled)
        elif finish_dis_p > finish_dis_q and (player_token_p != -1 and player_token_q != -1):
            self.move_token(player_playing, 'p', dice_rolled)
        elif finish_dis_q > finish_dis_p and (player_token_p != -1 and player_token_q != -1):
            self.move_token(player_playing, 'q', dice_rolled)

        # Rule 5. (Unsaid rule for everything else)
        elif player_token_p == -1:
            self.move_token(player_playing, 'q', dice_rolled)
        elif player_token_q == -1:
            self.move_token(player_playing, 'p', dice_rolled)


"""
players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
         ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
player_A = game.get_player_by_position('A')
print(player_A.get_completed())
print(player_A.get_token_p_step_count())
print(current_tokens_space)
player_B = game.get_player_by_position('B')
print(player_B.get_space_name(45))
"""


"""
# CASE 1
players = ['A','B','C','D']
turns = [('A', 6),('A', 1),('B', 6),('B', 2),('C', 6),('C', 3),('D', 6),('D', 4)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['1', 'H', '16', 'H', '31', 'H', '46', 'H']

# passed
"""

"""
# CASE 2
players = ['A','B']
turns = [('B', 6),('B', 4),('B', 5),('B', 4),('B', 4),('B', 3),('B', 4),('B', 5),('B', 4),('B', 4),('B', 5),('B', 4),('B', 1),('B', 4),('B', 5),('B', 5),('B', 5)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['H', 'H', 'B6', 'H']

# passed
"""

"""
# CASE 3
players = ['A','B']
turns = [('A', 6),('A', 3),('A', 6),('A', 3),('A', 6),('A', 5),('A', 4),('A', 6),('A', 4)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['28', '28', 'H', 'H']

# passed
"""
"""
# CASE 4
players = ['A','C']
turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 5),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('C', 6),('C', 4)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['33', 'H', '32', 'H']

# passed
"""

"""
# CASE 5
players = ['A','B']
turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 5),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 3),('A', 6),('B', 6),('A', 6)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['E', 'E', 'R', 'H']

# passed

"""
"""
# CASE 6
players = ['A','B']
turns = [('A', 6),('A', 2),('A', 2),('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('B', 6),('B', 3),('A', 6),('A', 3)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['3', 'H', '17', 'H']

# passed
"""
"""
# CASE 7
players = ['A','B']
turns = [('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('A', 4),('A', 5),('A', 4),('A', 5),('A', 5),('A', 3),('A', 5),('A', 3),('A', 6)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['A1', 'R', 'H', 'H']

# passed
"""
"""
# CASE 8
players = ['A','B']
turns = [('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('A', 4),('A', 5),('A', 4),('A', 5),('A', 5),('A', 3),('A', 5),('A', 5),('A', 6),('A', 5),('A', 5),('A', 3),('B', 6),('B', 3),('A', 4)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['E', '13', '17', 'H']

# passed
"""
"""
# CASE 9
players = ['A','B']
turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 6),('A', 5),('A', 3),('B', 6),('B', 2),('A', 2),('A', 4)]

game = LudoGame()
current_tokens_space = game.play_game(players, turns)

print(current_tokens_space)

# EXPECTED
# ['16', '10', 'H', 'H']

# passed
"""
"""
game = LudoGame()

players = ['A', 'B']

turns = [('A', 6), ('A', 5), ('A', 6), ('A', 4), ('B', 6), ('B', 6), ('B', 2), ('B', 2), ('A', 6), ('A', 6)]

current_tokens_space = game.play_game(players, turns)

print(current_tokens_space) # ['5', '16', 'H', 'H']

player_B = game.get_player_by_position('B')

ret = player_B.get_token_p_step_count()

print(ret) # -1

"""