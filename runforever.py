#printing randon funtion

import random

while True:
	i=input("enter 'n' to quit")
	if(i=='n'):
		print("Bye!")
		exit()

	else:
		print("you got",random.randint(1,6))