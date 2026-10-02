angle = int(input("Enter the angle in degrees: "))
if angle<0:
    angle=angle+360


if 0< angle and angle<90:
    print("Quadrant I")
elif 90<angle and angle<180:
    print("Quadrant II")
elif 180<angle and angle<270:
    print("Quadrant III")
elif 270<angle and angle<360:
    print("Quadrant IV")

