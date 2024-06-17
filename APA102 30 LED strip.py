from microbit import *
# initialise SPI
spi.init(baudrate=1000000,bits=8,mode=0, sclk=pin13, mosi=pin15, miso=pin14) #setup SPI
# number of pixels in the chain
num_pixels = 30
x = 0xff # brightness control
r = 0xff # red value
g = 0x0f # green value
b = 0xab # blue value
buf=bytearray([x,b,g,r]) # colour mix

#### start with all pixels off ####
spi.write(b'\x00\x00\x00\x00') # start frame
for i in range(num_pixels): # for each pixel
    spi.write(b'\xff\x00\x00\x00') # all colours off
spi.write(b'\xff\xff\xff\xff') # tail

#### now loop up and down ####
while True:
    for j in range(num_pixels): # going up!
    # light up LEDs

        sleep(15)
        spi.write(b'\x00\x00\x00\x00') # start frame
        for i in range(num_pixels): # check each value of i
            if i==j:
                spi.write(buf) # colour
            else:
                spi.write(b'\xff\x00\x00\x00') # off
    spi.write(b'\xff\xff\xff\xff') # end frame
   
    for k in range(num_pixels-1,0,-1): # going down!
        sleep(15)
        spi.write(b'\x00\x00\x00\x00') # start frame
        for i in range(num_pixels): # check each value of i
            if i==k:
                spi.write(buf) # colour
            else:
                spi.write(b'\xff\x00\x00\x00') # off
    spi.write(b'\xff\xff\xff\xff') #end frame
