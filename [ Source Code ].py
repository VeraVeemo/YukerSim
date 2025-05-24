import pygame as game
from pypresence import Presence
import time

game.init()
bime = time.time()

screen = game.display.set_mode((1280, 720))
game.display.set_caption("Yuker Simulator V1.1")
game.display.set_icon(game.image.load("icon.ico"))
fps = game.time.Clock()

pet = game.image.load("../../Assets/pet.gif")
sound = game.mixer.Sound("../../Assets/squish.wav")
yuker = game.image.load("../../Assets/yuker.png")

yimg = yuker.copy()
yrect = yimg.get_rect(center=(640, 360))
vis = False
timer = 0
count = 0
font = game.font.SysFont(None, 36)

def squish(image, squish_factor=0.7):
    w, h = image.get_size()
    return game.transform.scale(image, (w ,int(h * squish_factor)))

rpc = Presence("1375973151472619570")
rpc.connect()
rpc.clear()
run = True
while run:
    rpc.update(
        state=f"{count} times squished!",
        details='Squishing "Yuker"',
        large_text="Yuker",
        start=bime,
        buttons=[
            {"label": "[ Download ]", "url": "https://github.com/VeraVeemo/YukerSim/"},
        ]
    )
    dt = fps.tick(60)
    screen.fill((30, 30, 30))
    for event in game.event.get():
        if event.type == game.QUIT:
            run = False
        elif event.type == game.MOUSEBUTTONDOWN:
            if yrect.collidepoint(event.pos):
                sound.play()
                count += 1
                yimg = squish(yuker)
                vis = True
                timer = game.time.get_ticks()

    if vis and game.time.get_ticks() - timer > 300:
        yimg = yuker.copy()
        vis = False

    yrect = yimg.get_rect(center=(640, 360))
    screen.blit(yimg, yrect)

    if vis:
        rect = pet.get_rect(center=yrect.center)
        screen.blit(pet, rect)

    count_text = font.render(f"Pets: {count}", True, (255, 255, 255))
    screen.blit(count_text, (10, 10))

    game.display.flip()

game.quit()