'''
This is the primitive sprite system used in balatro.py, this script was the playground used to hardcore cards faces' sprites in the game.
'''

from kandinsky import *
D="007a2b7a6a4b6a5a6b5a4a8b4a3a9b1b3a2a9b3b2a1a9b5b1a"
S="7a2c7a6a4c6a5a6c5a4a8c4a3a9c1c3a2a9c3c2a1a9c5c1a1a9c5c1a1a9c5c1a2a3c2a2c2a3c2a7a2c7a7a2c7a6a4c6a5a6c5a"
C="6a4d6a5a6d5a4a8d4a4a8d4a4a8d4a2a9d3d2a1a9d5d1a1a9d5d1a1a9d5d1a2a9d3d2a3a2d2a2d2a2d3a7a2d7a6a4d6a5a6d5a"
H="2a3e6a3e2a1a5e4a5e1a1a6e2a6e1a1a5e9e1a1a5e9e1a1a5e9e1a1a5e9e1a1a5e9e1a2a3e9e2a3a1e9e3a4a8e4a5a6e5a6a4e6a7a2e7a"
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

draw_sprite(S,40,100)
draw_sprite(D,100,100)
draw_sprite(C,160,100)
draw_sprite(H,220,100)
