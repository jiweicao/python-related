class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print x


class Dog:
    count = 0 # this is a class variable
    dogs = [] # this is a class variable

    def __init__(self, name):
        self.name = name #self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n): # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def rollCall(n): #this is implicitly a class method (see comments below)
        print("There are {} dogs.".format(Dog.count))
        if n >= len(Dog.dogs) or n < 0:
            print("They are:")
            for dog in Dog.dogs:
                print("  {}".format(dog))
        else:
            print("The dog indexed at {} is {}.".format(n, Dog.dogs[n]))


class ClassMehodA(object):
    def foo(self,x):
        """foo"""
        print "executing foo(%s,%s)" % (self, x)

    @classmethod
    def class_foo(cls,x):
        """class foo"""
        print "executing class_foo(%s,%s)" % (cls.static_foo(x), x)

    @classmethod
    def class_foo_wrong(x, y):
        print "First should be default class: %s" % x
        print "Second one should be argument: %s" % y

    @staticmethod
    def static_foo(x):
        """sttic foo"""
        print "executing static_foo(%s)" % x
        


