Below is a module with a set of functions saved in a script called circleModule.py. You will see this script again later in the lab for this topic.

# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius
 
class Circle:
 
    def __init__(self, radius):
        self.radius = radius
 
    def circumference(self):
      pi = 3.14
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue
 
    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))
An application that exists in the same directory as circleModule.py could use this module by importing it, instantiating the class, and then using dot notation to call its functions, as follows:

from circleModule import Circle
      
# First instantiation of the Circle class.
circle1 = Circle(2)
# Call the printCircumference for the instantiated circle1 class.
circle1.printCircumference()
 
# Two more instantiations and method calls for the Circle class.
circle2 = Circle(5)
circle2.printCircumference()
 
circle3 = Circle(7)
circle3.printCircumference()
