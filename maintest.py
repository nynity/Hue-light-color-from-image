from PIL import Image
import random
from phue import Bridge
import time

def imageRandomPixel(image):
    #import image and convert to RGB friendly true color image
    im = Image.open(image)
    rgb_im = im.convert('RGB')

    #get image width and height
    width,height = im.size

    #select random width and height and grab that pixels rgb values
    random_x = random.randint(0,width-1)
    random_y = random.randint(0,height-1)

    red, green, blue = rgb_im.getpixel((random_x, random_y))
    

    #convert to x,y
    red = red / 255
    green = green / 255
    blue =  blue / 255

    # gamma correction
    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
    blue =  pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

    # convert rgb to xyz
    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    # convert xyz to xy
    new_x = x / (x + y + z)
    y = y / (x + y + z)

    # TODO check color gamut if known
     
    return [new_x, y]

b = Bridge('10.0.0.9')

lights = b.get_light_objects()


image = 'sunset2.jpg'


while True:
    for light in lights:
        extralow = random.randint(10, 25)
        low = random.randint(50, 80)
        lowmed = random.randint(90, 125)
        med = random.randint(125,175)
        medhigh = random.randint(160,200)
        high = random.randint(190, 255)

        # light.transitiontime = random.randint(30,70)
        xy = imageRandomPixel(image)
        light.brightness = medhigh
        light.xy = xy 
    # time.sleep(random.randint(10,30))
    time.sleep(3)
