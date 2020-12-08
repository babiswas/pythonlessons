class A:
  name=""
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"
  @classmethod
  def test(cls):
     return cls(3,4)

if __name__=="__main__":
   a=A(2,3)
   b=A.test()
   print(b.__dict__)
   print(a.__dict__)
