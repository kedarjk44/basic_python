def dict_compare(d1,d2):
	print (d1,d2)
	d1_keys = list(d1.keys())
	d2_keys= list(d2.keys())
	print(d1_keys,d2_keys)
	if (len(d1_keys) != len(d2_keys)):
		print("no. of keys are different in dictionaries")
		return
	keymatch = True
	valmatch = True
	for d1key in d1_keys:
		if (keymatch and valmatch):
			for d2key in d2_keys:
				if d2key == d1key:
					print ('keys are same',d1key,d2key)
					if (d2[d2key] == d1[d1key]):
						print('Values are same',d2[d2key],d1[d1key])
						keymatch = True
						valmatch = True
						break
					else:
						print('Values are not same',d2[d2key],d1[d1key])
						keymatch = False
						valmatch = False					
						break
				else:
					print ('keys are not same',d1key,d2key)
					keymatch = False
					continue
		else:
			break
	
	if (keymatch and valmatch):
		print ("Both dictionaries are the same",keymatch,valmatch)
	else:
		print ("Dictionaries are not same")
        
	return

def main():
    dict1 = { 'k1':'v1', 'k2':'v2','k3':'v3'}
    dict2 = { 'k1':'v1', 'k32':'v2','k3':'v3'}
    dict3 = { 'k1':'v1', 'k2':'v2','k3':'v3'}
    dict_compare(dict1,dict2)
    

if __name__ == '__main__':
    main()
