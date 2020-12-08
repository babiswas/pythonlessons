class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __add__(self,other):
     if isinstance(other,A):
        return other.a+self.a
     elif isinstance(other,int):
        return other+self.a
     else:
        return -1
        
  def __radd__(self,other):
      if not other:
         return self
      else:
         return self.__add__(other)

if __name__=="__main__":
   a=A(3,4)
   b=A(5,6)
   print(a+b)
   print(2+a)

   
