import sys

data = list(sys.stdin.read().strip().split(" "))

dp = {}


def stone_blink(stone, blink=0):
    stone_key = stone + "/" + str(blink)
    if blink == MAX_BLINK:
        return stone

    if stone in dp:
        return dp[stone_key]

    if stone == "0":
        dp[stone_key] = stone_blink("1", blink + 1)
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        dp[stone_key] = (
            stone_blink(str(int(stone[:mid])), blink + 1)
            + " "
            + stone_blink(str(int(stone[mid:])), blink + 1)
        )
    else:
        dp[stone_key] = stone_blink(str(2024 * int(stone)), blink + 1)
    return dp[stone_key]


MAX_BLINK = 25
print(sum(len(stone_blink(s).split()) for s in data))
