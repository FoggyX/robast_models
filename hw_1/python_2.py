def main():
    arr_string = input("arr (numbers separated by commas): ")

    arr = [int(x) for x in arr_string.split(',')]

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    count = 0
    length = len(arr)
    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    print(count)


if __name__ == '__main__':
    main()
