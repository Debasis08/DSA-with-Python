x = "awesome" #Global Variable

def myfunc():
  x = "fantastic" #global variable is declared but given a local value
  print("Python is " + x)

myfunc()

print("Python is " + x) # returns the global value only 