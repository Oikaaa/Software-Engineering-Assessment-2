arr = ["blue", "red", "yellow"]
pos = int(input("Input position: "))
print(arr[pos - 1])

delPos = input("Item to delete: ")
if delPos.isnumeric():
    numbified = int(delPos)
    arr.pop(numbified - 1)
else:
    arr.remove(delPos)
print(f"New color list: {arr}")
