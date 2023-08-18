import random


def roll_dice(*args, simulation_time: int = 100000):
    res = {}
    for _ in range(simulation_time):
        total = 0
        for dice in args:
            total += random.randint(1, dice)
        if total in res:
            res[total] += 1
        else:
            res[total] = 1

    for each, count in sorted(res.items()):
        print(f"{each} : {count/100000*100:.4}%")


# commands used in solution video for reference
if __name__ == '__main__':
    roll_dice(4, 6, 6)
    print("-----------")
    roll_dice(4, 6, 6, 20)
