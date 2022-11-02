from .game import Game
from .player_info import PlayerInfo, Player


def create_game(distribution):
    players = []

    for category, size in distribution.items():
        for _ in range(size):
            players.append(Player(category))

    game = Game(players)

    return players, game
