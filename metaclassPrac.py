# Custom meta classes
# More into: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python




# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned 
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__' and uppercase it
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo(): # global __metaclass__ won't work with "object" though
  # but we can define __metaclass__ here instead to affect only this class
  # and this will work with "object" children
  bar = 'bip'


#=====================================================================
# Test type created metalcass
#=====================================================================
print "Test type created metaclass"
print "Has attribute bar? ", (hasattr(Foo, 'bar'))
# Out: False
print "Has attribute BAR? ", (hasattr(Foo, 'BAR'))
# Out: True

print "new instance f = Foo()"
f = Foo()
print "f.BAR:", f.BAR  # Out: 'bip'


#=====================================================================
# Real example: UpperAttrMetaclass
#=====================================================================
# remember that `type` is actually a class like `str` and `int`
# so you can inherit from it
class UpperAttrMetaclass_1(type): 
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)

# But this is not really OOP. We call type directly and we don't override call the parent __new__. Let's do it:
class UpperAttrMetaclass_2(type):

    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # reuse the type.__new__ method
        # this is basic OOP, nothing magic in there
        return type.__new__(upperattr_metaclass, future_class_name, 
                            future_class_parents, uppercase_attr)
# You may have noticed the extra argument upperattr_metaclass. 
# There is nothing special about it: a method always receives the current instance as first parameter. 
# Just like you have self for ordinary methods.

# Of course, the names I used here are long for the sake of clarity, 
# but like for self, all the arguments have conventional names. 
# So a real production metaclass would look like this:
class UpperAttrMetaclass_3(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)

# We can make it even cleaner by using super, which will ease inheritance 
# (because yes, you can have metaclasses, inheriting from metaclasses, inheriting from type):

class UpperAttrMetaclass_4(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

"""
That's it. There is really nothing more about metaclasses.

The reason behind the complexity of the code using metaclasses is not because of metaclasses, it's because you usually use metaclasses to do twisted stuff relying on introspection, manipulating inheritance, vars such as __dict__, etc.

Indeed, metaclasses are especially useful to do black magic, and therefore complicated stuff. But by themselves, they are simple:

intercept a class creation
modify the class
return the modified class
"""
