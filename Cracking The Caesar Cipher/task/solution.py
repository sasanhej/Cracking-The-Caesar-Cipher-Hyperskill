import string
import itertools
import tqdm
import numpy as np

def caesar(shift):
    caesarlist = string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift]
    return {caesarlist[i]: string.ascii_lowercase[i] for i in range(26)}


def decipher(code, shift):
    mahsa = code.split()
    msg = ""
    for i in mahsa:
        msg += caesar(shift)[i]
    return msg.replace('x', ' ')


def findshift(code):
    for i in range(26):
        if 'butterscotch' in decipher(code, i):
            return i


def veg(keyword):
    vegdict = {string.ascii_lowercase[i]: i for i in range(26)}
    keylist=[]
    for i in keyword:
        keylist.append(vegdict[i.lower()])
    return tuple(keylist)


def vegen(keyword):
    vegdict = {string.ascii_lowercase[i]: 26-i for i in range(26)}
    keylist=[]
    for i in keyword:
        keylist.append(vegdict[i.lower()])
    return tuple(keylist)


def decveg(message, keyword):
    keylen = len(keyword)
    shifts = veg(keyword)
    msg = ""
    for i in range(len(message)):
        msg += caesar(shifts[i%keylen])[message[i]]
    return msg.replace("x", " ")


def encveg(message, keyword):
    message = message.replace(" ","x")
    keylen = len(keyword)
    shifts = vegen(keyword)
    msg = ""
    for i in range(len(message)):
        msg += caesar(shifts[i%keylen])[message[i]]
    return msg


def findveg(length,decoded,encoded):
    for prod in tqdm.tqdm(itertools.product(string.ascii_lowercase, repeat=length)):
        keyword = ''.join(prod).lower()
        if decveg(encoded, keyword) == decoded:
            return keyword


def find_key(length, decoded, encoded):
    encoded = encoded.lower().replace(" ", "x")
    decoded = decoded.lower()
    ennum = [string.ascii_lowercase.index(x) for x in encoded]
    denum = [string.ascii_lowercase.index(x) for x in decoded]
    diff = [(ennum[i]-denum[i])%26 for i in range(len(ennum))]+((length-len(ennum)%length)%length)*[0]
    key = "".join([string.ascii_lowercase[x] for x in diff[:length]])
    return key


if __name__=='__main__':
    a1 = int(input())
    a2 = input().replace(" ","x")
    a3 = input().replace(" ","")
    a4 = input().replace(" ","")
    print(decveg(a4, find_key(a1, a2, a3)))
