class point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def calc_distance(point1, point2):
    return pow((point1.x - point2.x), 2) + pow((point1.y - point2.x), 2)

  def findOtherWithMid(midpoint, point1):
    xOther = (2 * midpoint.x) - point1.x
    yOther = (2 * midpoint.y) - point1.y
    return point(xOther, yOther)
    




x = int(input("How many points are in the figure you want to reflect? "))
slope = input("What is the slope? If it is undefined, type \"undef\": ")
intercept = float(input("What is the y-intercept? If and only if the line doesn't have one, type the x intercept. "))

points = []

isUndef = False
isUndefY = False
try:
  slope = float(slope)
except:
  if (slope == "undef"):
    isUndef = True


for i in range(x):
  xcoord = float(input("x coordinate: "))
  ycoord = float(input("y coordinate: "))
  p = point(xcoord, ycoord)
  points.append(p)

if (isUndef):
  for p in points:
    # diff x values, same y vals
    # e.g. x = -3
    difference = intercept - p.x
    linePoint = point(intercept + difference, p.y)
    print("(" + str(round((linePoint.x), 2)) + ", " + str(round((linePoint.y), 2)) + ")")


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

    print("(" + str(round((wanted.x), 2)) + ", " + str(round((wanted.y), 2)) + ")")
    # implement midpoint formula!

