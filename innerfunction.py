def myfunc():
  x = 1
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()