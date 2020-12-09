def function1(cls):
   print("Decorator block executed")
   def wrapper(*args):
       print("Wrapper Block executed")
       return cls(*args)
   return wrapper

@function1
class A:
  def __init__(self,a,b):
      print("Class init executed")
      self.a=a
      self.b=b
  def __str__(self):
     return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(5,6)
   print(a)

   
