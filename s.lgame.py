#printing snake and ladder game
import random
count=0



while(count<=100):
	n=input("press r to roll")
	if(n=='r'):
		r=random.randint(1,6)
		count=count+r
		print("u got ",r)
		print("new position is",count)

		if(count==8):
			count=37
			print("i got the ladder ")
	elif(count==11):
			count=2
			print("sorry, you got the snake ")
	elif(count==13):
			count=34
			print(" i got th ladder")
	elif(count==25):
			count=4
			print("sorry you got the snake")
	elif(count==38):
			count=9
			print("sorry you got the snake")


	elif(count==40):
			count=70
			print("i got the ladder ")			
	elif(count==52):
			count=79
			print("i got the ladder ")
	elif(count==65):
			count=45
			print("sorry,u got the snake ")
	elif(count==76):
			count=90
			print("i got the ladder")
	elif(count==89):
			count=70
			print("sorry,u got the snake")
	elif(count==93):
			count=64
			print("sorry,u got the snake")