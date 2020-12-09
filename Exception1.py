class A(Exception):
   def __init__(self,str1):
      self.str1=str1
   def __str__(self):
      return f"{self.str1}"

if __name__=="__main__":
   try:
       raise A("hello")
   except Exception as e:
       print("Exception Block")
       print(e)
