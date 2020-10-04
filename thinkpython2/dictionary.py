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

# =============================================================================
#  official edition
# =============================================================================

def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.
    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.
    d: dict
    Returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)    
    
    
    
    
    
    
    
    
