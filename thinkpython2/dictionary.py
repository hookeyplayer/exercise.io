# =============================================================================
#  count frequency in the word
# =============================================================================
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] =  1
        else:
            d[c] += 1
    return d

h = histogram('Sarcastic')
#print(h)
# =============================================================================
#  print dictionary
# =============================================================================
def print_dictionary(s):
    for c in s:
        print(c, s[c])
print_dictionary(h)
# =============================================================================
# reverse lookup
# =============================================================================
# 已知出现v次，查是哪个字母
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
        raise LookupError('value doesnt appear in dictionary')
        
reverse_lookup(h, 3)

# =============================================================================
# inverse dictionary
# =============================================================================
def inverse(s):
    inverse = dict()
    for key in s:
        val = s[key]
        if val not in inverse:
            inverse[val] = [key]
        else:   
            inverse[val].append(key)
    return inverse
test = inverse(h)
print(type(test))
test
    
    
    
    
    
    
    
    
    
    