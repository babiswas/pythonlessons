def test(**kwargs):
    print(kwargs)

def test1(*args):
    print(args)


if __name__=="__main__":
   test(a=1,b=2)
   test(**{'c':3,'d':4})
   test1(*(1,2,3))
   test1(1,2,3,4)

