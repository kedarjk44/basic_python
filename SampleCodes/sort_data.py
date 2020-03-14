
my_dict2 = {}
inp1 = input("Enter the no. of rows and no. of columns")
no_of_rows = int(inp1.split()[0])
assert(no_of_rows >= 1)
no_of_columns = int(inp1.split()[1])
assert(no_of_columns <= 100)

for i in range(no_of_rows):
	inp2 = input("Enter the %d values for column no. %d separated by spaces:" % (int(no_of_columns), (i+1)))
	arr2 = []
	for j in range(int(no_of_columns)):
		assert(int(inp2.split()[j]) <= 1000)
		arr2.append(inp2.split()[j])
	my_dict2[i] = arr2

print(my_dict2)

sort_index = int(input("Enter the index to sort the rows upon:"))
assert (sort_index >= 0 and sort_index <= (no_of_columns-1))
arr3 = []
my_dict3 = {}
for i in range(len(my_dict2)):
	print("inside for loop arr3 and my_dict2[i][sort_index]", (arr3,my_dict2[i][sort_index]))
	if int(my_dict2[i][sort_index]) in arr3:
		arr3.append(int(int(my_dict2[i][sort_index]) + 1))
		my_dict3[(int(int(my_dict2[i][sort_index]) + 1))] = my_dict2[i]
	else:
		arr3.append(int(my_dict2[i][sort_index]))
		my_dict3[int(my_dict2[i][sort_index])] = my_dict2[i]
	

arr3.sort()
for keys in arr3:
	print(my_dict3[(keys)])	
