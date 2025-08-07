arr = [125, 12, 86, 47, 38]

def sorting_array(arr):
    sorted = []
    while arr:
        minimun = min(arr)
        sorted.append(minimun)
        arr.remove(minimun)
    return sorted

print(sorting_array(arr))