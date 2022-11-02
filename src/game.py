import random

from .player_info import Player


class Game:
    def __init__(self, players: list[Player]):
        self.all_players = players
        self.alive_players = players.copy()
        self.ranks = []
        self.size = len(players) - 1
        self.winner = self.all_players[0]

    def initialize(self):
        self.alive_players = self.all_players.copy()
        self.ranks = []

    def play_game(self):
        for _ in range(self.size):
            [p1, p2] = random.sample(self.alive_players, 2)

            self.play_round(p1, p2)

        # Declare the winner of the game at the end of the rounds
        winner = self.alive_players[0]
        self.winner = winner
        winner.wins += 1
        winner.game_kills = 0  # Reset
        winner.ranks.append(1)
        self.ranks.append(winner)

    def play_round(self, p1: Player, p2: Player):
        """
        Play round between 2 players
        """
        kd_1 = p1.kd
        kd_2 = p2.kd

        threshold = kd_1 / (kd_1 + kd_2)

        while True:
            if random.random() < threshold:
                shooter, target = p1, p2
            else:
                shooter, target = p2, p1

            for _ in range(5):  # Shoot 5 times
                shot = shooter.shoot()
                if shot == 20:
                    shooter.headshots += 1
                elif shot == 10:
                    shooter.body_shots += 1
                target.hb -= shot
                if target.hb <= 0:
                    # Loser
                    rank = len(self.alive_players)
                    if rank <= 5:
                        target.top_5 += 1
                    elif rank <= 10:
                        target.top_10 += 1
                    elif rank <= 25:
                        target.top_25 += 1
                    elif rank <= 50:
                        target.top_50 += 1
                    elif rank <= 75:
                        target.top_75 += 1

                    target.ranks.append(rank)
                    self.alive_players.remove(target)
                    self.ranks.append(target)
                    target.deaths += 1
                    target.hb = 100
                    target_game_kills = target.game_kills
                    target.game_kills = 0

                    # Winner
                    shooter.hb = 100
                    shooter.game_kills += 1
                    if shot == 20:
                        shooter.kill_headshots += 1
                    else:
                        shooter.kills += 1

                    if self.winner == target:
                        shooter.king_slayer += 1
                    if target_game_kills >= 3:
                        shooter.three_killer += 1


                    return







