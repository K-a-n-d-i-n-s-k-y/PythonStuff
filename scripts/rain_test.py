'''
This is a simple pixel rain test
'''

from random import randint
from kandinsky import set_pixel
n=100
dh=1
dw=1
listpos=[]
for i in range(1,n+1):
  listpos.append([randint(-50,320-dw),
  0-(dh*randint(i,i*10))])
while listpos!=[]:
  for i in range(len(listpos)):
    if listpos[i][1]>=222:
      listpos[i]=[randint(-50,320-dw),
      0-(dh*randint(1,10))]
    set_pixel(listpos[i][0],listpos[i][1],
    (255,255,255))
    set_pixel(listpos[i][0],listpos[i][1]
    +1,(255,255,255))
    listpos[i][1]+=4
    listpos[i][0]+=1
    set_pixel(listpos[i][0],listpos[i][1],
    (0,0,0))
    set_pixel(listpos[i][0],listpos[i][1]
    +1,(0,0,0))
