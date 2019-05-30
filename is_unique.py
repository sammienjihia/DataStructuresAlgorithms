

# the set() function shall return an iterable of the string with no duplicate elements.

def is_unique(s):
    if len(set(s)) == len(s):
        return True
    else:
        return False


str1 = "unique"
str2 = "bear"

print(is_unique(str1))
print(is_unique(str2))