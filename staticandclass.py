class A:
  multiply=0
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

  @staticmethod
  def const():
     return 6

  @classmethod
  def mul(cls):
     return A.multiply

  def add(self):
      return self.a+self.b+A.const()

  def product(self):
     A.multiply=self.a*self.b

if __name__=="__main__":
   a=A(5,6)
   print(a.__dict__)
   print(a.add())
   a.product()
   print(A.mul())
