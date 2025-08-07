listN = [5.0, 10.0, 3.0, 6.0, 8.0]

def convert (i):
    return i / 2.5 # Whatever/10 = x/4 ---> (Whaterever * 4) / 10

converted = map(convert, listN) 
print(list(converted))