f= open("FILE.txt",mode="w")
f.write("hello")
f.close()
with open("FILE.txt",mode="r") as w:
   print( w.read()