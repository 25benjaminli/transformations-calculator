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


def tryInt(num):
  try:
    return int(num)
  except:
    print("unable to process, try retyping the number.")
    inp = input("type again: ")
    return tryInt(inp)

def tryFloat(num):
  try:
    return float(num)
  except:
    print("unable to process, try retyping the number.")
    inp = input("type again: ")
    return tryFloat(inp)