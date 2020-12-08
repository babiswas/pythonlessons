from contextlib import contextmanager

@contextmanager
def func(filename):
   try:
      file=open(filename,'w')
      yield file
   finally:
      if file:
        file.close()

if __name__=="__main__":
  with func("test1.txt") as file:
      file.write("Bapan Biswas\n")
      file.write("Tapan Biswas \n")

