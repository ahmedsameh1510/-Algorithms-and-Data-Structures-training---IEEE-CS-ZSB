def rotateLeft(d, numbers):
    size=len(numbers)
    for i in range(d):
        numbers.append(None)
    for i in range(d):
        numbers[size+i]=numbers[i]
    for index in range(size):
        print(numbers[d+index],end=" ")

if __name__ == '__main__':
    n,d=map(int,input().split())
    numbers=list(map(int,input().split()))
    d=d%n
    rotateLeft(d, numbers)