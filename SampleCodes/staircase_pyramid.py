def staircase(n):
	for i in range(n, 0, -1):
		my_space = " " * (i-1)
		my_star = "*" * (n-i+1)
		print(my_space + my_star)


def pyramid(n):
	for i in range(n, 0, -2):
		my_space = " " * int(i//2)
		my_star = "*" * (n-i+1)
		print(my_space + my_star + my_space)
	
	
num = 9  # int(input("Enter a number to create staircase and pyramid:"))
staircase(num)
pyramid(num)
