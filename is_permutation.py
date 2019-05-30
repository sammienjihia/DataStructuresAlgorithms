


def is_permutation(str1, str2):
    # remove spaces
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Check if the lengths of the strings are equal to each other. If not then str1 not a valid permutation of str2
    if len(str1) != len(str2):
        return False

    for chr in str1:
        if chr in str2:
            str2 = str2.replace(chr, "")

    if len(str2) == 0:
        return True

    else:
        return False


str1 = "driving"
str2 = "driivng"

print(is_permutation(str1, str2))