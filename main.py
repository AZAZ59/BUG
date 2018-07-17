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
        GameMap[x][y] = 0
        for dx, dy in dirs:
            if GameMap[x + dx][y + dy] == -1:
                queue.append((x + dx, y + dy))
    if GameMap[-2][-2] != 0:
        print('-1')
        exit(0)
    x = y = 1
    curDir=0
    while y!=rows-1 and x != cols-1:
        pass

    for row in GameMap:
        print(''.join(list(map(lambda x: '@' if x > 100 else '.' if x == 0 else '!', row))))
        # print(rows, cols)
