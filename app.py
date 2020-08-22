from pygame import display, image, event ,transform
import os
import pygame
import settings as set
from animal import Animal
from time import sleep

win_screen = image.load(os.path.join(set.ASSET_DIR,'win/youwon.jpg'))
win_screen = transform.scale(win_screen,(set.total_size,set.total_size))

matched = image.load('assets/win/match.jpg')
matched = transform.scale(matched,(set.total_size,set.total_size))

def find_index(x,y):
    #print('x :',x,' y:',y)
    row = y // set.tile_size
    col = x // set.tile_size

    return row*4 + col 

pygame.init()
display.set_caption('my game')
s = set.total_size
screen=display.set_mode((s,s))


animals=[]
for index in range(0,16):
    a=Animal(index)
   # print(a.name)
    screen.blit(a.block,(a.col*set.tile_size+set.tile_margin,a.row*set.tile_size+set.tile_margin))
    animals.append(a)
q=[]
block=a.block
display.flip()
running=True
show=[True]*16
match=0
while running:
    current_event = event.get()
    for e in current_event:
        if e.type == pygame.QUIT:
            running = False
        elif e.type  == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running= False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            index=find_index(x,y)
           # print(index)
            q.append((index,animals[index]))
            if len(q)>2:
                q=q[1:]
        for i in range(16):
            if show[i]:
                r = i // 4
                c = i % 4
                screen.blit(block,(c*set.tile_size+set.tile_margin,r*set.tile_size+set.tile_margin))
        for index,animal in q:
            if show[i]:
                r = index // 4
                c = index % 4
                screen.blit(animal.image,(c*set.tile_size+set.tile_margin,r*set.tile_size+set.tile_margin))
        display.flip()
        if len(q) == 2:
            #print(q)
            if q[0][0]  != q[1][0]  and q[0][1].name == q[1][1].name:
                for index,imag in q:
                    show[index] = False
                #print('matched')
                q = []
                display.flip()
                sleep(0.2)
                screen.blit(matched,(0,0))
                display.flip()
                sleep(0.5)
                screen.fill((255,255,255))
                match += 2
        if match == 16:
            screen.fill((255,255,255))
            screen.blit(win_screen,(0,0))
            display.flip()
            sleep(5)
            running = False

print('good game !!!')
                




            


