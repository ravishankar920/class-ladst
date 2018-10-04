#printing rock paper siccor 
import random
u=(input(" enter rock or paper or scissor "))
a={1:'r',2:'p',3:'s'}
c=[random.randint(1,3)]
if(u == 'r'or u== 'p'or u=='s'):
	if(u==c):
		print("its a tie")
	elif((u=='r' and c=='s') or (u=='r' and c=='p') or (u=='p' and c=='s')):
		print("user wins")
	else:
	    print("computer wins")

