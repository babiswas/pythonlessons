class A:
  def __init__(self,a):
     self.a=a
  def __iter__(self):
     self.b=10
     return self
  def __next__(self):
      if not hasattr(self,'b'):
         self.__iter__()
      if self.a<self.b:
         item=self.a
         self.a=self.a+1
         return item
      else:
         raise StopIteration

if __name__=="__main__":
   a=A(0)
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))


      