# What does this piece of code do?
# Answer:get 10 random number and print the maximum of them.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#give initial value to progress and stored_random_number.
progress=0
stored_random_number=0
while progress<10:
	progress+=1
	#give n a value between 1 to 100
	n = randint(1,100)
	#store the bigger value
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
