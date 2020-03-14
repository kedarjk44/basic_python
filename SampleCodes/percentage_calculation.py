if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        inp_str = input()
        student_name = inp_str.split(" ")[0]         
        list1 = []
        list1.append(float(inp_str.split(" ")[1]))
        list1.append(float(inp_str.split(" ")[2]))
        list1.append(float(inp_str.split(" ")[3]))
        student_marks[student_name] = list1
    out_student = input()
    percentage = (student_marks[out_student][0] + student_marks[out_student][1] + student_marks[out_student][2]) / 3
    print("%.2f"%percentage)