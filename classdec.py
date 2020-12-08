class A:
  def __init__(self,a,b):
      print("Object creation function executed")
      self.a=a
      self.b=b
  def __call__(self,func):
      print("call function executed")
      def wrapper(*args):
          print("Wrapper executed")
          return func(*args)
      return wrapper

@A(2,3)
def func(*args):
    for var in args:
       print(var)

if __name__=="__main__":
   print("Calling Wrapped functions")
   func(3,4,5,6)

      