# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:18:48 2018

@author: Akshay Jagadale
"""

def rev_word(s):
    
    word = ''
    rlist = []
    for i in reversed(range(len(s))):
        if s[i] != ' ':
            word += s[i]
        if (s[i] == ' ' and s[i+1] != ' ') or (i == 0 and s[1] != ' '):
            rlist.append(word[::-1]) 
            word = ''
    return ' '.join(rlist)

print(rev_word('Hi John,                        are you ready to go?'))