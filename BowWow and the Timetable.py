def Binary_To_Decimal(binary):
    decimall=0
    for i in range(len(binary)):
        decimall+=int(binary[len(binary)-1-i])*2**i
    return decimall
def trains(decimall):
    number=0
    i=0
    while True:
        if decimall<=4**i:
            break
        number+=1
        i+=1
    return number

if __name__ == '__main__':
    binary=input()
    decimal=Binary_To_Decimal(binary)
    print(trains(decimal))