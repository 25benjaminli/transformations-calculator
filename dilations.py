from point import point, tryInt, tryFloat

def dilation():
  num = tryInt(input("How many points do you want to dilate? "))
  xDil = tryFloat(input("X coordinate of center of dilation: "))
  yDil = tryFloat(input("Y coordinate of center of dilation: "))
  scaleFactor = tryFloat(input("Scale factor (decimal): "))

  points = []

  for i in range(num):
    x = tryInt(input("x: "))
    y = tryInt(input("y: "))
    
    pt = point(x, y)
    points.append(pt)

  print("printing new coordinates in order of input: ")
  for p in points:
    xDiff = (xDil - p.x) * scaleFactor
    yDiff = (yDil - p.y) * scaleFactor

    print(f"({xDil - xDiff}, {yDil - yDiff})")


  