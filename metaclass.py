class C:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"
   def geta(self):
      return self.a
   def getb(self):
      return self.b

class D(type):
   def __new__(cls,classname,baseclass,attrs):
       print("Meta class Executed")
       attrs['display']=C.__dict__['geta']
       return type.__new__(cls,classname,baseclass,attrs)

   def  __init__(self,*args,**kwargs):
        pass

class E(metaclass=D):
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def findsum(self,a,b):
        return self.a+self.b
    def __str__(self):
        return f"{self.a} and {self.b} and {self.c} and {self.d}"

if __name__=="__main__":
   e=E(3,4,5,6)
   print(e)
   print(e.display())

         