def binary_search(arr, n, lo, hi):
    lo = 0
    hi = len(arr)
    steps = 0

    while lo < hi: 
        steps += 1
        mid = int((lo+hi)/2)

        if arr[mid] == n:
            print("Quantidade de buscas: ", steps)
            return mid     
        elif arr[mid] < n:
            lo = mid+1
        else:
            hi = mid
    return -1

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

binary_search(a, 3, 0, len(a))
binary_search(b, 3, 0, len(b))
binary_search(c, 3, 0, len(c))
binary_search(d, 3, 0, len(d))

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2

    if arr[i] == target:
        return i

    return binary_search(arr, target, i//2, min(i, n-1))

arr = list(range(1, 41))
target = 32
result = exponential_search(arr, target)

print(f"Elemento encontrado no indice {result}")