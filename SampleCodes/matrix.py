##from numbers import matrix

##a = ([[1,2,3],[10,20,30],[100,200,300]])
a = ([[1,2,3,4],[10,20,30,40],[100,200,300,400],[11,22,33,44]])

for i in range (0,len(a)):
    for j in range (0,len(a[i])):
        print ("\t%s"%a[i][j])
rows = []
colmns = [[],[],[],[]]
eq = 0
for i in range (len(a),0,-1):
    if len(a)== len(a[len(a)-i]):
        eq = 1
    else:
        eq = 0
        print ("Rows and columns are not equal")
        break
if eq==1:
    print ("Rows and columns are equal")
    
    for i in range (len(a),0,-1):
##        print ("%s"%a[len(a)-i])
        rows.append(a[len(a)-i])

    print ("all rows = %s"%rows)
    print ("No. of rows = %s"%len(rows))

    for i in range(0,len(rows)):
        for j in range (0,len(rows[i])):
##            print ("%s"%a[i][j])
            colmns[j].append(a[i][j])

    print ("all columns = %s"%colmns)
    print ("No. of columns = %s"%len(colmns))

    for i in range (0,len(rows)):
        print ("%s %s"%(rows[i],colmns[(len(colmns)-1-i)]))
##        print ("%s"%colmns[(len(colmns)-1-i)])
