try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("asad")
  finally:
    f.close()
except:
  print("axx")  
