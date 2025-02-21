def myfunc1():
  x = "Asad"
  def myfunc2():
    nonlocal x
    x = "ZXCvbnm"
  myfunc2()
  return x

print(myfunc1())