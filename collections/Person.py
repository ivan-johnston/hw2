# ============================================================
# Person.py: Simple model of a Person ...
# ============================================================

class Person:
   __age = 0
   __ssn = 0

   # Constructor method ...

   def __init__(self, fname, lname):
     self.__firstname = fname
     self.__lastname  = lname

   def printname(self):
     print("--- Name: %s, %s" % ( self.__firstname, self.__lastname) )

   # Get first and last names ...

   def getFirstName(self): 
     return self.__firstname 

   def getLastName(self): 
     return self.__lastname 

   # Set/get/print age ...

   def setAge(self, age):
     self.__age = age

   def getAge(self):
     return self.__age

   def printAge(self):
     print("--- Age = %d " % (self.__age) )

   # Set/get/print social security number ...

   def setSSN(self, ssn ):
     self.__ssn = ssn

   def getSSN(self):
     return self.__ssn

   def printSSN(self):
     print("--- Social Security No: %d " % (self.__ssn) )

   # Methods for object sorting logic ...

   def __eq__(self, other):
       return self.__age == other.__age

   def __lt__(self, other):
       return self.__age < other.__age

   # return string represention of object ...

   def __str__(self):
       return "Person: {:s} {:s}: age = {:d} ".format( self.__firstname, self.__lastname, self.__age )


