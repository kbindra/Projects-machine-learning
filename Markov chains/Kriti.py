import numpy as np
import matplotlib.pyplot as plt
import random

f = open("/home/kriti/Desktop/self practice/Apna time aega/Apna Time Aayega.txt", 'r')
lr = f.read()
f.close()

lr = lr.split("\n")
song = '\n'
song = song.join(lr).lower()


T = {}

order=4

for ix in range(len(song)-order):
    ## current context
    ctx = song[ix:ix+4]
    
    next_word = song[ix+order]
    
    if T.get(ctx) is None:
        T[ctx] = {}
        T[ctx][next_word] = 1
    else:
        if T[ctx].get(next_word) is None:
            T[ctx][next_word] = 1
        else:
            T[ctx][next_word] += 1

for kx in T.keys():
    s = float(sum(T[kx].values()))
    
    for k in T[kx].keys():
        T[kx][k] = T[kx][k]/s

def generate_text(ctx):
    
    possible = T.get(ctx)
    
    if possible is None:
        return " "
    
    keys = list(possible.keys())
    random.seed(11)
    random.shuffle(keys)
    
    keys_probs = [possible[kx] for kx in keys]
#     print(keys_probs)
    
    return np.random.choice(keys, p=keys_probs )

ctx = "apna"

sentence = "" + ctx
order = 4
for ix in range(2000):
    
    nxt = generate_text(ctx)
    sentence += nxt
    ctx = sentence[-order:]
    
print(sentence)
