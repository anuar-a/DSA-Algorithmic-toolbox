import sys
import tkinter as tk
from tkinter import *
from itertools import permutations,combinations
from functools import partial

def diff(a,b):
    count = 0
    #x = [int(z) for z in str(a)]
    #y = [int(z) for z in str(b)]
    x = abs(a - b)
    if x in (1000,100,10,1,2000,200,20,2,0):
        #print(a,b,x)
        return 1
    else:
        return 0

a = set(['1','2','3'])

def vicinity(a):
    res = set()
    '''for x in (1000,100,10,1,2000,200,20,2,0):
        res.append(min(abs(a+x),abs(a-x)))'''
    res.add(a)
    d1 = 0
    if a > 1000 and a < 2000:
        res.add(a+1000)
        res.add(a+2000)
        d1 = 1
    elif a > 2000 and a < 3000:
        res.add(a+1000)
        res.add(a-1000)
        d1 = 2
    else:
        res.add(a-2000)
        res.add(a-1000)
        d1 = 3

    d2 = 0
    if a - d1*1000 > 100 and a - d1*1000 < 200:
        res.add(a+100)
        res.add(a+200)
        d2 = 1
    elif a - d1*1000 > 200 and a - d1*1000 < 300:
        res.add(a+100)
        res.add(a-100)
        d2 = 2
    else:
        res.add(a-100)
        res.add(a-200)
        d2 = 3

    d3 = 0
    if a - d1*1000 - d2*100 > 10 and a - d1*1000 - d2*100 < 20:
        res.add(a+10)
        res.add(a+20)
        d3 = 1
    elif a - d1*1000 - d2*100 > 20 and a - d1*1000 - d2*100 < 30:
        res.add(a+10)
        res.add(a-10)
        d3 = 2
    else:
        res.add(a-10)
        res.add(a-20)
        d3 = 3

    if a - d1*1000 - d2*100 - d3*10 == 1:
        res.add(a+1)
        res.add(a+2)
    elif a - d1*1000 - d2*100 - d3*10 == 2:
        res.add(a+1)
        res.add(a-1)
    else:
        res.add(a-1)
        res.add(a-2)
    return res

b = [[0,1,0,1],
     [0,0,2,0],
     [0,2,1,2],
     [2,1,2,2],
     [2,0,1,1],
     [2,2,0,0],
     [1,1,1,0],
     [1,0,0,2],
     [1,2,2,1]]
c = set([1212,
     1131,
     1323,
     3233,
     3122,
     3311,
     2221,
     2113,
     2332])
d = set([3111,3332,2311,3213,3323,2113,2331,3313,2333])
ans = []
num = set()

for i in a:
    for j in a:
        for k in a:
            for l in a:
                '''for m in a:
                    for n in a:
                        for o in a:
                            for p in a:'''
                num.add(int(i+j+k+l))

#Frame definition
master = Tk()
master.resizable(False,False)

graphic = Frame(master,width = 300, height=400)
buttons = Frame(master,width = 200, height=400,bg = 'white')
graphic.pack(side = LEFT, fill = BOTH, expand = 1)
buttons.pack(side = LEFT, fill = BOTH, expand = 1)

#Canvas definition
canvas_width = 300
canvas_height = 300
w = Canvas(graphic, width=canvas_width, height=canvas_height)
w.pack(fill = BOTH, expand = 1)
offset = 10
size = 30
rectangles = dict()
for i in num:
    i = str(i)
    rectangles[int(i)] = w.create_rectangle(offset + 0 + (int(i[0])-1)*3*size + (int(i[2])-1)*size,
                                            canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3])-1)*size,
                                            offset + (int(i[0])-1)*3*size + int(i[2])*size,
                                            canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3]))*size,
                                            fill="#FFFFFF")
def create_table(tablek):
    for j in tablek:
        for i in vicinity(j):
            i = str(i)
            '''rect = w.create_rectangle(offset + 0 + (int(i[0])-1)*3*size + (int(i[2])-1)*size,
                            canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3])-1)*size,
                            offset + (int(i[0])-1)*3*size + int(i[2])*size,
                            canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3]))*size,
                            fill="#00FF00")'''
            w.itemconfig(rectangles[int(i)], fill='#00FF00',activefill ='green')

def clear_table():
    for i in num:
        i = str(i)
        '''w.create_rectangle(offset + 0 + (int(i[0])-1)*3*size + (int(i[2])-1)*size,
                           canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3])-1)*size,
                           offset + (int(i[0])-1)*3*size + int(i[2])*size,
                           canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3]))*size,
                           fill="#FFFFFF")'''
        w.itemconfig(rectangles[int(i)], fill='#FFFFFF')

