class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def sum(self):
      return self.a+self.b

  def __str__(self):
      return f"{self.a} and {self.b}"

class B(A):
   def __init__(self,*args):
      super().__init__(args[0],args[1])
      self.c=args[2]

   def sum(self):
       m=super().sum()
       return m+self.c

   def __str__(self):
      return f"{self.a} and {self.b} and {self.c}"


if __name__=="__main__":
   a=A(3,4)
   print(a)
   b=B(3,4,5)
   print(b)
   print(b.sum())

   
   

   
   