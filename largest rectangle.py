def largestRectangle(h):
    maxx = 0
    for building in range(len(h)):
        left = building - 1
        right = building + 1
        number_of_buildings = 1
        while True:
            if left == -1:
                break
            if h[left] < h[building]:
                break
            left -= 1
            number_of_buildings += 1
        while True:
            if right == len(h):
                break
            if h[right] < h[building]:
                break
            right += 1
            number_of_buildings += 1
        temp = h[building] * number_of_buildings
        if temp > maxx:
            maxx = temp

    return maxx


if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split()))
    result = largestRectangle(h)
    print(result)