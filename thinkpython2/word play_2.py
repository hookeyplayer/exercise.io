# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:59:22 2020

@author: xiaofan
"""
from urllib.request import urlopen
import time
target_url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt'
# =============================================================================
# compare speed of appending methods
# =============================================================================

line = fin.readlines() # list
test = fin.readline() # bytes
#%%
def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = urlopen(target_url)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
#%%
def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = urlopen(target_url)
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t
#%%
start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')
#%%
start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

# =============================================================================
# Binary search word
# =============================================================================
import bisect
from urllib.request import urlopen
target_url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt'
#%%
def make_word_list():
    """Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin = urlopen(target_url)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list
#%%
def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)
#%%
def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word
#%%
if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))
# =============================================================================
# reverse pair
# =============================================================================
from inlist import in_bisect, make_word_list

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.
    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])

# =============================================================================
# interlock
# =============================================================================
def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.
    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
#%%        
def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.
    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
#%%
if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
