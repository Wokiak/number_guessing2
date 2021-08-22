import random
number = random.randint(1,10)
player_name = input("Hi, what's your name?")
number_of_guess = 0
print("Okey," , player_name , ',i guessed a number between 1 and 10 ')
while number_of_guess <5 :
	guess = int(input("Enter your number :  "))
	number_of_guess += 1
	if guess == number :
		break
	if guess > number:
		print("lower")
	if guess < number :
		print("higher")
if guess == number :
	print("You guessed the umer in ", str(number_of_guess) ," tries" )		
else :
	print("You didn't guess the number, The numer was" , str(number_of_guess))

