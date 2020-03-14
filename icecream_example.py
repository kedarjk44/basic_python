import cmath
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        self.scoops = []
        for topping in self.toppings:
            for ing in self.ingredients:
                self.scoops.append([ing, topping])
        return self.scoops


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


def group_by_owners(files):
    temp_dict = {}
    for k, v in files.items():
        if v in temp_dict.keys():
            temp_dict[v].append(k)
        else:
            temp_dict[v] = []
            temp_dict[v].append(k)
    return temp_dict


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))



# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None
#
#     def next_song(self, song):
#         self.next = song
#
#     def is_repeating_playlist(self):
#         song_list = []
#         song_list.append(self.name)
#         if self.next:
#             last = self.next
#             repeats = False
#             while last.next:
#                 last = last.next
#                 print("here", last.name)
#                 if last.name in song_list:
#                     repeats = True
#                     break
#                 else:
#                     song_list.append(last.name)
#                 print("going back")
#         else:
#             return False
#         return repeats
#
#
# first = Song("Hello")
# second = Song("Eye of the tiger")
# third = Song("third song")
#
# first.next_song(second)
# second.next_song(third)
# # third.next_song()
#
# print(first.is_repeating_playlist())

def find_roots(a, b, c):
    x = (-b + ((b**2 - 4*a*c) ** 0.5)) / (2*a)
    y = (-b - ((b**2 - 4*a*c) ** 0.5)) / (2*a)
    if x == y:
        tup = (x, y)
    else:
        tup = (x, y), (y, x)
    return tup


print(find_roots(2, 10, 8))
