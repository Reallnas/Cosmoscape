import pygame

def loadImage(name,transparence=False):
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print("Cannot load image:", name)
        raise SystemExit
    image = image.convert()
    if transparence:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL )
    return image
