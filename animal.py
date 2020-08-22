import random
import os
import settings as set
from pygame import image, transform

d=dict((img,0) for img in set.ASSET_FILES)

def available_animals():
    return [img for img,c in d.items() if c<2]

class Animal:
    def __init__(self,index):
        self.row = index // 4
        self.col = index % 4
        self.name = random.choice(available_animals())
        self.image_path = os.path.join('assets',self.name)
        self.image=image.load(self.image_path)
        self.image = transform.scale(self.image,(set.tile_size-2*set.tile_margin,set.tile_size-2*set.tile_margin))
        d[self.name] += 1 
        self.block = self.image.copy()
        self.block.fill((200,200,200))



