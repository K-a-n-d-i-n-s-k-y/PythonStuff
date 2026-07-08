'''
A Flappybird clone
'''

from random import randint
from time import sleep
from ion import keydown,KEY_EXE
from kandinsky import *
score=0
xpr=320
ypr=randint(20,212)
x=155
y=0
z=0
t=0
fill_rect(x,y,10,10,color(0,0,0))
while True:
  if xpr<=-10:
    score+=1
    xpr=320
    ypr=randint(20,212)
  if y<212:
    z+=1
  if keydown(KEY_EXE) and t==0:
    z=-5
    t=1
  if not keydown(KEY_EXE):
    t=0
  if get_pixel(x-1,y)==(0,0,0) or get_pixel(x+11,y)==(0,0,0):
    fill_rect(0,0,320,240,color(255,255,255))
    draw_string("Score :"+str(score),110,100)
    break
  fill_rect(x,y,10,10,color(255,255,255))
  fill_rect(xpr,ypr,10,222-ypr,color(255,255,255))
  y+=z
  xpr-=4
  if y>212:
    y=212
  fill_rect(x,y,10,10,color(0,0,0))
  fill_rect(xpr,ypr,10,222-ypr,color(0,0,0))
  sleep(0.02)
