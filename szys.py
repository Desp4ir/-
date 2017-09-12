
import random


def integer(str):
	ops=['+','-','*','/']
	i=1
	count=0
	while i<21:	
	 	num1 = random.randint(1,100)
	 	num2 = random.randint(1,100)
	 	op = random.randint(0,3)
	 	eq = str(num1) + ops[op] + str(num2)
	 	val = eval(eq)
	 	print "Q%d: %s=" %(i,eq)
	 	ans = raw_input("answer:")
	 	if val == int(ans):
	 		count+=1
	 	i+=1
	print "right:%d,error:%d" %(t,20-t)
	return
def score(str):
	ops=['+','-','*','/']
	i=1
	temp=0	
	while i<21:	
		 	num1 = random.randint(1,100)
		 	num2 = random.randint(1,100)
		 	if(num1>num2):
		 		temp=num1
		 		num1=num2
		 		num2=temp
		 	num3 = random.randint(1,100)
		 	num4 = random.randint(1,100)
		 	if(num3>num4):
		 		temp=num3
		 		num3=num4
		 		num4=temp
		 	op = random.randint(0,3)
		 	eq = (str(num1)+ops[3]+str(num2)) + ops[op] + (str(num3)+ops[3]+str(num4))
		 	val = eval(eq)
		 	print "Q%d: %s=" %(i,eq)
		 	ans = raw_input("answer:")
		 	if val == int(ans):
		 		count+=1
		 	i+=1
	print "right:%d,error:%d" %(t,20-t)
	return

def main():
	print "Please select the type of operation (integer input 1, true score input 0):"
	input = raw_input("A:")
	if(input=='1'):
		integer(str)

	elif(input=='0'):
		score(str)
	
	else:
		print "error input"

if __name__ == '__main__':
	main()