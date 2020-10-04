# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 02:30:25 2020

@author: xiaofan
"""

# =============================================================================
# 1.search; 
# 2.looping with indices;
# =============================================================================
from urllib.request import urlopen
target_url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt'
fin = urlopen(target_url) # it's a file like object and works just like a file
line = fin.readline()
word = line.strip() # 去掉space
word
#%% 第一种版本test有没有字母e
def have_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
have_no_e('paint')
#%% 第二种版本test有没有字母e
def avoids(word, forbidden):
    if forbidden in word:
        return False
    else:
        return True
avoids('appretice', 't')
#%%
# for loop
def is_abecedarian_for(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True
is_abecedarian_for('asss')
#%%
's' < 's'
#%%
# if recursion
def is_abecedarian_recursion(word):
    test = word.lower()
    if len(test) <= 1:
        return True
    elif test[0] > test[1]:
        return False
    return is_abecedarian_recursion(test[1:])
is_abecedarian_recursion('assss')
#%%
'A' < 'a'
#%%
# palindrome
def is_pal(word):
    test = word.lower()
    if len(test) <= 1:
        return True
    elif test[0] != test[-1]:
        return False
    return is_pal(test[1:-1])
is_pal('Abka')
#%%
# palindrom second way
def is_palindrome(word):
    i = 0
    test = word.lower()
    j = len(test) - 1
    while i < j:
        if test[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True
#%%
# while loop
def is_abecedarian_while(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1
    return True
is_abecedarian_while('asss')

# =============================================================================
# traversal
# =============================================================================

a.isupper()
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
#%%
# travese one list and returns a new
fruit = 'apple'
def capitalize_all(t):
    new = []
    for chars in t:
        new.append(t.capitalize())
    return new
capitalize_all(fruit)
#%%
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
find('Jerry', 'e')

# Recursion: call itself
# Iteration: run block repeatedly
