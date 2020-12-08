class A:
  def __init__(self,a,b):
      self.__a=a
      self.__b=b
  def __str__(self):
     return f"{self._A__a} and {self._A__b}"

  def __sum(self):
     return self._A__a+self._A__b

if __name__=="__main__":
   a=A(2,3)
   print(a)
   print(a.__dict__)
   print(a._A__a)
   print(a._A__b)
   print(a._A__sum())


  