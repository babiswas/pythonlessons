def fun1(self):
   print("hello")

if __name__=="__main__":
   A=type('A',(object,),{'a':12,'b':13,'func2':fun1})
   obj=A()
   print(obj.a)
   print(obj.b)
   A.func2(obj)



   
   