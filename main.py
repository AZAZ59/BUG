INF = int(1e9)
dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
if __name__ == '__main__':
    rows, cols = map(int, input().split())
    GameMap = []
    for y in range(rows):
        row = input()
        GameMap.append([])
        for x in range(cols):
            GameMap[-1].append(INF if row[x] == '@' else -1)
    ##########################
    ###      TEST OUT      ###
    ##########################
    x = y = 1
    queue = [(x, y)]
    while len(queue) != 0:
        x, y = queue.pop()
        GameMap[y][x] = 0
        for dx, dy in dirs:
            if GameMap[y + dy][x + dx] == -1:
                queue.append((x + dx, y + dy))
    if GameMap[-2][-2] != 0:
        print('-1')
        exit(0)
    x = y = 1
    curDir = 0
    step = 0
    while y != rows - 2 or x != cols - 2:
        step += 1
        GameMap[y][x] += 1

        dx, dy = dirs[curDir]

        min_count = GameMap[y + dy][x + dx]
        for dx, dy in dirs:
            if GameMap[y + dy][x + dx] < min_count:
                min_count = GameMap[y + dy][x + dx]
        ## minimum
        dx, dy = dirs[curDir]
        if GameMap[y + dy][x + dx] == min_count:
            x += dx
            y += dy
            continue
        ## eq direction

        for dir_, (dx, dy) in enumerate(dirs):
            if GameMap[y + dy][x + dx] == min_count:
                curDir = dir_
                x += dx
                y += dy
                break
    print(step)