def iterate():
    for i in num:
        aa = set(vicinity(i))
        for j in num.difference(aa):
            aa.update(vicinity(j))
            if len(aa) < 18:
                aa.difference_update(set(vicinity(j)))
                continue
            for k in num.difference(aa):
                aa.update(vicinity(k))
                print(len(aa))
                if len(aa) < 27:
                    aa.difference_update(set(vicinity(k)))
                    continue
                for l in num.difference(aa):
                    aa.update(vicinity(l))
                    if len(aa) < 36:
                        aa.difference_update(set(vicinity(l)))
                        continue
                    for m in num.difference(aa):
                        aa.update(vicinity(m))
                        if len(aa) < 45:
                            aa.difference_update(set(vicinity(m)))
                            continue
                        for n in num.difference(aa):
                            aa.update(vicinity(n))
                            if len(aa) < 54:
                                aa.difference_update(set(vicinity(n)))
                                continue
                            for o in num.difference(aa):
                                aa.update(vicinity(o))
                                if len(aa) < 63:
                                    aa.difference_update(set(vicinity(o)))
                                    continue
                                for p in num.difference(aa):
                                    aa.update(vicinity(p))
                                    if len(aa) < 72:
                                        aa.difference_update(set(vicinity(p)))
                                        continue
                                    for q in num.difference(aa):
                                        aa.update(vicinity(q))
                                        print(i,j,k,l,m,n,o,p,q)
                                        if len(aa) == 81:
                                            print(i,vicinity(i))
                                            print(j,vicinity(j))
                                            print(k,vicinity(k))
                                            print(l,vicinity(l))
                                            print(m,vicinity(m))
                                            print(n,vicinity(n))
                                            print(o,vicinity(o))
                                            print(p,vicinity(p))
                                            print(q,vicinity(q))
                                            zc = 1
                                            for zz in aa:
                                                print(zc,zz)
                                                zc = zc + 1
                                            quit()
                                        aa.difference_update(set(vicinity(q)))

                                    aa.difference_update(set(vicinity(p)))
                                aa.difference_update(set(vicinity(o)))
                            aa.difference_update(set(vicinity(n)))
                        aa.difference_update(set(vicinity(m)))
                    aa.difference_update(set(vicinity(l)))
                aa.difference_update(set(vicinity(k)))
            aa.difference_update(set(vicinity(j)))
        aa.difference_update(set(vicinity(i)))


iterate()

button = Button(buttons,
                   anchor = 'w',
                   text="SHOW",
                   command=partial(create_table,d))
button.pack(fill = BOTH)
clear = Button(buttons,
                   anchor = 'w',
                   text="CLEAR",
                   command=clear_table)
clear.pack(fill = BOTH)
test = Button(buttons,
                   anchor = 'w',
                   text="TEST")
test.pack(fill = BOTH)
exit_button = Button(buttons,
                   anchor = 'w',
                   text="EXIT",
                   command=quit)
exit_button.pack(fill = BOTH)


#mainloop()

'''for i in num:
    aa = [z for z in num if z in vicinity(i)]
    for j in [zz for zz in num if zz not in aa]:
        aa = aa + [y for y in num if y in vicinity(j)]
        for k in [yy for yy in num if yy not in aa]:
            aa = aa + [x for x in num if x in vicinity(k)]
            for l in [xx for xx in num if xx not in aa]:
                aa = aa + [w for w in num if w in vicinity(l)]
                for m in [ww for ww in num if ww not in aa]:
                    aa = aa + [v for v in num if v in vicinity(m)]
                    for n in [vv for vv in num if vv not in aa]:
                        aa = aa + [u for u in num if u in vicinity(n)]
                        for o in [uu for uu in num if uu not in aa]:
                            aa = aa + [t for t in num if t in vicinity(o)]
                            for p in [tt for tt in num if tt not in aa]:
                                aa = aa + [s for s in num if s in vicinity(p)]
                                for q in [ss for ss in num if ss not in aa]:
                                    print(len(aa))
                                    if sorted([i,j,k,l,m,n,o,p,q]) == c:
                                        print(True)
                                        quit()
                                    ans = []
                                    for aaa in num:
                                        #ans = []
                                        g = 0
                                        for bbb in (i,j,k,l,m,n,o,p,q):
                                            g = g + diff(aaa,bbb)
                                        ans.append(g)
                                        #print(aaa, ans)
                                    #print(ans)
                                    if 0 in ans:
                                        True
                                    else:
                                        print(i,j,k,l,m,n,o,p,q)
                                    print(i,j,k,l,m,n,o,p,q)'''
