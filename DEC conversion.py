def dec_to_degminsec(degree):
    deg = int(degree)
    min = int((degree - deg)*60)
    sec = (((degree - deg)*60) - min) * 3600

    return deg, min, sec

deg, min, sec = dec_to_degminsec(dec)
print(f'Coordinate: {deg}° {min}min {sec}s')
