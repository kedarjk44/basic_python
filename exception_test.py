# class CriticalError(Exception):
#     def __init__(self, message='ERROR MESSAGE A'):
#         Exception.__init__(self, message)
#
#
# raise CriticalError
# raise CriticalError("ERROR MESSAGE B")


def fun(a, b=0, c=5, d=1):
    return a ** b ** c

print(fun(b=2, a=2, c=3))