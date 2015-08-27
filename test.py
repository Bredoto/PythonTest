from abc import ABCMeta, abstractmethod, abstractproperty

class Color:
        __metaclass__ = ABCMeta
        @abstractmethod
        def color(self, b): pass
        
class Green(object):
    def color(self):
        print 'Green'

Color.register(Green)
g = Green()
g.color() # Green
print isinstance(g, Color) # True
