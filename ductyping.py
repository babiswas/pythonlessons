class USA:
   def capital(self):
      print("The capital of usa is washington")
   def icon(self):
      print("Statue of liberty")
   def language(self):
      print("The language of USA is english")

class India:
   def capital(self):
      print("The capital of india is delhi")
   def icon(self):
      print("Taj mahal")
   def language(self):
      print("Hindi is the language of india")

def describe(d):
   d.capital()
   d.icon()
   d.language()


if __name__=="__main__":
  i=India()
  u=USA()
  countries=[i,u]
  for c in countries:
      describe(c)

   