to_one_hundred = range(101)
print(*to_one_hundred)
# Add your code below!
backwards_by_tens = to_one_hundred[100:0:-10]
print(*backwards_by_tens)

to_21 = range(1, 22)
print(*to_21)
odds = [x for x in to_21 if (x % 2 != 0)]
print(*odds)
middle_third = to_21[7:14]
print(*middle_third)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(*(x for x in languages if x == "Python"))
# print filter(lambda x: x == "Python", languages)
