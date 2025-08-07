balls = ["b","r", "r","w","b","w","w", "r"]

def sorting_colors(arr):
    num_red = arr.count("r")
    num_white = arr.count("w")
    num_blue = arr.count("b")
    output = []
    for i in range(num_red):
        output.append("r")
    for i in range(num_white):
        output.append("w")
    for i in range(num_blue):
        output.append("b")
    return output

output = sorting_colors(balls)
print(output)
