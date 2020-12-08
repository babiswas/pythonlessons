class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __str__(self,a,b):
     return f"{self.a} and {self.b}"

  def sum(self):
     return self.a+self.b

if __name__=="__main__":
   a=A(12,13)
   print(a.sum())
   print(A.sum(a))


   