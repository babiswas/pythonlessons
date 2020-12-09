from abc import ABC,abstractmethod

class C(ABC):
   @abstractmethod
   def sum(self):
      pass
   @abstractmethod
   def sub(self):
      pass

class A(C):
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def sum(self):
       return self.a+self.b
   def sub(self):
       return self.a-self.b

if __name__=="__main__":
   a=A(3,4)
   print(a.__dict__)
   print(a.sum())
   print(a.sub())


   