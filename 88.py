i=int(input("enter a number"))
j=int(input("enter a numaber"))
o=input("which operation you want =,-,*,/ ")

def add(i,j):
	return i+j
def sub(i,j):
	return i-j
def mul(i,j):
	return i*j
def div(i,j):
	return i/j

if(o==+):
	print("addition =",add(i,j))
	elif(o==-):
	print("subtraction =",sub(i,j))
	elif(o==*):
	print("multiplication =",mul(i,j))
	elif(o==/):
	print("division =",div(i,j))
