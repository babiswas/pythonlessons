def decorator(*params,**kwargs):
   def wrapper(func):
      print(kwargs)
      return func
   return wrapper

@decorator(test1="hello",test2="bello",test3="kello")
def func(*args):
   print(args)

if __name__=="__main__":
   func(2,3,4)


      