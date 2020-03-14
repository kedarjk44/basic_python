user_input = []
while True:    
    try:
        line = input()
        if line:
            user_input.append(line)
    except:
        break

eng = int(user_input[0])
eng_roll = set(user_input[1].split(" "))

fre = int(user_input[2])
fre_roll = set(user_input[3].split(" "))
#print("\n",eng,"\n",eng_roll,"\n",fre,"\n",fre_roll)
print(len(eng_roll.union(fre_roll)))
print(len(eng_roll.difference(fre_roll)))
print(len(eng_roll.intersection(fre_roll)))