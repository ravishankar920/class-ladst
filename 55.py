#printing randon funtion

import random

while True:
	i=input("enter 'r' to role 'q' to quit  ")
	if(i=='q'):
		print("Bye!")
		exit()


	if(i=='r'):
		print("role the dice ",random.randint(1,6))
    	


		