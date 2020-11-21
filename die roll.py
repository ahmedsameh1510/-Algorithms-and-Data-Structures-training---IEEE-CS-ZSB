if __name__ == '__main__':
    y, w = map(int, input().split())
    numerator = (max(y, w)-1)
    if numerator == 0 or numerator == 6:
        print(numerator, '/1', sep="")
    elif numerator == 1 or numerator == 5:
        print(numerator, '/6', sep="")
    elif numerator == 2 or numerator == 4:
        print(numerator/2, '/3', sep="")
    else:
        print('1/2')