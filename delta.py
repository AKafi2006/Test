in1 = int(input())

if in1 >= 3 and in1 <= 20:
    f = 1

    while f < in1:
        if f == 1:
            print((in1 - 1) * '.', end = '')
            print('D' , end = '')
            print((in1 - 1) * '.' , end = '')
            print()
        else:
            print((in1 - f) * '.', end = '')
            print('D' , end = '')
            print(((2 * (f - 1)) - 1) * '.' , end = '')
            print('D' , end = '')
            print((in1 - f) * '.', end = '')
            print()

        f += 1

    print('D' , end = '')
    print((in1 - 1) * '.D')