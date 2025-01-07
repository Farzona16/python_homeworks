import math

class Vector:
    def __init__(self,*args):
        if not args:
            raise ValueError("Vector must contain at least one component") 
        self.args=tuple(args)

    def __repr__(self):
        return f"Vector{self.args}"
    
    def check_value(self,other):
        if not isinstance(other,Vector):
            raise TypeError("it is not vector")
        if len(self.args)!=len(other.args):
            return ValueError("Vectors must have same dimensions for addition")
    def check_operand(self,other):
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Operand must be a vector or scalar int/float")
    
    def __add__(self,other):
        self.check_value(other)
        return Vector(*(a+b for a,b in zip(self.args,other.args)))
    
    def __sub__(self,other):
        self.check_value(other)
        return Vector(*(a-b for a,b in zip(self.args,other.args)))
    
    def  __mul__(self,other):
        self.check_operand(other)
        if isinstance(other,(int,float)):
            return Vector(*(a*other for a in zip(self.args)))
        elif isinstance(other,Vector):
            self.check_value(other)
            return sum(a*b for a,b in zip(self.args,other.args))
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.args))

    def normalize(self):
        mag=self.magnitude()
        if mag==0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a/mag for a in self.args ))
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3=v1+v2
v4=v1-v2
print(v3)
print(v4)
# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1*3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
