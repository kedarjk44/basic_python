#email validator
def validateUsername(name):
	pass
def validateEmailId(email):
	if '@' in email:
		if '.' in email:			
			index_at = 0
			index_dot = 0
			for i in range(len(email)):
				if (email[i] == '@'):
					index_at = i
				elif (email[i] == '.'):
					index_dot = i
			try:		
				assert (index_at != 0 and index_dot != 0)
				assert (index_at < (index_dot - 1))
				assert (index_at != (len(email) - 1) and index_dot != (len(email) - 1))
				username = email[0:index_at]
				print (username)
			except:
				print (email + " is an invalid email ID")
				return False
		else:
			print (email + " is an invalid email ID")
			return False
	else:
		print (email + " is an invalid email ID")
		return False
	print(email + " is a valid email ID")
	
	return True
def main():
	validateEmailId('a@b.com')
	
if __name__ == "__main__":
	main()