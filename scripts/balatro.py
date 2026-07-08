'''
My most polished numworks python project as of July 8th 2026.
Upgrades are declared but as joker aren't implemented levels stay the same.
Controls :

Up :         Select card
Down :       Deselect card
Left :       Move left
Right :      Move right
Ok :         Play selected cards (if not empty)
Backspace :  Discard selected cards

This code is standalone and doesn't import balatro-sprite.py
'''


from kandinsky import *
from random import choice
from ion import *
from time import sleep
# INIT
ranks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
faces = ["S","C","D","H"]
hands = {
    "CH":{"count":0,"chips":5,"mult":1},
    "P":{"count":0,"chips":10,"mult":2},
    "DP":{"count":0,"chips":20,"mult":2},
    "B":{"count":0,"chips":30,"mult":3},
    "S":{"count":0,"chips":30,"mult":4},
    "CL":{"count":0,"chips":35,"mult":4},
    "F":{"count":0,"chips":40,"mult":4},
    "CA":{"count":0,"chips":60,"mult":7},
    "QF":{"count":0,"chips":100,"mult":8}
}
D="007a2b7a6a4b6a5a6b5a4a8b4a3a9b1b3a2a9b3b2a1a9b5b1a"
S="7a2c7a6a4c6a5a6c5a4a8c4a3a9c1c3a2a9c3c2a1a9c5c1a1a9c5c1a1a9c5c1a2a3c2a2c2a3c2a7a2c7a7a2c7a6a4c6a5a6c5a"
C="6a4d6a5a6d5a4a8d4a4a8d4a4a8d4a2a9d3d2a1a9d5d1a1a9d5d1a1a9d5d1a2a9d3d2a3a2d2a2d2a2d3a7a2d7a6a4d6a5a6d5a"
H="2a3e6a3e2a1a5e4a5e1a1a6e2a6e1a1a5e9e1a1a5e9e1a1a5e9e1a1a5e9e1a1a5e9e1a2a3e9e2a3a1e9e3a4a8e4a5a6e5a6a4e6a7a2e7a"
sp={"D":D,"S":S,"C":C,"H":H}
linkr={"A":"As","Q":"Reine","J":"Valet","K":"Roi"}
linkf={"S":"pique","C":"trefle","D":"carreau","H":"coeur"}
## UI
# BG
fill_rect(100,0,220,222,(0,185,100))
fill_rect(0,0,100,222,(100,100,100))
fill_rect(105,5,215,60,(0,135,100))
fill_rect(0,70,100,152,(0,0,0))
fill_rect(5,110,90,18,(0,0,255))
draw_string("X",45,130,(255,255,255),(0,0,0))
fill_rect(5,150,90,18,(255,0,0))

# FUNCTIONS
def draw_sprite(s,x,y):
  xc=0
  col={"a":(255,255,255),"b":(255,100,0),"c":(0,0,0),"d":(0,255,0),"e":(255,0,0)}
  s = [s[i]+s[i+1] for i in range(0,len(s)-1,2)]
  if s[0] == "00":
    s = s[1:]+s[-1:0:-1]
  for (n,c) in s:
    n=int(n)
    if c != "a":
      fill_rect(x+xc,y,n,1,col[c])
    xc+=n
    if xc >=16:
      y+=1
      xc=0
def refresh(x):
  if x==1:fill_rect(100,0,220,222,(0,185,100))
  elif x==2:fill_rect(5,110,90,18,(0,0,255))
  elif x==3:fill_rect(5,150,90,18,(255,0,0))
  else:fill_rect(0,70,100,36,(0,0,0))
def draw_card(val,f,x,y):
  fill_rect(x-18,y-28,36,56,(255,255,255))
  fill_rect(x-20,y-26,40,52,(255,255,255))
  draw_sprite(sp[f],x-8,y-8)
  if val=="10":
    draw_string(str(1),x-18,y-28,(255,0,0))
    draw_string(str(0),x-10,y-28,(255,0,0))
    draw_string(str(1),x,y+8,(255,0,0))
    draw_string(str(0),x+8,y+8,(255,0,0))
  else:
    draw_string(str(val),x-18,y-28,(255,0,0))
    draw_string(str(val),x+8,y+8,(255,0,0))
