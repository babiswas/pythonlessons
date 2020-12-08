def decorator1(func):
   print("Decorator1 body Executed")
   def wrapper(*args):
      print("Wrapper 1 Executed")
      return func(*args)
   return wrapper

def decorator2(func):
    print("Decorator 2 executed")
    def wrapper(*args):
        print("Wrapper2 executed")
        func(*args)
        print("Wrapper 2 completed")
    return wrapper

@decorator2
@decorator1
def func(*args):
   for i in args:
      print(i)

if __name__=="__main__":
   print("Calling wrapped function")
   func("hello","mello","bello")
