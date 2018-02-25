"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random

#import logging
##logger = logging.getLogger(__name__)
##logger.setLevel(logging.DEBUG)
#fh = logging.FileHandler('solution.log')
#fh.setLevel(logging.DEBUG)
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#fh.setFormatter(formatter)
#ch.setFormatter(formatter)
##logger.addHandler(fh)
##logger.addHandler(ch)


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    #w, h = game.width / 2., game.height / 2.
    own_y,own_x=game.get_player_location(player)
    opponent_y, opponent_x = game.get_player_location(game.get_opponent(player))

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return own_moves - 1/float((own_y - opponent_y)**2 + (own_x - opponent_x)**2)* opp_moves



def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(game.get_opponent(player))

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return own_moves - (1/float((h - y)**2 + (w - x)**2))*opp_moves

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)


    return float(1/((h - y)**2 + (w - x)**2)*(own_moves) - opp_moves)



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout




class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    #def __init__(self, search_depth, score_fn, timeout=10.):

    #    IsolationPlayer.__init__(self,search_depth, score_fn, timeout=10. )



    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            return self.minimax(game, self.search_depth -1) #RIMA togli sto -1

        except SearchTimeout:
            ##logger.info('####*Get_move - Time Out, Do Something!!!!!!')
            #return best_move
            moves=game.get_legal_moves()
            return moves[0]   # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def min_play(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            ##logger("****Min Play: Time over my not so friend****")
            #.info("Min Play, Time Left: %s. Timer Threshold: %s", self.time_left(),self.TIMER_THRESHOLD )
            #return self.score(game, self)
            raise SearchTimeout()
        if (not game.get_legal_moves()) or depth==0:
            ###logger.info("**Min Play, Game Over? %s or reached depth 0? %s", game.is_game_over(), depth)
            ##logger.info("***Min Play, Score: %s", self.score(game,self))
            return self.score(game, self)
        moves = game.get_legal_moves()
        ##logger.info("**Min Playing, at level %s. Legal Moves: %s", depth, moves)
        best_score = float('inf')
        for move in moves:
            game_cloned = game.forecast_move(move)
            #print(game_cloned.to_string())
            score = self.max_play(game_cloned, (depth-1))
            if score < best_score:
                best_move = move
                best_score = score
        return best_score


    def max_play(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            #logger.info("Max Play, Time Left: %s. Timer Threshold: %s", self.time_left(),self.TIMER_THRESHOLD )
            #return self.score(game, self)
            #return self.score(game, self)
            raise SearchTimeout()
        if (not game.get_legal_moves()) or depth==0:
            ##logger.info("**Max Play, Game Over? %s or reached depth 0? %s", game.is_game_over(), depth)
            #logger.info("***Max Play, Score: %s", self.score(game,self))
            return self.score(game, self)
        moves = game.get_legal_moves()
        #logger.info("Max Playing, at level %s. Legal Moves: %s", depth, moves)
        best_score = float('-inf')
        for move in moves:
            game_cloned = game.forecast_move(move)
            #print(game_cloned.to_string())
            score = self.min_play(game_cloned, (depth -1))
            if score > best_score:
                best_move = move
                best_score = score
        return best_score


    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        moves=game.get_legal_moves()
        ##logger.info("moves: %s", moves)

        #best_move=moves[0]
        best_move=(-1,-1)
        best_score=float('-inf')

        for move in moves:
            if self.time_left() < self.TIMER_THRESHOLD:
                return best_move

            #logger.info("***Minimax***Considering move: %s" , move)
            game_cloned=game.forecast_move(move)
            ##print(game_cloned.to_string())

            score=self.min_play(game_cloned, (depth -1))
            #logger.info("***Minimax***Score would be: %s", score)
            if score > best_score:
                best_move=move
                best_score=score
        return best_move





class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """
    #def __init__(self, search_depth, score_fn, timeout=10.):
        #IsolationPlayer.__init__(self,search_depth, score_fn, timeout=10. )



    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the cuclsrrent state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # how it was, working fine, changing now for iterarive deepening
            #return self.alphabeta(game, self.search_depth -1)

                for depth in range (1,game.width*game.height):
                    if self.time_left() < self.TIMER_THRESHOLD:
                        raise SearchTimeout()
                    best_move= self.alphabeta(game, depth)
                    #if best_move !=(-1,-1):
                    #    break

        except SearchTimeout:
            ##logger.info('####*Get_move - Time Out, Do Something!!!!!!')
            #return best_move
            moves=game.get_legal_moves()
            return moves[0]   # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration

        return best_move

        #inizio minimax rima 08/08/2017
    def min_play_alphabeta(self, game, depth,alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if (not game.get_legal_moves()) or depth==0:
            #logger.info("Evaluating node")
            return self.score(game, self)
        moves = game.get_legal_moves()
        best_score = float('inf')
        for move in moves:
            game_cloned = game.forecast_move(move)
            #print(game_cloned.to_string())
            #logger.info("Min considering move: %s", move)
            score = self.max_play_alphabeta(game_cloned, (depth-1), alpha, beta)

            if score < best_score:
                best_score = score
            if score < beta:
                beta=score
            if alpha>=beta:
            #    logger.info("!!!!!!!!!Min, Pruning: %s?",move)
                break

            #logger.info("Min Alpha: %s, Beta: %s", alpha, beta)
        return best_score


    def max_play_alphabeta(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if (not game.get_legal_moves()) or depth==0:

            return self.score(game, self)
        moves = game.get_legal_moves()
        best_score = float('-inf')
        for move in moves:
            #logger.info("!!!!!!!!!!!!Max considering move: %s", move)
            game_cloned = game.forecast_move(move)
            #print(game_cloned.to_string())
            score = self.min_play_alphabeta(game_cloned, (depth -1), alpha,beta)

            if score > best_score:
                best_score = score
            if score > alpha:
                alpha=score
            if alpha>=beta:
            #    logger.info("Max, Pruning: %s?",move)
                break

            #logger.info("Max Alpha: %s, Beta: %s", alpha, beta)
        return best_score


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        moves=game.get_legal_moves()
        ##logger.info("moves: %s", moves)

        #best_move=moves[0]
        best_move=(-1,-1)
        best_score=float('-inf')

        for move in moves:
            if self.time_left() < self.TIMER_THRESHOLD:
                return best_move

            #logger.info("***Minimax***Considering move: %s" , move)
            game_cloned=game.forecast_move(move)
            ##print(game_cloned.to_string())

            score=self.min_play_alphabeta(game_cloned, (depth -1),alpha,beta)
            #logger.info("***Minimax***Score would be: %s", score)
            if score > best_score:
                best_move=move
                best_score=score
            

            if score > alpha:
                alpha=score
            #logger.info("Top Level, score of move: %s",score)
            #logger.info("Top Level Alpha: %s, Beta: %s", alpha, beta)
            if alpha>=beta:
                #logger.info("Top Level, Pruning: %s?",move)
                break
        return best_move
