path = input("/")

def path_finder(path):
    output = []
    directors = path.split("/")
    for director in directors:
        if director == "" or director == ".":
            continue
        elif director == "..":
            if output:
                output.pop()
        else:
            output.append(director)
    return "/".join(output)

print(f"/{path_finder(path)}")