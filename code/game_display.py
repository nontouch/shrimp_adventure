import pygame
from pygame.locals import *
import sys
import time


class Map_generate() :
    def __init__(self, point_x , point_y , wide , height) :
        self.point_x = point_x
        self.point_y = point_y
        self.wide = wide
        self.height = height
        self.rect = (point_x, point_y, wide, height)
    def draw(self,image,surface) :
        self.surface = surface
        self.image = image
        pygame.draw.rect(self.image ,(0, 0, 0) ,self.rect, 1)
        self.surface.blit(self.image,(self.point_x, self.point_y, self.wide, self.height), self.rect)
    def draw_point(self,image,surface) :
        self.surface = surface
        self.image = image
        pygame.draw.rect(self.image ,(0, 255, 0) ,self.rect, 1)
        self.surface.blit(self.image,(self.point_x, self.point_y, self.wide, self.height))

class built() :
    def __init__(self,background,ground_play,player) :
        pygame.init()
        pygame.display.set_caption('Shrimp Adventure') 
        #clock = pygame.time.Clock()
        wide = 800
        height = 800
        keys = [False, False, False, False]
        screen  = pygame.display.set_mode((wide, height))
        surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

        chapter = []
        mape = background
        chapter.append(mape)


        is_running = True 

        bg = []
        m = []
        charactor = []
        wide_part, height_part = 8, 8
        wp , hp = wide // wide_part , height // height_part
        for map_cut_wide in range(wide_part) :
            for map_cut_height in range(height_part) :
                block = Map_generate(map_cut_wide*wp ,map_cut_height*hp, wp ,hp)
                bg.append(block)
        for i in ground_play :
            chapter.append(i[0])
            block = Map_generate(i[1]*wp ,i[2]*hp, wp ,hp)
            m.append([i[0],block])

        target_high = cheak(m,player[0][2],hp)
        print(target_high)
        for i in player :
            chapter.append(i[0])
            block = Map_generate(i[1]*wp ,target_high*hp, wp ,hp)
            charactor.append([i[0],block])

        while is_running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    is_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key==K_UP:
                        keys[0]=True
                    elif event.key==K_LEFT:
                        keys[1]=True
                    elif event.key==K_DOWN:
                        keys[2]=True
                    elif event.key==K_RIGHT:
                        keys[3]=True
 
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_UP:
                        keys[0]=False
                    elif event.key==pygame.K_LEFT:
                        keys[1]=False
                    elif event.key==pygame.K_DOWN:
                        keys[2]=False
                    elif event.key==pygame.K_RIGHT:
                        keys[3]=False


            for b in bg :
                b.draw(mape,surface)

            for g in m :
                g[1].draw_point(g[0],surface)

            for c in charactor :
                c[1].draw_point(c[0],surface)

            if mape is None:
                continue

            # get the image size
            for data in chapter : 
                img_rect = data.get_rect()
                img_w, img_h = img_rect.w, img_rect.h


            if (charactor[0][1].point_y) - (height-228) < 0 :
                charactor[0][1].point_y += 3
                if keys [1]: 
                    if charactor[0][1].point_x > 0:      # If the player is inside the playing field
                        charactor[0][1].point_x -= 5  # Decrease x position. The player goes left
    # If the right key is pressed
                elif keys [3]: 
                    if charactor[0][1].point_x <wide-128: # If the player is inside the playing field
                        charactor[0][1].point_x += 5    # Increase x position. The player goes right
            else :
                if keys [0]: 
                    if charactor[0][1].point_y> 0:     # If the coordinate is greater than 0 (not outside the playing field)
                        charactor[0][1].point_y -= 150 # Change the y position by 15 pixels. The player moves upwards
    
    # If the down key is pressed
                elif keys [2]: 
                    if charactor[0][1].point_y < height-228: # If the coordinate is less than the height of the playing field
                        charactor[0][1].point_y += 5     # Change the y position by 15 pixels. The player goes down
    # Update x-position
    # If the left key is pressed
                if keys [1]: 
                    if charactor[0][1].point_x > 0:      # If the player is inside the playing field
                        charactor[0][1].point_x -= 5  # Decrease x position. The player goes left
    # If the right key is pressed
                elif keys [3]: 
                    if charactor[0][1].point_x <wide-128: # If the player is inside the playing field
                        charactor[0][1].point_x += 5    # Increase x position. The player goes right
            


            screen.blit( surface, (0,0) )
            pygame.display.update()


def cheak(Rect_list,target,high_part) :
    for i in range(2) :
        for r in Rect_list :
            if int(r[1].point_y) < (target* high_part) + 100 :
                target -= 1.28
            else : 
                pass
    return target

