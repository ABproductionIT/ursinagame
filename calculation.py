def checkWinner(cube, X, O, level):
    for i in cube:
        # 2d ankyunagic
        count = 0
        for y in range(len(cube)):
            count += i[y, y]
        if count == X * level:
            return 'x'
        if count == O * level:
            return 'o'

        count = 0
        for y in reversed(range(len(cube))):
            count += i[y, (len(cube) - y - 1)]

        if count == X * level:
            return 'x'
        if count == O * level:
            return 'o'

# bolor 2dy-gcovner@
        for y in range(len(cube)):
            count = 0
            for j in i:
                count += j[y]

            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'

        # bolor 2dx-gcovner@
        for j in i:
            count = 0
            for k in j:
                count += k

            if count == X*level:
                return 'x'
            if count == O*level:
                return 'o'

# cankacac 3dy
    for y1 in range(len(cube)):
        for y2 in range(len(cube)):
            count = 0
            for y3 in range(len(cube)):
                count += cube[y3, y2, y1]

            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'

    for y in range(len(cube)):
        for y2 in range(len(cube)):
            count = 0
            l = 0
            for y3 in range(len(cube)):
                count += cube[l, y, l]
                l += 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'

    #new
    for y in range(len(cube)):
        for y2 in range(len(cube)):
            count = 0
            l = 0;
            j = len(cube) - 1
            for y3 in range(len(cube)):
                count += cube[j][y][l]
                l += 1
                j -= 1
            if (count == X * level):
                return 'x'
            if (count == O * level):
                return 'o'

    for y in range(len(cube)):
        for y2 in range(len(cube)):
            count = 0
            l = 0
            for y3 in range(len(cube)):
                count += cube[l, l, y]
                l += 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'
    #new
    for y in range(len(cube)):
        for y2 in range(len(cube)):
            count = 0
            l = 0;
            j = len(cube) - 1;
            for y3 in range(len(cube)):
                count += cube[l][j][y]
                l += 1
                j -= 1
            if (count == X * level):
                return 'x'
            if (count == O * level):
                return 'o'
    # mejtexi ankyunagcer, palubomu 4 ankyunica linelu, aysinqn 4 hat stuguma petq
    for y in [[0, 0], [0, len(cube) - 1], [len(cube) - 1, 0], [len(cube) - 1, len(cube) - 1]]:
        # stugum amenarajin nerqevi dzax kubikic depi verevi aj verji
        if y[0] == 0 and y[1] == 0:
            count = 0
            l = 0
            for y3 in range(len(cube)):
                count += cube[l, l, l]
                l += 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'
        if y[0] == 0 and y[1] == len(cube) - 1:
            count = 0
            l = len(cube) - 1
            for y3 in range(len(cube)):
                count += cube[y3, y3, l]
                l -= 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'
        if y[0] == len(cube) - 1 and y[1] == 0:
            count = 0
            l = len(cube) - 1
            for y3 in range(len(cube)):
                count += cube[y3, l, y3]
                l -= 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'
        if y[0] == len(cube) - 1 and y[1] == len(cube) - 1:
            count = 0
            l = len(cube) - 1
            for y3 in range(len(cube)):
                count += cube[l, y3, y3]
                l -= 1
            if count == X * level:
                return 'x'
            if count == O * level:
                return 'o'

    return
