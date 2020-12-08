class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

  def __add__(self,other):
     if isinstance(other,A):
        return other.a+self.a
     elif isinstance(other,int):
         return other+self.a
     else:
         return -1

if __name__=="__main__":
   a=A(3,4)
   print(a)
   b=A(5,6)
   print(a+b)

     