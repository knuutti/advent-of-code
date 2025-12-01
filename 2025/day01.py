def turn(current: int, direction: str, distance: int) -> int:
    current_start = current
    if direction == "R":
        current += distance
    else:
        current -= distance
    clicks = abs(current // 100)
    current %= 100

    if current == 0 and direction == "L": clicks += 1

    if current_start == 0 and direction == "L": clicks -= 1

    return current, clicks

fname = "day01.txt"
file = open(fname, 'r')
data = file.read().splitlines()

current = 50
zeros = 0
total_clicks = 0

for action in data:
    direction = action[0]
    distance = int(action[1:])
    current, clicks = turn(current, direction, distance)
    total_clicks += clicks
    if current == 0: zeros += 1

print("Silver:", zeros)
print("Gold:", total_clicks)

