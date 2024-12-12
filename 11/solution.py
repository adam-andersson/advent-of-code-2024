import sys

data = list(sys.stdin.read().strip().split(" "))

dp = {}


def stone_blink(stone, blink):
    if blink <= 0:
        return 1

    stone_key = (stone, blink)

    if stone_key in dp:
        return dp[stone_key]

    if stone == "0":
        dp[stone_key] = stone_blink("1", blink - 1)
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        dp[stone_key] = stone_blink(str(int(stone[:mid])), blink - 1) + stone_blink(
            str(int(stone[mid:])), blink - 1
        )
    else:
        dp[stone_key] = stone_blink(str(2024 * int(stone)), blink - 1)
    return dp[stone_key]


for blinks, part in zip((25, 75), (1, 2)):
    print(f"Part {part}:", sum([stone_blink(s, blinks) for s in data]))
