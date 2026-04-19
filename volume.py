import pint

_si = pint.UnitRegistry()

def volume(length, width, height):
    length = length * _si.meter
    width = width * _si.meter   
    height = height * _si.meter
    return length * width * height

print(volume(2, 3, 4))