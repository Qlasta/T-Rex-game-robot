import pyautogui as pag
from PIL import Image
# pip install --upgrade Pillow
# pip install opencv-python
import time
game_is_on = True
screenWidth, screenHeight = pag.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)
time.sleep(3)
# get image of dinosaur

# locate dinosaur on screen, get his position
im_rgba = Image.open("dino.png")
im = im_rgba.convert('RGB')
print(im.format, im.size, im.mode)

dino_loc = pag.locateOnScreen(im, grayscale=True, confidence=0.8)
pag.press("up")
print(dino_loc)
print(dino_loc.left, dino_loc.top, dino_loc.width, dino_loc.height)

dino_jump_position = (int(dino_loc.left + dino_loc.width), int(dino_loc.top + 40))
dino_down_position = (int(dino_loc.left + dino_loc.width), int(dino_loc.top))
print(dino_jump_position)

# get color of cactus -
cactus_color = (83, 83, 83)

# cactus_color = pag.pixel(mouse_on_cactus.x, mouse_on_cactus.y)
# print(cactus_color)

time.sleep(3)

mouse_on_cactus = pag.position()
print(f" Mouse position: {mouse_on_cactus.x, mouse_on_cactus.y}")
print(f"Dino jump position: {dino_jump_position[0], dino_jump_position[1], cactus_color}")

# check if distance from dinosaur and color is equal to something, click key UP or DOWN if its on dinos top.
while game_is_on:
    start = time.time()
    im = pag.screenshot()
    bird1 = im.getpixel((dino_down_position[0], dino_down_position[1]))
    bird2 = im.getpixel((dino_down_position[0] + 10, dino_down_position[1]))
    bird3 = im.getpixel((dino_down_position[0] + 20, dino_down_position[1]))
    bird4 = im.getpixel((dino_down_position[0] + 30, dino_down_position[1]))
    bird5 = im.getpixel((dino_down_position[0] + 25, dino_down_position[1]))
    bird6 = im.getpixel((dino_down_position[0] + 15, dino_down_position[1]))
    bird7 = im.getpixel((dino_down_position[0] + 35, dino_down_position[1]))
    bird8 = im.getpixel((dino_down_position[0] + 40, dino_down_position[1]))
    bird9 = im.getpixel((dino_down_position[0] + 45, dino_down_position[1]))
    bird10 = im.getpixel((dino_down_position[0] + 50, dino_down_position[1]))
    bird11 = im.getpixel((dino_down_position[0] + 55, dino_down_position[1]))
    bird12 = im.getpixel((dino_down_position[0] + 60, dino_down_position[1]))
    bird13 = im.getpixel((dino_down_position[0] + 70, dino_down_position[1]))
    bird14 = im.getpixel((dino_down_position[0] + 100, dino_down_position[1]))
    bird15 = im.getpixel((dino_down_position[0] + 110, dino_down_position[1]))

    cactus1 = im.getpixel((dino_jump_position[0], dino_jump_position[1]))
    cactus2 = im.getpixel((dino_jump_position[0] + 10, dino_jump_position[1]))
    cactus3 = im.getpixel((dino_jump_position[0] + 20, dino_jump_position[1]))
    cactus4 = im.getpixel((dino_jump_position[0] + 30, dino_jump_position[1]))
    cactus5 = im.getpixel((dino_jump_position[0] + 25, dino_jump_position[1]))
    cactus6 = im.getpixel((dino_jump_position[0] + 15, dino_jump_position[1]))
    cactus7 = im.getpixel((dino_jump_position[0] + 35, dino_jump_position[1]))
    cactus8 = im.getpixel((dino_jump_position[0] + 40, dino_jump_position[1]))
    cactus9 = im.getpixel((dino_jump_position[0] + 45, dino_jump_position[1]))
    cactus10 = im.getpixel((dino_jump_position[0] + 50, dino_jump_position[1]))
    cactus11 = im.getpixel((dino_jump_position[0] + 55, dino_jump_position[1]))
    cactus12 = im.getpixel((dino_jump_position[0] + 60, dino_jump_position[1]))
    cactus13 = im.getpixel((dino_jump_position[0] + 70, dino_jump_position[1]))
    cactus14 = im.getpixel((dino_jump_position[0] + 100, dino_jump_position[1]))
    cactus15 = im.getpixel((dino_jump_position[0] + 105, dino_jump_position[1]))
    if cactus1[0] == 83 or cactus2[0] == 83 or cactus3[0] == 83 or cactus4[0] == 83 or cactus5[0] == 83 or cactus6[0] == 83 or \
        cactus7[0] == 83 or cactus8[0] == 83 or cactus9[0] == 83 or cactus10[0] == 83 or cactus11[0] == 83 or cactus12[0] == 83 or \
        cactus13[0] == 83 or cactus14[0] == 83 or cactus15[0] == 83:
        pag.press("up")

    if bird1[0] == 83 or bird2[0] == 83 or bird3[0] == 83 or bird4[0] == 83 or bird5[0] == 83 or bird6[0] == 83 or \
        bird7[0] == 83 or bird8[0] == 83 or bird9[0] == 83 or bird10[0] == 83 or bird11[0] == 83 or bird12[0] == 83 or \
        bird13[0] == 83 or bird14[0] == 83 or bird15[0] == 83:
        pag.press("down")
        time.sleep(0.000001)

    # too slow function:
    # if pag.pixelMatchesColor(dino_jump_position[0], dino_jump_position[1], cactus_color) or\
    #         pag.pixelMatchesColor(dino_jump_position[0] + 100, dino_jump_position[1], cactus_color) or\
    #         pag.pixelMatchesColor(dino_jump_position[0] + 50, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 45, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 40, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 35, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 30, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 25, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 20, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 15, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 10, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 5, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + -5, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + -10, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + -15, dino_jump_position[1], cactus_color) or \
    #         pag.pixelMatchesColor(dino_jump_position[0] + 5, dino_jump_position[1], cactus_color):
        # pag.press("up")
        # time.sleep(0.00001)
    finish = time.time()
    dur = finish-start
    print(F"Duration: {dur}")



