def my_var():
  filename = 'numbers.txt'
  with open(filename, 'r') as f:
     data = f.readline().split(',')	 
     print(*data, sep='\n') 	   

if __name__ == '__main__':
	my_var()