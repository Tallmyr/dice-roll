import time
from collections import Counter


def roll(seed: int, rolls: int):
    seed1 = seed
    roll = []
    for _ in range(rolls):
        digits = map(int, str(seed1))
        for x in digits:
            if x != 0:
                seed1 **= x
                seed1 = int(str(seed1)[:17])
        roll.append(seed1 % 6)
    return roll


def seed():
    seed = str(time.time())
    seed = seed.replace(".", "")
    seed = int(seed)
    return seed


def tester(rolls: int):
    result: list = roll(seed(), rolls)
    count = Counter(result).values()
    percentage = []
    for x in count:
        p = (x / rolls) * 100
        percentage.append(p)
    print(percentage)
