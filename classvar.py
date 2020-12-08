class A:
  test="bello"
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"
  @classmethod
  def set_test(cls,testvalue):
      A.test=testvalue


if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   print(a)
   print(A.test)
   A.set_test("hello")
   print(A.test)
   print(dir(a))

