import pygame
from pygame.locals import *
import sys
import time
import socket
import pygame
#from network import Network


class Player() :
    def __init__(self,x,y,w,h) :
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.ground_map = []
        self.current_map = []
        self.vel = 6
        self.jump = False
        self.jump_height = 8
        self.right = True
        self.left = False
        self.atk = False
        self.fell = False
        self.fristfell = True
        self.fell_pos = (0,0)
        self.map = 1
        self.rightwalk = [pygame.image.load("Shrimp-front-atk.png"),pygame.image.load("Shrimp-front.png")]
        self.leftwalk = [pygame.image.load("Shrimp-back-atk.png"),pygame.image.load("Shrimp-back.png")]
        self.ground = [pygame.image.load('dirt-1.png'),pygame.image.load('dirt-2.png'),pygame.image.load('dirt-3.png')]

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.atk = True 
        else:
            self.atk = False

        if keys[pygame.K_LEFT]:
            if check_left(self.pos_x,self.pos_y,self.current_map) :
                self.pos_x -= self.vel
                self.right = False
                self.left = True
        elif keys[pygame.K_RIGHT]:
            if check_right(self.pos_x,self.pos_y,self.current_map) :
                self.pos_x += self.vel
                self.right = True
                self.left = False

        index = check_ground(self.pos_x,self.pos_y,self.current_map)
        #print(index)
        if not self.jump and self.pos_y +64 >= self.current_map[index][1] and index != -1 :
            if keys[pygame.K_UP]:
                self.jump = True
        elif self.jump :
            if self.jump_height >= -8:
                neg = 1
                if self.jump_height < 0 :
                    print(self.pos_y +64 ,self.current_map[index][1],index )
                    if self.pos_y +64 < self.current_map[index][1] :
                        neg = -1
                        if self.current_map[index][1] - (self.pos_y + 64) < (self.jump_height**2) * 0.6 :
                            self.pos_y -= (self.current_map[index][1] - (self.pos_y + 64)) * neg
                        else :
                            self.pos_y -= (self.jump_height**2) * 0.6 * neg
                        self.jump_height -= 1
                    elif self.pos_y +64 >= self.current_map[index][1] :
                        neg = 0
                        self.pos_y -= (self.jump_height**2) * 0.6 * neg
                        self.jump_height -= 1
                else :
                    self.pos_y -= (self.jump_height**2) * 0.6 * neg
                    self.jump_height -= 1
            else:
                self.jump = False
                self.jump_height = 8
    
    def checkstatus(self):
        if self.right:
            if self.atk:
                screen.blit((self.rightwalk[0]),(self.pos_x,self.pos_y))    
            else:
                screen.blit((self.rightwalk[1]),(self.pos_x,self.pos_y))
        elif self.left:
            if self.atk:
                screen.blit((self.leftwalk[0]),(self.pos_x,self.pos_y))
            else:
                screen.blit((self.leftwalk[1]),(self.pos_x,self.pos_y))

    def fellHole(self,ground):
        for i in ground :
            if (self.pos_x in range(i[0],i[0] + i[2]) or (self.pos_x + self.width) in range(i[0],i[0] + i[2])):
                if i[1] - (self.pos_y + 64) == 0 and i[1] - (self.pos_y) == 64:
                    self.fell =  False
                    break
            #self.checkstatus()
            #self.pos_y += self.vel
            else :
                self.fell = True
    
    def checkMap(self):
        if self.map == 1:
            
            if self.pos_x < 0:
                self.pos_x = 0
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 2 

            index = 0
            for i in range(0,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            self.current_map = self.ground_map
            self.ground_map = []

        elif self.map == 2:

            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 1
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 3
            
            index = 0
            for i in range(0,300,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            for i in range(400,600,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            for i in range(700,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1

            self.current_map = self.ground_map
            #print(self.current_map)
            print(self.fell)
            if self.jump_height == 8 :
                if self.fell :
                    self.checkstatus()
                    vel = error_block(self.pos_x,self.pos_y,self.ground_map,'bottom',self.vel)
                    if self.vel > vel :
                        self.pos_y += vel
                    else :
                        self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)

            self.ground_map = []

        elif self.map == 3:
            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 2
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 4
            index = 0
            for i in range(0,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            self.current_map = self.ground_map
            self.ground_map = []
        
        elif self.map == 4:
            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 3
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 5

            index = 0
            self.ground_map.append([0 , 600 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
            index += 1
            for i in range(100,300,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[2],(self.ground_map[index][0],600))
                index += 1
            for i in range(300,800,100):
                self.ground_map.append([i , 600 , 100 , 100])
                screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],600))
                index += 1
            self.ground_map.append([100 , 500 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            self.ground_map.append([200 , 500 , 100 , 100])
            screen.blit(self.ground[2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            self.ground_map.append([200 , 400 , 100 , 100])
            screen.blit(self.ground[(self.ground_map[index][0]//100)%2],(self.ground_map[index][0],self.ground_map[index][1]))
            index += 1
            #print(index)
            self.current_map = self.ground_map

            if self.jump_height == 8 :
                if self.fell :
                    index_g = check_ground(self.pos_x,self.pos_y,self.current_map)
                    if self.current_map[index_g][1] == (self.pos_y + 64) :
                        self.fell = False
                    else :
                        self.checkstatus()
                        vel = error_block(self.pos_x,self.pos_y,self.ground_map,'bottom',self.vel)
                        if self.vel > vel :
                            self.pos_y += vel
                        else :
                            self.pos_y += self.vel
                
                else: 
                    self.fellHole(self.current_map)

            self.ground_map = []
        
        elif self.map == 5:
            if self.pos_x < 0:
                self.pos_x = 800
                self.map = 4
            if self.pos_x > 800:
                self.pos_x = 0
                self.map = 6

def drawWindow(bg,player1):
        screen.blit(bg,(0,-100))
        player1.checkMap()
        #player2.checkMap()
        player1.checkstatus()
        #player2.checkstatus()
        pygame.display.update()

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def check_ground(x,y,data) :
    index = -1
    for i in range(len(data)) :
        if (data[i][0] < x < data[i][0] + data[i][2] or data[i][0] < x + 64 < data[i][0] + data[i][2])   :#or data[i][1].point_x < pos.point_x + 64 < data[i][1].point_x + data[i][1].wide):
            if (y +64 <= data[i][1] and y <= data[i][1] ) :
                index = i
    return index

def check_left(x,y,data) :
    process = True
    for i in range(len(data)) :
        if x == data[i][0]+ data[i][2] :
            if (data[i][1] < y + 64 < data[i][1] + data[i][3] or data[i][1] < y < data[i][1] + data[i][3]):
                process = False
                break
            else:
                process = True
        else :
            pass
    return process

def check_right(x,y,data) :
    process = True
    for i in range(len(data)) :
        if x + 64 >= data[i][0] and x < data[i][0]:
            if (data[i][1] < y + 64 < data[i][1] + data[i][3] or data[i][1] < y < data[i][1] + data[i][3]):
                process = False
                break
            else:
                process = True
        else :
            pass
    return process

def error_block(x,y,data,direction,diff) :
    process = diff
    for i in range(len(data)) :
        if direction == 'left':
            if data[i][0] < x  < data[i][0] + data[i][2] :
                if (x - data[i][0]) < diff :
                    process = (x - data[i][0])
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'right':
            if data[i][0] < x +64  < data[i][0] + data[i][2] :
                if ((data[i][0] + data[i][2]) - (x + 64)) < diff :
                    process = ((data[i][0] + data[i][2]) - (x + 64))
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'top':
            if data[i][1] < y  < data[i][1] + data[i][3] :
                if (y - data[i][1]) < diff :
                    process = (y - data[i][1])
                    break
                else :
                    process = diff
                    break

            else :
                pass

        elif direction == 'bottom':
            if data[i][1] < y + 64 < data[i][1] + data[i][3] :
                if ((data[i][1] + data[i][3]) - (y +64)) < diff :
                    process = ((data[i][1] + data[i][3]) - (y +64))
                    break
                else :
                    process = diff
                    break

            else :
                pass


    return process


pygame.init()
pygame.display.set_caption('Shrimp Adventure') 
width = 800
height = 700
screen  = pygame.display.set_mode((width, height))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
clock = pygame.time.Clock()
bg = pygame.image.load('map1.png')


def main():
    #net = Network()
    #startPos = read_pos(net.getPos())
    player1 = Player(0,600-64,64,64)
    #player2 = Player(300,600-64,64,64)
    run = True
    while run:
        clock.tick(60)
        #p2Pos = read_pos(net.send(make_pos((player1.pos_x, player1.pos_y))))
        #player2.pos_x = p2Pos[0]
        #player2.pos_y = p2Pos[1]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #player1.move()
        #player2.move()
        drawWindow(bg,player1) 
        player1.move()
        #player2.move()

                  
main()
#network.py




class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.189"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
