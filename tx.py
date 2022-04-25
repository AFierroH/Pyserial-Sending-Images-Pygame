import serial
ser = serial.Serial('COM1', 9600)
with open('img01.jpg', "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(b)
    ser.write(b)
ser.close()