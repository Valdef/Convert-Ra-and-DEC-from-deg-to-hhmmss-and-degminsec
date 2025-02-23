def ra_to_hhmmss(deg):
    hours = int(deg/15)
    min = int(((deg/15) - hours) * 60)
    sec = ((((deg/15) - hours) * 60) - min) * 60

    return hours, min, sec

h, min, sec = ra_to_hhmmss(ra)
print(f'Coordinate: {h}H {min}min {sec}s')
