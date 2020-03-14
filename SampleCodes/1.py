# import unittest
# import HTMLTestRunner
import sys
#
# class testclas(unittest.TestCase):
#    def setUp(self):
#        print ("This is constructor")
#    def tearDown(self):
#        print ("This is destructor")
#    def test1(self):
#        print ("This is actual test")


def complete_reverse(str_ip):
    str_op = ""
    for i in range (0,len(str_ip)):
        str_op = str_op + str_ip[len(str_ip)-1-i]
    return str_op


def reverse_words(str_ip):
    lst1= str_ip.split(" ")
    lst2= []
    for i in range (1,len(lst1)+1):
        lst2.append(lst1[len(lst1)-i])
    str_op=""
    for i in range (0,len(lst2)):
        str_op = str_op + lst2[i]+" "
    return str_op
                    

def main():
    print ("This is test")
#    suite = unittest.TestSuite()
#    suite.addTest(testclas("test1"))
#    unittest.TextTestRunner().run(suite)
#    outfile = open("C:\Users\Kedar Kulkarni\Desktop\kktest.html","w")
#    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile, title = 'kk report', description='Test')
#    runner.run(suite)
#    return suite
    str1 = "This is python version 2.7"
    print ("%s"%str1)
#    count =0
#    for i in range(len(str1)):
#        if str1[i] == " ":
#            count +=1
#    print ("%d"%count)
    lst1 = str1.split(" ")
    lst2 = []
    print ("%s"%lst1)
    for i in range (1,len(lst1)+1):
#        print ("%s"%lst1[len(lst1) -i])
        lst2.append (lst1[len(lst1)-i])
    print ("%s"%lst2)
    str2 = ""
    for i in range (0,len(lst2)):
        str2 = str2+ lst2[i] + " "
    print ("%s"%str2)
    str2 = ""
    for i in range (0,len(str1)):
        str2 = str2 + str1[len(str1)-1-i]
    print ("%s"%str2)

    str_new = "This string is test for complete reverse function"
    print ("%s"%str_new)
    str_op = complete_reverse(str_new)
    print ("%s"%str_op)

    str_new = "This string will test reverse words function"
    print ("%s"%str_new)
    str_op = reverse_words(str_new)
    print ("%s"%str_op)

    print ("no. of arguments received: %s"%len(sys.argv))
    print ("%s"%sys.argv[0])

    i_p = input("Enter here:")
    print ("%s"%i_p)


if __name__ == '__main__':
    main()
