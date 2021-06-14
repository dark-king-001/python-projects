import sys,pygame as py
import assets as gameasset
def window(width , height):
    ScreenSize = width,height
    return py.display.set_mode(ScreenSize)

def gameloop(screen):
    posx,posy=300,675
    ballx , bally = 300,425 
    speed =50
    while 1:
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    print("player moved left")
                    posx -= speed
                if event.key == py.K_RIGHT:
                    print("player moved right")
                    posx += speed
        screen.fill(gameasset.black)
        posx=player(screen,posx,posy)
        draw(screen,1)
        ballx,bally=ball(screen,ballx,bally)
        py.display.flip()
#positios of all the textures
def draw(screen,level):
    if level == 1:
        level_1(screen)
#loading textures and printing them
def textureload(screen,object,posx,posy):
    mask = texture(object)
    mask_rect = texturerect(object)
    mask_rect.center = (posx,posy)
    return screen.blit(mask,mask_rect)
def texturerect(object):
    return texture(object).get_rect()
def texture(object):
    return py.image.load(gameasset.texturepath(object)).convert_alpha()
def player(screen,posx,posy):
    textureload(screen,"player",posx,posy)
    return posx
def ball(screen,posx,posy):
    textureload(screen,"ball",posx,posy)
    return posx , posy
#levels
def level_1(screen):
    i=1
    j=1
    for i in range(1,14):
        for j in range(1,14):
            textureload(screen,"brick",(j*50)-25,(i*25)+12.5)