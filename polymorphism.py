class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def sum(self):
     return self.a+self.b

class B(A):
   def __init__(self,a,b,c):
       super().__init__(a,b)
       self.c=c
   def sum(self):
      return super().sum()+self.c

if __name__=="__main__":
   print("Polymorphism example")
   a=A(2,3)
   print(a.sum())
   b=B(2,3,4)
   print(b.sum())
