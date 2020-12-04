def has_duplicates(t):
    # make a copy of t
    s = t[:]
    s.sort()
    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
has_duplicates([1, 9, 8, 8])