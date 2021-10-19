import random

def setFigurCordinates(cube, value):
    v = {}
    for i in range(len(cube)):
        v[i+1] = []

    for i in range(len(cube)):
        # 2d ankyunagic
        xCount = []
        oCount = []
        nCount = []
        for y in range(len(cube)):
            if cube[i][y][y] == 1:
                xCount.append([i,y,y])
            elif cube[i][y][y] == value:
                oCount.append([i,y,y])
            else:
                nCount.append([i,y,y])

        if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
            v[len(cube) - len(xCount)].append(random.choice(nCount))

        xCount = []
        oCount = []
        nCount = []
        for y in reversed(range(len(cube))):
            if cube[i][y][len(cube)- y - 1] == 1:
                xCount.append([i, y, len(cube)- y - 1])
            elif cube[i][y][y] == value:
                oCount.append([i, y, len(cube)- y - 1])
            else:
                nCount.append([i, y, len(cube)- y - 1])

        if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
            v[len(cube) - len(xCount)].append(random.choice(nCount))

        for y in range(len(cube)):
            xCount = []
            oCount = []
            nCount = []
            for j in range(len(cube)):
                if cube[i][j][y] == 1:
                    xCount.append([i, j, y])
                elif cube[i][j][y] == value:
                    oCount.append([i, j, y])
                else:
                    nCount.append([i, j, y])

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

        for j in range(len(cube[i])):
            xCount = []
            oCount = []
            nCount = []
            for y in  range(len(cube[i][j])):
                if cube[i][j][y] == 1:
                    xCount.append([i, j, y])
                elif cube[i][j][y] == value:
                    oCount.append([i, j, y])
                else:
                    nCount.append([i, j, y])

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for j in range(len(cube)):
        for y in range(len(cube)):
            xCount = []
            oCount = []
            nCount = []
            for i in range(len(cube)):
                if cube[i][y][j] == 1:
                    xCount.append([i, y, j])
                elif cube[i][y][j] == value:
                    oCount.append([i, y, j])
                else:
                    nCount.append([i, y, j])

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for y in range(len(cube)):
        for y2 in range(len(cube)):
            l = 0;
            xCount = []
            oCount = []
            nCount = []
            for y3 in range(len(cube)):
                if cube[l][y][l] == 1:
                    xCount.append([l, y, l])
                elif cube[l][y][l] == value:
                    oCount.append([l, y, l])
                else:
                    nCount.append([l, y, l])
                l+=1

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for y in range(len(cube)):
        for y2 in range(len(cube)):
            l = 0;
            xCount = []
            oCount = []
            nCount = []
            for y3 in range(len(cube)):
                if cube[l][l][y] == 1:
                    xCount.append([l, l, y])
                elif cube[l][l][y] == value:
                    oCount.append([l, l, y])
                else:
                    nCount.append([l, l, y])
                l+=1

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for y in range(len(cube)):
        for y2 in range(len(cube)):
            l = 0;
            j = len(cube) - 1
            xCount = []
            oCount = []
            nCount = []
            for y3 in range(len(cube)):
                if cube[j][y][l] == 1:
                    xCount.append([j, y, l])
                elif cube[j][y][l] == value:
                    oCount.append([j, y, l])
                else:
                    nCount.append([j, y, l])
                l += 1
                j -= 1
            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))
    for y in range(len(cube)):
        for y2 in range(len(cube)):
            l = 0;
            j = len(cube) - 1;
            xCount = []
            oCount = []
            nCount = []
            for y3 in range(len(cube)):
                if cube[l][j][y] == 1:
                    xCount.append([l, j, y])
                elif cube[l][j][y] == value:
                    oCount.append([l, j, y])
                else:
                    nCount.append([l, j, y])
                l += 1
                j -= 1

            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for y in [[0, 0], [0, len(cube) - 1], [len(cube) - 1, 0], [len(cube) - 1, len(cube) - 1]]:
        if (y[0] == 0 and y[1] == 0):
            l = 0;
            xCount = []
            oCount = []
            nCount = []
            for y3 in range(len(cube)):
                if cube[l][l][l] == 1:
                    xCount.append([l, l, l])
                elif cube[l][l][l] == value:
                    oCount.append([l, l, l])
                else:
                    nCount.append([l, l, l])
                l += 1
            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))
        if (y[0] == 0 and y[1] == len(cube) - 1):
            xCount = []
            oCount = []
            nCount = []
            l = len(cube) - 1;
            for y3 in range(len(cube)):
                if cube[y3][y3][l] == 1:
                    xCount.append([y3, y3, l])
                elif cube[y3][y3][l] == value:
                    oCount.append([y3, y3, l])
                else:
                    nCount.append([y3, y3, l])
                l -= 1
            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))
        if (y[0] == len(cube) - 1 and y[1] == 0):
            xCount = []
            oCount = []
            nCount = []
            l = len(cube) - 1;
            for y3 in range(len(cube)):
                if cube[y3][l][y3] == 1:
                    xCount.append([y3, l, y3])
                elif cube[y3][l][y3] == value:
                    oCount.append([y3, l, y3])
                else:
                    nCount.append([y3, l, y3])
                l -= 1
            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

        if (y[0] == len(cube) - 1 and y[1] == len(cube) - 1):
            xCount = []
            oCount = []
            nCount = []
            l = len(cube) - 1;
            for y3 in range(len(cube)):
                if cube[l][y3][y3] == 1:
                    xCount.append([l, y3, y3])
                elif cube[l][y3][y3] == value:
                    oCount.append([l, y3, y3])
                else:
                    nCount.append([l, y3, y3])
                l -= 1
            if len(xCount) > 0 and len(oCount) == 0 and len(nCount) > 0:
                v[len(cube) - len(xCount)].append(random.choice(nCount))

    for i in range(len(cube)):
        if len(v[i+1]) > 0:
            return random.choice(v[i+1])

