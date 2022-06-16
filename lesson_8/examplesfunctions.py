def comm(a='-', b=100):
    return (a*b)


def comment(c, v, *args):
    print (c + v, args)

def comments(**kwargs):
    for x,y in kwargs.items():
        print(x,y)

numbers = []

# for i in range(3):
#     number = int(input('Введите число: '))
#     numbers.append(number)
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

print(comm('=-', 70))
comment(10,20,30,40,50)
print(comm())
comments(lm=10,mm=20,j=50,bm=40,hm=80,tu=90,ym=10)
print(comm())
