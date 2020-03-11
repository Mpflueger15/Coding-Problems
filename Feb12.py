def min_operations(x, y):
  if y%x==0:
  	return (y/x)/2
  else:
  	return y%x + (y/x)/2

print(min_operations(6, 20))