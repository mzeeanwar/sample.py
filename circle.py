# Print the circumference for circles with a radius of 2, 5, and 7
# In this example, there is a class named Circle.
# Classes will be discussed later. circumference
# and printCircumference are the names of the
# method in the class. These methods returns the
# value of the circumferenceValue to the code
# that called the method.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
      # Formula for a circumference is c = pi * diameter
      # Formula for a diameter is d = 2 * radius
      pi = 3.14 # (Will hardcode pi in this example)
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue
    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))
radius1 = 2
radius2 = 5
radius3 = 7
# Since Circle is a class, it must be instatiated
# with the value of the radius first.
circle1 = Circle(radius1)
# Since printCircumference is a method, it must be
# called using the [class instance].[method]
# syntax. Just calling printCircumference() will
# not work
circle1.printCircumference()
circle2 = Circle(radius2)
circle2.printCircumference()
circle3 = Circle(radius3)
circle3.printCircumference()
