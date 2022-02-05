from point import point
from reflections import reflection
from dilations import dilation
choice = input("Reflection (ref) or Dilation (dil)? ")

if choice == "ref":
  reflection()
elif choice == "dil":
  dilation()

