from math import pi
class Plane():
    def  __init__(self, c, s, e=False):
        self.ncorner = c
        self.nside = s
        self.equalside = e
    
    def ShapeName(self):
            
        if self.ncorner == 1 and self.nside == 0:
            return("Circle")

        elif self.ncorner == 3 and self.nside == 3:
            return("Triangle")
        
        elif self.ncorner == 4 and self.nside == 4 and self.equalside:
            return("Square")
        else:
            return('Rectangle')
        

        
class Circle(Plane):

    def __init__(self, r):
        super().__init__(1,0)
        self.r = r
    
    def Area(self):
        return(pi*(self.r)**2)

    def ShapeName(self):
        return super().ShapeName()
    
    
    def Centroid(self):
        x = self.r
        y = self.r
        return("Centroid is at ({}, {}".format(x,y))


class square(Plane):
    
    def __init__(self, b):
        super().__init__(4,4)
        self.l = b
        self.b =b

    def Area(self):
        return(self.b*self.l)
    
    def ShapeName(self):
        return super().ShapeName()
    
    def Centroid(self):
        x = self.b/2
        y = self.l/2
        return("Centroid is at ({}, {}".format(x,y))
    

class rectangle(Plane):

    def __init__(self,l,b):
        super().__init__(4,4)
        self.equalside = False
        self.l = l
        self.h = b
    def Area(self):
        return(self.l*self.h)
    
    def ShapeName(self):
        return super().ShapeName()
    
    def Centroid(self):
        x = self.b/2
        y = self.l/2
        return("Centroid is at ({}, {})".format(x,y))
    

class triangle(Plane):

    def __init__(self,b,h):
        super().__init__(3,3)
        self.b = b
        self.h =h

    def Area(self):
        return(self.b*self.h*0.5)

    def ShapeName(self):
        return super().ShapeName()
    
    def Centroid(self):
        x = self.b/2
        y = self.h/3
        return("Centroid is at ({}, {}".format(x,y))
    

t = triangle(4,5)
print(t.Area())
print(t.ShapeName())