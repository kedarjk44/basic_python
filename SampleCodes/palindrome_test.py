def palindrome_test(word):

    flag_palindrome = True    
    if (len(word) >= 2):
        for i in range(0, int(len(word) / 2)):
            if word[i] == word[len(word) - (i + 1)]:
                flag_palindrome = True
                continue
            else:
                print ("String is not palindrome")
                flag_palindrome = False
                break
    else:
        print ("The string you provided does not have more than or 2 characters")
        flag_palindrome = False

    if flag_palindrome:
        print ("String you entered is palindrome")


str_to_test = input('Enter a string: ')
# palindrome_test(str_to_test)

if str_to_test == str_to_test[::-1]:
    print("String is palindrome")
else:
    print("Entered string is not palindrome")
