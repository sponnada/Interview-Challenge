#function that takes a positive integer and prints out a set of all the combinations of parentheses
def printCombo(number):
    set1 = []
    x = 0
    while x < number:
        set1.append("(")
        set1.append(")")
        x = x + 1
    perms = itertools.permutations(set1)
    blah = []
    for element in perms:
        blah.append(element)
    sets = []
    k = 0
    while k < len(blah):
        if blah[k] not in sets:
            if blah[k][0] == ")" or blah[k][-1] == "(":
                k = k + 1
            else:
                counter = 0
                for character in blah[k]:
                    if counter >=0:
                        if character == "(":
                            counter = counter + 1
                        else:   
                            counter = counter - 1
                if counter == 0:
                    sets.append(blah[k])
                    k = k + 1         
                else:
                    k = k + 1
                    
        else:
            k = k + 1
            
    for element in sets:
        new = ""
        for character in element:
            new = new + character
        print new