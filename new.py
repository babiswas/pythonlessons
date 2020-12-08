import json
class A:
  def __new__(cls,*args,**kwargs):
     print("new method executed")
     return object.__new__(cls)
  def __init__(self,a,b):
      self.a=a
      self.b=b

if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   print(json.dumps(a.__dict__))

