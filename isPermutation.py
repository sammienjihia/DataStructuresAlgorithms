string1 = "driving"
string2 = "drivign"

def is_permutation(stringA, stringB):
    # clean the string. Remove spaces
    stringA = stringA.replace(" ", "")
    stringA = stringA.replace(" ", "")

    # compare the lengths
    if len(stringA) != len(stringB):
        return False

    for char in stringA:
        if char in stringB:
            # remove the character from stringB
            stringB.replace(char, "")

    return len(stringB) == 0

print(is_permutation("stringA", "stringB"))