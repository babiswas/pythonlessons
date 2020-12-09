def decorator1(*args,**kwargs):
    print("Decorator 1 executed")
    def wrapper(func):
       print(kwargs)
       print("Wrapper executed")
       return func
    return wrapper


@decorator1(test1="hello",test2="bello")
def func():
   print("hello")

if __name__=="__main__":
   func()

        