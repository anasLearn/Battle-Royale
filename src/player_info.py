from enum import Enum
import random


class PlayerInfo(Enum):
    PRO = ("pro", 5, 0.9)
    V_GOOD = ("very_good", 3, 0.75)
    GOOD = ("good", 1.85, 0.58)
    AVERAGE = ("average", 1.45, 0.5)
    BAD = ("bad", 0.75, 0.4)

    @staticmethod
    def get_cat_enum(cat):
        for info in PlayerInfo:
            if info.value[0] == cat:
                return info


class Player:
    def __init__(self, info):
        value = info.value
        self.category = value[0]
        self.kd = value[1]
        self.accuracy = value[2]
        self.hb = 100  # health bar
        self.kills = 0  # Kill without headshot
        self.deaths = 0
        self.headshots = 0
        self.body_shots = 0
        self.kill_headshots = 0
        self.ranks = []
        self.wins = 0
        self.top_75 = 0
        self.top_50 = 0
        self.top_25 = 0
        self.top_10 = 0
        self.top_5 = 0
        self.king_slayer = 0
        self.three_killer = 0
        self.game_kills = 0

    def shoot(self):
        """
        Returns how many points the player gets from shooting
        The accuracy is applied twice. First to check if the player hits, then to check if the player hits the head
        :return: 20: headshot, 10: body shot, 0: miss
        """
        if random.random() < self.accuracy:
            if random.random() < self.accuracy:
                return 20
            return 10
        return 0


if __name__ == "__main__":
    for info in PlayerInfo:
        print(info.value, "-", info)
