import sys
import PIL.ImageOps
import serial, io
import pygame
from PIL import Image

ser = serial.Serial('COM1', 9600, timeout=3)
data = b""

while True:
    data_in = ser.readline()
    if data_in:
        data += data_in
    else:
        break
ser.close()
ioData = io.BytesIO(data)
x = Image.open(ioData)
gray = (PIL.ImageOps.grayscale(x)).convert('RGB')

mode = gray.mode
print(mode)
size = gray.size
print(size)
datos = gray.tobytes()

pygame.init()

pantalla = screen = pygame.display.set_mode((128, 128))
py_image = pygame.image.fromstring(datos, size, mode)
superficie = pygame.Surface((64,64))
superficie.blit(py_image, (0,0))
pantalla.blit(superficie, (0, 0))
pantalla.blit(superficie, (64, 0))
pantalla.blit(superficie, (0, 64))
pantalla.blit(superficie, (64, 64))
while True:
    if pygame.event.get() == pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()