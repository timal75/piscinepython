def my_var():
  a=42
  print (a," est de type", type(a))
  a='42'
  print (a," est de type", type(a))
  a='quarante-deux'
  print (a," est de type", type(a))
  a=(42.0 == 42.0)
  print (a," est de type", type(a))
  a=[42]
  print (a," est de type", type(a))
  a={42:42}
  print (a," est de type", type(a))
  a=42,
  print (a," est de type", type(a))
  a={42}
  print (a," est de type", type(a))
  
if __name__ == '__main__':
	my_var()