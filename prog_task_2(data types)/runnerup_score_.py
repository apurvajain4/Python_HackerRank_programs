if __name__ == '__main__':
    num = int(input())
    array = list(map(int, input().split()))
    max = max(array)
    score = None
    for num in array:
        if num == max:
            pass
        elif score == None:
            score = num
        elif num > score:
            score = num
    print(score)