from collections import OrderedDict

no_of_items = int(input())
item_dict = OrderedDict()
for i in range(no_of_items):
    name,price = input().strip().rsplit(" ",1)
    if (name in item_dict):
        item_dict[name] = item_dict[name] + int(price)
    else:
        item_dict[name] = int(price)
#print(item_dict)
for key in list(item_dict.keys()):
    print(key,item_dict[key])