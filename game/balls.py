import pygame as p
from pygame.locals import *
from sys import exit
from random import choice,randrange

w,h=1366,768
colors=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,0,255),(128,128,128),(128,0,0),(128,128,0),(0,128,0),(128,0,128),(0,128,128),(0,0,128)]
p.init()
sur=p.display.set_mode((w,h),FULLSCREEN)
sur.fill((255,255,0))
sur1=sur.copy()
speed=8
r=40
class ball:
    def __init__(self,pos,x,y,color,acc=0):
        self.x=x
        self.y=y
        self.color=color
        self.pos=pos
        self.acc=acc
    def update(self,time):
        bounce=1
        if not r <= self.pos[0] <= w-r:
            self.x = -self.x
            bounce=2
        if not r <= self.pos[1] <= h-r:
            self.y = -self.y
            bounce=2

        self.y+=self.acc*time
        p.draw.circle(sur,(255,255,0),self.pos,r)
        self.pos = self.pos[0]+int(self.x*time*bounce) , self.pos[1]+int(self.y*time*bounce)
        p.draw.circle(sur,self.color,self.pos,r)


balls=[]
clock=p.time.Clock()

while 1:
    for e in p.event.get():
        if e.type==5:
            color=choice(colors)
            pos1=p.mouse.get_pos()
            p.draw.circle(sur1,color,pos1,r)
        elif e.type==6:
            p.draw.circle(sur1,(255,255,0),pos1,r)
            pos2=p.mouse.get_pos()
            x,y=pos1[0]-pos2[0],pos1[1]-pos2[1]
            if (x,y)!=(0,0):
                balls.append(ball(pos1,x*speed,y*speed,color))
        elif e.type==3:
            if e.key>=97 and e.key<=122:
                balls.append(ball(p.mouse.get_pos(),randrange(-600,610,50),0,choice(colors),randrange(500,4000,200)))

     
    sur.blit(sur1,(0,0))
    for b in balls:
        b.update(timepassed)
    
    key=p.key.get_pressed()  
    if key[27]:
        p.quit()
        exit()
    if key[32]:
        balls=[]

    timepassed=clock.tick(60)/1000.      
    p.display.update()
