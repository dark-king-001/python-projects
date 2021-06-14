import sys,pygame as py
import attributes as at
py.init()
screenSize = width,height = 1560 , 880
screen = screen = py.display.set_mode(screenSize)
render = True

speed = 0.5
movex =-speed
movey =-speed
posx = 50
posy = 30
size = sizex, sizey= [200,200]
#main loop
while 1:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
    
    
    print(posx)
    print(posy)
    if posx <= 0:
        movex = speed
    if posy <= 0:
        movey = speed
    if posx >= width-sizex:
        movex = -speed
    if posy >= height-sizey:
        movey = -speed
    posx += movex
    posy += movey
    pos=[posx,posy]
    if render == True:
        screen.fill(at.black)
        py.draw.rect(screen, at.blue , py.Rect(pos , size))
        py.display.flip()
    
    #render = False