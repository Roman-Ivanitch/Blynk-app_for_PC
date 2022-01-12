import pyaudio
import math
import struct
import pygame
import numpy
pa = pyaudio.PyAudio()
#open audio stream
stream = pa.open(input_device_index=1,rate=44100,format=pyaudio.paInt16,channels=2,input=True)    


#read bytes from stream and convert to numbers
def get_data():
    data = stream.read(int(44100*0.05))
    s = numpy.fromstring(data, numpy.int16)
    return struct.unpack('h'*4410, data)



pygame.init()
screen = pygame.display.set_mode((4000,1000))



def redraw():
    data = get_data() 
    #draw every number as a bar onto pygame windows
    #last 4410 values are missin      
    for x in range(4000):            
        val = data[x]           
        pygame.draw.rect(screen,(0,0,0),(x,0,1,1000),0)                      
        pygame.draw.rect(screen,(255,255,255),(x,0,1,val),0)



    pygame.display.update()
    pygame.event.clear()



while 1:    
    redraw()