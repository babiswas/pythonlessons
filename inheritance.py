class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def sum(self):
      return self.a+self.b

  def __str__(self):
      return f"{self.a} and {self.b}"

class B:
   def __init__(self,c,d):
       self.c=c
       self.d=d

   def sub(self):
       return self.d-self.c

   def __str__(self):
      return f"{self.c} and {self.d}"


class D(A,B):
   def __init__(self,a,b,c,d,e):
       A.__init__(self,a,b)
       B.__init__(self,c,d)
       self.e=e
   def __str__(self):
      return f"{self.a} ,{self.b},{self.c},{self.d},{self.e}"

if __name__=="__main__":
   a=D(1,2,3,4,5)
   print(a.__dict__)
   print(a.sum())
   print(a.sub())
   print(a)

  