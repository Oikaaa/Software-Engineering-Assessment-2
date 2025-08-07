district = ["BD", "BTL", "CG", "DD", "HBT"]
population = [247100, 333300, 266800, 420900, 318000]

def max(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max

def min(arr):
    min = 1000000000000000000000000000000000000000000000000000000000
    for i in arr:
        if i < min:
            min = i
    return min

highest = max(population)
lowest = min(population)
print(f"Most populated dist: {population.index(highest)}")
print(f"Most populated dist: {population.index(lowest)}")
print(f"Most populated dist: {district[population.index(highest)]}")
print(f"Most populated dist: {district[population.index(lowest)]}")