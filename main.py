from PIL import Image
import random
from phue import Bridge
import time
from multiprocessing import Process

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

# brightness
extralow = random.randint(10, 25)
low = random.randint(50, 80)
lowmed = random.randint(90, 125)
med = random.randint(125,175)
medhigh = random.randint(160,200)
high = random.randint(190, 255)

# transition speed
slow_tran = random.randint(300,600)
med_tran = random.randint(100,300)
fast_tran = random.randint(30,70)
instant_tran = 50

# sleep time
sleep_long = random.randint(70, 100)
sleep_med = random.randint(35, 60)
sleep_short = random.randint(10, 25)
sleep_instant = 30



def light1(image):
    while True:
        b.set_light(1, 'on', True)
        xy = imageRandomPixel('C:/Users/nickt/Documents/Python Scripts/Visual Studio Code/Phue/phue-master/Images/%s' %image)
        lights[0].transitiontime = random.randint((userInputTranstion_low * 10), (userInputTranstion_low * 10))
        lights[0].brightness = random.randint(userInputBrightness_low, userInputBrightness_high)
        lights[0].xy = xy
        time.sleep((lights[0].transitiontime)/10 + random.randint(userInputSleep_low, userInputSleep_high))

def light2(image):
    while True:
        b.set_light(2, 'on', True)
        xy = imageRandomPixel('C:/Users/nickt/Documents/Python Scripts/Visual Studio Code/Phue/phue-master/Images/%s' %image)
        lights[1].transitiontime = random.randint((userInputTranstion_low * 10), (userInputTranstion_low * 10))
        lights[1].brightness = random.randint(userInputBrightness_low, userInputBrightness_high)
        lights[1].xy = xy
        time.sleep((lights[1].transitiontime)/10 + random.randint(userInputSleep_low, userInputSleep_high))

def light3(image):
    while True:
        b.set_light(3, 'on', True)
        xy = imageRandomPixel('C:/Users/nickt/Documents/Python Scripts/Visual Studio Code/Phue/phue-master/Images/%s' %image)
        lights[2].transitiontime = random.randint((userInputTranstion_low * 10), (userInputTranstion_low * 10))
        lights[2].brightness = random.randint(userInputBrightness_low, userInputBrightness_high)
        lights[2].xy = xy
        time.sleep((lights[2].transitiontime)/10 + random.randint(userInputSleep_low, userInputSleep_high))

def light4(image):
    while True:
        b.set_light(4, 'on', True)
        xy = imageRandomPixel('C:/Users/nickt/Documents/Python Scripts/Visual Studio Code/Phue/phue-master/Images/%s' %image)
        lights[3].transitiontime = random.randint((userInputTranstion_low * 10), (userInputTranstion_low * 10))
        lights[3].brightness = random.randint(userInputBrightness_low, userInputBrightness_high)
        lights[3].xy = xy
        time.sleep((lights[3].transitiontime)/10 + random.randint(userInputSleep_low, userInputSleep_high))

def lightflicker():
    while True:
        for light in lights:
            light.brightness = random.randint(235,255)
            # time.sleep(random.uniform(0,0.1))
        time.sleep(random.uniform(0.2,0.7))

#User Inputs Here
userInputImage = 'water.jpg'

userInputBrightness_low = 180
userInputBrightness_high = 200

userInputTranstion_low = 2
userInputTranstion_high = 8

userInputSleep_low = 2
userInputSleep_high = 7



if __name__ == '__main__':
    p1 = Process(target=light1, args=(userInputImage,))
    p1.start()
    p2 = Process(target=light2, args=(userInputImage,))
    p2.start()
    p3 = Process(target=light3, args=(userInputImage,))
    p3.start() 
    p4 = Process(target=light4, args=(userInputImage,))
    p4.start()
    # p5 = Process(target=lightflicker)
    # p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    # p5.join()
