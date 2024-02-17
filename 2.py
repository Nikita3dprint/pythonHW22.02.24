for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (y and (not x or w) and (x or (not w == z))) == 1:
                    print(x, y, z, w)

#0101 1
#0110 1

#0111 0
#1011 0
#1110 0

#0101
#0110
#1110
