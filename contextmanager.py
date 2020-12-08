class A:
  def __init__(self,filename):
      self.name=filename
  def __enter__(self):
     self.file=open(self.name,'w')
     return self.file
  def __exit__(self,a,b,c):
     if self.file:
        self.file.close()

if __name__=="__main__":
   with A("test1.txt") as file:
      file.write("hello world\n")
      file.write("hello1.world\n")
