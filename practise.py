# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 19:41:14 2022

@author: ASUS
"""

""" Son topish o'yini """

import random

def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    taxminlar = 0
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        if tasodifiy_son<taxmin:
            print("Xato men o'ylagan son bundan kichikroq, yana urunib ko'ring")
        elif tasodifiy_son>taxmin:
            print("Xato men o'ylagan son bundan kattaroq, yana urinib ko'ring")
        else:
            print(f"Tabriklayman siz {taxminlar} ta taxmin bilan topdingiz men o'ylagan son {tasodifiy_son} edi")
    return taxminlar        

def son_top_pc(x=10):
    input(f"Siz 1 dan {x} gacha son o'ylang. Men topaman! o'ylagan bo'lsez biror tugmani bosing!")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
       # input("Son o'ylagan bo'lsangiz biror tugmani bosing!")
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz, agar to'g'ri bo'lsa (t)"
                      f"kichik bo'lsa (-) , katta bo'lsa (+) ni bosing".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar
            
def play(x=10):
    yana = True
    while yana:
       taxminlar_user = son_top(x)
       taxminlar_pc = son_top_pc(x)
    
       if taxminlar_user<taxminlar_pc:
          print(f"tabriklayman siz {taxminlar_user} ta taxmin yutdingiz")
       elif taxminlar_user>taxminlar_pc:
           print(f"Men {taxminlar_pc} ta taxmin bilan yutdim")
       else:
           print("Durrang!")
       yana = int(input(f"yana o'ynaymizmi yes(1)/no(0) ni bosing"))



        
    
       
        

















