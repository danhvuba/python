# import backage
import demobackage
from demobackage.modules import *
say_hello()

# thu chay ham va xu li loi sai
try:
    print(div(5, 0))
except ZeroDivisionError:
    print("Khong chia duoc cho Zero")
finally:
    print("finall!")


# tu tao 1 Exception loi moi
class ExceptionDemo(Exception):
    def __init__(self, value):
        print("Loi:"+value)


def Chia(a, b):
    if (b == 1):
        raise ExceptionDemo("Khong can phai chia cho 1")
    return a/b


print(Chia(6, 1.5))
# print(Chia(6,1))


res = map(lambda x, y: x + ' '+y, ["tiger", "wolf"], ["dog", "cat"])
print(list(res))

result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7])
print(list(result))

print('something and nothing')