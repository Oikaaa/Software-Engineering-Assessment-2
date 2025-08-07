true_string = "{[()]}"
false_string = "{[(]]}"

def operation(string):
    boolean = False
    dictionary = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    if len(string) % 2 != 1:    
        try:
            for i in range(len(string)//2):
                if dictionary[string[i]] == string[-i - 1]:
                    boolean = True
                else:
                    boolean = False
                    return boolean
        except:
            boolean = False
    return boolean

print(operation(true_string))