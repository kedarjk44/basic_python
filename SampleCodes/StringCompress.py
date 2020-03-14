#stringcompress.py


def stringCompress(ip_str):
	count = 1
	op_str = ""
	for i in range(len(ip_str)):
		if (i == 0):
			pass		
		elif (ip_str[i] == ip_str[i-1]):
			#print ("count of " + ip_str[i] + " is " + str(count), i , i-1 )
			count += 1
			if (i == len(ip_str)-1):
				op_str = op_str + ip_str[i-1] + str(count)		
		elif (ip_str[i] != ip_str[i-1]):
			if (count != 1):
				op_str = op_str + ip_str[i-1] + str(count)
			else:
				op_str = op_str + ip_str[i-1]
			#print (op_str, "\n")
			count = 1
			if (i == len(ip_str)-1):
				count = 1
				op_str = op_str + ip_str[i]				
				break
	return op_str	


def compress_string(inp_str):
	char_dict = {}
	for i in range(len(inp_str)):
		if inp_str[i] in list(char_dict.keys()):
			char_dict[inp_str[i]] += 1
		else:
			char_dict[inp_str[i]] = 1
	print(char_dict)
	out_str = ""
	for k, v in char_dict.items():
		out_str += k
		out_str += str(v)
	print(out_str)


def main():
	ip_str = "abbbbbbssssssssssssssssqrrrrrrrrrrvvvvvvvvzzzxx"	
	# op_str = stringCompress(ip_str)
	# print("This is the compressed string: " + op_str)
	compress_string(ip_str)

if __name__ == "__main__":
	main()