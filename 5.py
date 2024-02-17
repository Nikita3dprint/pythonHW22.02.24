for n in range(1, 200):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '0'
    else:
        b += '1'
    if b.count('1') % 3 == 0:
        b = '11' + b[2:]
    else:
        b = '10' + b[2:]
    r =