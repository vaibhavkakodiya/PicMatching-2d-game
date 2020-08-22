from pygame import image
import os 
ASSET_FILES = [img for img in os.listdir('assets') if img[-3:] == 'png' ]
ASSET_DIR = 'assets'
total_size = 1200
tile_size = total_size // 4
tile_margin = 10