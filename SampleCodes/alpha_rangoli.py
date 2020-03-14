def print_rangoli(size):
    # your code goes here
    assert(size > 0)
    assert(size < 27)
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    height_of_rangoli = (size*2) - 1
    len_of_rangoli = (height_of_rangoli * 2 ) - 1
    '''for i in range(height_of_rangoli):
        if (i != 0):
            print("")
        for j in range(len_of_rangoli):
            if (j == int(len_of_rangoli/2)):
                print(alphabets[size-1],end="")
            else:
                print("-",end="")'''
    '''for i in range(size):
        dashes1 = (size*2 - (i*2)) * "-"
        alphas = alphabets[(size-i)-1]
        dashes2 = (size*2 - (i*2)) * "-"
        print(str(len(dashes1)) + alphas + dashes1)'''
	
    for i in range(1,len_of_rangoli):
        print("-",end="")

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print_rangoli(n)