def draw_deck(d,s,t):
  x=140
  refresh(1)
  for i,card in enumerate(d):
    y=180
    if i in t:y=150
    elif i==s:
      y=170
    if i==s:
      if t!=set():draw_val(card,x,100)
      else:draw_val(card,x,120)
    draw_card(card[0],card[1],x,y)
    x+=20
def new_hand(d,i):
  s=[]
  for _ in range(i):
    s.append(choice(d))
    d.remove(s[-1])
  return (d,s)
def draw_val(c,x,y):
  t=" de "+linkf[c[1]]
  if c[0] in "12345678910":
    t=c[0]+t
  else:
    t=linkr[c[0]]+t
  draw_string(t,max(100,min(x-(len(t)*10)//2,320-len(t)*10)),y,(255,255,255),(0,185,100))
def draw_chips(x):
  refresh(2)
  draw_string(x,50-len(x)*10//2,110,(255,255,255),(0,0,255))
def draw_mult(x):
  refresh(3)
  draw_string(x,50-len(x)*10//2,150,(255,255,255),(255,0,0))
def draw_hand(h):
  refresh(4)
  draw_string(h,0,70,(255,255,255),(0,0,0))
def find_hand(d,t):
    tmp = d
    d = []
    ind=[]
    for i in range(len(t)):
      if i in tmp:
        d.append(t[i])
        ind.append(i)
    del tmp
    x = {}
    h = {"Paire":0,
         "Double Paire":0,
         "Brelan":0,
         "Suite":0,
         "Couleur":0,
         "Full":0,
         "Carré":0,
         "Quinte Flush":0}
    for c in d:
      if c[0] not in x:
        x[c[0]]=1
      else:
        x[c[0]]+=1
    for c in x:
      if x[c] == 4:
        h["Carré"] = 1
      elif x[c] == 3:
        h["Full"] += 1
        h["Brelan"] = 1
      elif x[c] == 2:
        h["Full"] += 0.5
        h["Paire"] = 1
        h["Double Paire"] += 0.5
    ordered = 0
    colored = 0
    for i in range(len(d) - 1):
      if ranks.index(d[i][0]) == ranks.index(d[i + 1][0])-1:
        ordered += 1
      else:
        ordered = 0
      if d[i][1] == d[i + 1][1]:
        colored += 1
      else:
        colored = 0
    tmp=[]
    for i in range(len(d)):
      if x[d[i][0]]>1:
        tmp.append(ind[i])
    if ordered == 4 and colored == 4:
      draw_chips(str(hands["QF"]["chips"]))
      draw_mult(str(hands["QF"]["mult"]))
      return "  Quinte\n   Flush",hands["QF"]["chips"],hands["QF"]["mult"],ind
    elif h["Carré"] == 1:
      draw_chips(str(hands["CA"]["chips"]))
      draw_mult(str(hands["CA"]["mult"]))
      return "  Carré",hands["CA"]["chips"],hands["CA"]["mult"],tmp
    elif h["Full"] == 1.5:
      draw_chips(str(hands["F"]["chips"]))
      draw_mult(str(hands["F"]["mult"]))
      return "  Full",hands["F"]["chips"],hands["F"]["mult"],ind
    elif colored == 4:
      draw_chips(str(hands["CL"]["chips"]))
      draw_mult(str(hands["CL"]["mult"]))
      return "  Couleur",hands["CL"]["chips"],hands["CL"]["mult"],ind
    elif ordered == 4:
      draw_chips(str(hands["S"]["chips"]))
      draw_mult(str(hands["S"]["mult"]))
      return "  Suite",hands["S"]["chips"],hands["S"]["mult"],ind
    elif h["Brelan"] == 1:
      draw_chips(str(hands["B"]["chips"]))
      draw_mult(str(hands["B"]["mult"]))
      return "  Brelan",hands["B"]["chips"],hands["B"]["mult"],tmp
    elif h["Double Paire"] == 1:
      draw_chips(str(hands["DP"]["chips"]))
      draw_mult(str(hands["DP"]["mult"]))
      return "  Double\n   Paire",hands["DP"]["chips"],hands["DP"]["mult"],tmp
    elif h["Paire"] == 1:
      draw_chips(str(hands["P"]["chips"]))
      draw_mult(str(hands["P"]["mult"]))
      return "  Paire",hands["P"]["chips"],hands["P"]["mult"],tmp
    else:
      draw_chips(str(hands["CH"]["chips"]))
      draw_mult(str(hands["CH"]["mult"]))
      return "  Carte\n   Haute",hands["CH"]["chips"],hands["CH"]["mult"],[ind[0]]
# START
draw_chips("0")
draw_mult("0")
drawn=set()
x=140
sel=0
chips="0"
mult="0"
score="0"
deck=[(r,f) for r in ranks for f in faces]
deck,curdeck=new_hand(deck,8)
curdeck=sorted(curdeck,key=lambda c:ranks.index(c[0]))
draw_deck(curdeck,0,set())
# GAME LOOP
while 1:
  if keydown(KEY_LEFT):
    while keydown(KEY_LEFT):pass
    if sel>0:
      sel-=1
      draw_deck(curdeck,sel,drawn)
  if keydown(KEY_RIGHT):
    while keydown(KEY_RIGHT):pass
    if sel<len(curdeck)-1:
      sel+=1
      draw_deck(curdeck,sel,drawn)
  if keydown(KEY_UP):
    while keydown(KEY_UP):pass
    if len(drawn)<5:
      drawn.add(sel)
      tmp=find_hand(drawn,curdeck)
      draw_hand(tmp[0])
      chips,mult=tmp[1],tmp[2]
      draw_deck(curdeck,sel,drawn)
  if keydown(KEY_DOWN):
    while keydown(KEY_DOWN):pass
    drawn.discard(sel)
    if len(drawn)>0:
      tmp=find_hand(drawn,curdeck)
      draw_hand(tmp[0])
      chips,mult=tmp[1],tmp[2]
    else:
      refresh(4)
      draw_chips("0")
      draw_mult("0")
    draw_deck(curdeck,sel,drawn)
  if keydown(KEY_BACKSPACE):
    while keydown(KEY_BACKSPACE):pass
    if len(drawn)==0:break
    tmp=[]
    for i in range(len(curdeck)):
      if i not in drawn:tmp.append(curdeck[i])
      else:deck.append(curdeck[i])
    curdeck=tmp
    tmp=new_hand(deck,len(drawn))
    deck,curdeck=tmp[0],curdeck+tmp[1]
    curdeck=sorted(curdeck,key=lambda c:ranks.index(c[0]))
    drawn.clear()
    draw_deck(curdeck,sel,drawn)
  if keydown(KEY_OK):
    while keydown(KEY_OK):pass
    if len(drawn)==0:break
    refresh(1)
    tmp=[]
    for i in range(len(curdeck)):
      if i not in drawn:
        tmp.append(curdeck[i])
    draw_deck(tmp,-1,[])
    tmp=[]
    for i in drawn:
      tmp.append(i)
    for i in sorted(tmp):
      draw_card(curdeck[i][0],curdeck[i][1],x-20,100)
      x+=45
    sleep(1)
    x=140
    tmp2=find_hand(drawn,curdeck)[3]
    for i in sorted(drawn):
      if i in tmp2:
        if ranks.index(curdeck[i][0])>3:
          tmp=str(14-ranks.index(curdeck[i][0]))
        elif ranks.index(curdeck[i][0])>0:
          tmp="10"
        else:
          tmp="11"
        draw_string(tmp,x-20-len(tmp)*10//2,50,(255,0,0),(0,185,100))
        chips=str(int(chips)+int(tmp))
        draw_chips(chips)
        sleep(0.5)
        fill_rect(100,50,240,20,(0,185,100))
      x+=45
    x=140
    score=str(int(score)+int(chips)*int(mult))
    fill_rect(0,0,100,70,(100,100,100))
    draw_string(score,0,20,(255,255,255),(100,100,100))
    chips="0"
    mult="0"
    refresh(4)
    draw_chips("0")
    draw_mult("0")
    refresh(1)
    tmp=[]
    for i in range(len(curdeck)):
      if i not in drawn:tmp.append(curdeck[i])
      else:deck.append(curdeck[i])
    curdeck=tmp
    tmp=new_hand(deck,len(drawn))
    deck,curdeck=tmp[0],curdeck+tmp[1]
    curdeck=sorted(curdeck,key=lambda c:ranks.index(c[0]))
    drawn.clear()
    draw_deck(curdeck,sel,drawn)
