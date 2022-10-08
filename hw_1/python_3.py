import heapq

def main():
    arr_string = input("arr (numbers separated by commas): ")

    arr = [int(x) for x in arr_string.split(',')]

    k = int(input("k: "))
    hashmap = {}
    for number in arr:
        if number in hashmap:
            hashmap[number] += 1
        else:
            hashmap[number] = 1
    
    heap = []

    for key in hashmap:
        heapq.heappush(heap, (hashmap[key], key))
    
    res = [i[1] for i in heapq.nlargest(k, heap)]
    
    print(res)
    


if __name__ == '__main__':
    main()

