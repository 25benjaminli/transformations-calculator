from point import point, tryInt, tryFloat

def reflection():
  x = tryInt(input("How many points are in the figure you want to reflect? "))

  slope = input("What is the slope? If it is undefined, type \"undef\": ")

  intercept = tryFloat(input("What is the y-intercept? If and only if the line doesn't have one, type the x intercept. "))

  rounder = tryInt(input("How many decimal points do you want to round to? "))

  points = []

  isUndef = False
  isUndefY = False
  try:
    slope = float(slope)
  except:
    if (slope == "undef"):
      isUndef = True


  for i in range(x):
    xcoord = tryFloat(input("x coordinate: "))
    ycoord = tryFloat(input("y coordinate: "))
    p = point(xcoord, ycoord)
    points.append(p)

  if (isUndef):
    for p in points:
      # diff x values, same y vals
      # e.g. x = -3
      difference = intercept - p.x
      linePoint = point(intercept + difference, p.y)
      print("(" + str(round((linePoint.x), rounder + 1)) + ", " + str(round((linePoint.y), rounder + 1)) + ")")

  elif slope == 0:
    for p in points:
      difference = intercept - p.y
      linePoint = point(p.x, intercept + difference)
      print("(" + str(round((linePoint.x), rounder + 1)) + ", " + str(round((linePoint.y), rounder + 1)) + ")")

  else:

    perpSlope = -1 * float(1/slope)

    for p in points:
      # point slope it!
      newslope = perpSlope
      newintercept = float(newslope * p.x * -1) + p.y
      # make the ys equal to each other to find the midpoint

      xMid = float(1/((-1 * newslope) + slope - intercept)) * newintercept

      yMid = float(newslope * xMid) + newintercept

      mid = point(xMid, yMid)

      wanted = point.findOtherWithMid(mid, p)

      print("(" + str(round((wanted.x), rounder + 1)) + ", " + str(round((wanted.y), rounder + 1)) + ")")
      # implement midpoint formula!

