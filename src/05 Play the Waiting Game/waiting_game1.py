import time
import random


def waiting_game():
    goal = random.randint(2, 4)
    print(f"the goal is {goal}")

    input("-- type Enter to start --")
    start = time.time()

    input("-- click Enter to stop --")
    duration = time.time() - start

    print(f"start {start:.4}")
    print(f"duration {duration:.4}")

    if duration == goal:
        print("amazing ")
    elif duration < goal:
        print(f"faster {goal - duration:.4}")
    else:
        print(f"slower {duration - goal:.4}")


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
